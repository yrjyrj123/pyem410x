# pyem410x
[![PyPI version](https://img.shields.io/pypi/v/pyem410x.svg)](https://pypi.python.org/pypi/pyem410x/)
[![Build Status](https://travis-ci.org/yrjyrj123/pyem410x.svg?branch=master)](https://travis-ci.org/yrjyrj123/pyem410x)

A python module for Em410x ID card encode and decode.

## Installation
	pip install pyem410x

## How to use it
	>>> import pyem410x
	>>> pyem410x.encode("0x1234567890")	
	BitArray('0xff8ca64a98f8c802')
	>>> pyem410x.decode("0xff8ca64a98f8c802")
	BitArray('0x1234567890')

## Use Case
If you want to clone a Em410x card, You need a T5577 card which can read/write. You can get Em410x ID from origin card easily, but before you write it in T5577 you need encode it by **pyem410x**.

Assume your Em410x ID is **0x1234567890**, after be encoded by **pyem410x** is **0xff8ca64a98f8c802**.
You should write **0xff8ca64a** in T5577 page0 block1 and write **0x98f8c802** in page0 block2, and you will get a same ID card.

## About Em410x
This legend shows how **0x1234567890** be encoded as **0xff8ca64a98f8c802**.

![Em410x legend](https://github.com/yrjyrj123/image/raw/master/em410x_legend.png)
