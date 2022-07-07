Rawtx Serializer
=========================================

A simple package to take a GETH signed transaction dictionary and return a 
raw transaction

Usage
-----

.. code-block:: python

    >>> from rawtx_serializer import transaction_serializer

    >>> transaction = {
            "blockHash": HexBytes(
                "0x5f27e154914d457180272df19abfa73868a0e72768eb497fe7ba2e5784d10cb0"
            ),
            "blockNumber": 15092359,
            "from": "0x1010101010101010101010101010101011010100",
            "gas": 21000,
            "gasPrice": 40885000000,
            "hash": HexBytes(
                "0x56a75c805678b46649a7c2ced6147c05d91a7a6b97ffcf199636a0cedf106e43"
            ),
            "input": "0x",
            "nonce": 1,
            "to": "0x1010101010101010101010101440101011010100",
            "transactionIndex": 7,
            "value": 90424686285000000000,
            "type": "0x0",
            "v": 37,
            "r": HexBytes(
                "0x181b418f79710ccd4a0ea6df0344e3b7f09dd065770c296b307837f006971c98"
            ),
            "s": HexBytes(
                "0x62434ffd15817a0e1f7990835ef14d797ac3625215b3d80fa555503ed88c34b9"
            ),
        }

    >>> transaction_serializer(transaction)

    HexBytes('0xf86d01850984ef97408252089410101010101010101010101014401010110101008904e6e50515ef8fc2008025a0181b418f79710ccd4a0ea6df0344e3b7f09dd065770c296b307837f006971c98a062434ffd15817a0e1f7990835ef14d797ac3625215b3d80fa555503ed88c34b9')

* Free software: MIT

⊂(▀¯▀⊂)