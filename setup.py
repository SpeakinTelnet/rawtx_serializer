#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ["rlp",
                "eth_account",
                "eth_utils"]

test_requirements = ['pytest>=3','nox']

setup(
    author="SpeakinTelnet",
    author_email='gui.lac@protonmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    description="A simple package to take a GETH signed transaction dict and return a raw transaction",
    install_requires=requirements,
    license='License :: OSI Approved :: MIT License',
    long_description=readme,
    include_package_data=True,
    keywords='rawtx_serializer',
    name='rawtx_serializer',
    packages=find_packages(include=['rawtx_serializer*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SpeakinTelnet/rawtx_serializer',
    version='1.0.0',
    zip_safe=False,
)
