"""Provide functions to hash transaction attributes into a rawtransaction"""
from cytoolz import pipe
from hexbytes import HexBytes
import rlp

from eth_utils.curried import apply_formatters_to_dict

from eth_account._utils.legacy_transactions import (
    Transaction,
)

from eth_account._utils.typed_transactions import DynamicFeeTransaction

from eth_account._utils.validation import (
    LEGACY_TRANSACTION_FORMATTERS,
)


def _serialize_type0_transaction(transaction_dict):
    """return a raw transaction from a set of attributes"""

    filled_transaction = pipe(
        transaction_dict,
        dict,
        apply_formatters_to_dict(LEGACY_TRANSACTION_FORMATTERS),
    )
    serialized = Transaction.from_dict(filled_transaction)
    return rlp.encode(serialized)


def _filter_type0_fields(transaction):
    return {
        "nonce": transaction["nonce"],
        "gasPrice": transaction["gasPrice"],
        "gas": transaction["gas"],
        "to": transaction["to"],
        "value": transaction["value"],
        "data": transaction["input"],
        "v": transaction["v"],
        "r": transaction["r"],
        "s": transaction["s"],
    }


def _filter_type2_fields(transaction):

    return {
        "nonce": transaction["nonce"],
        "maxFeePerGas": transaction["maxFeePerGas"],
        "gas": transaction["gas"],
        "maxPriorityFeePerGas": transaction["maxPriorityFeePerGas"],
        "to": HexBytes(transaction["to"]) if "to" in transaction else None,
        "value": transaction["value"],
        "type": transaction["type"],
        "accessList": transaction["accessList"],
        "chainId": transaction["chainId"],
        "data": HexBytes(transaction["input"]),
        "v": transaction["v"],
        "r": transaction["r"],
        "s": transaction["s"],
    }


def transaction_serializer(transaction):
    match transaction["type"]:
        case "0x0":
            filtered_transaction = _filter_type0_fields(transaction)
            return HexBytes(_serialize_type0_transaction(filtered_transaction))
        case "0x2":
            filtered_transaction = _filter_type2_fields(transaction)
            rawdata = DynamicFeeTransaction.from_dict(filtered_transaction)
            return HexBytes("0x02" + rawdata.payload().hex())
        case _:
            raise ValueError("Unknown Transaction type")
