# coding=utf-8

import em410x
from bitstring import BitArray


def test_encode():
    # 正常情况
    data = em410x.encode("0x12c6824e32")
    assert data == BitArray("0xff8cb8644a9e98b0")
    # 长度超过EM_TAG_ID_LEN
    try:
        em410x.encode("0x000000000000")
        assert False
    except ValueError:
        assert True


def test_decode():
    # 正常情况
    tag_id = em410x.decode("0xff8cb8644a9e98b0")
    assert tag_id == BitArray("0x12c6824e32")
    # 非0b111111111开头
    try:
        em410x.decode("0xdf8cac7c64318c66")
        assert False
    except ValueError:
        assert True
    # 长度不是64bit
    try:
        em410x.decode("0xff8cac7c64318c660")
        assert False
    except ValueError:
        assert True
    # 非0b0结尾
    try:
        em410x.decode("0xff8cac7c64318c61")
        assert False
    except ValueError:
        assert True
    # 校验和错误
    try:
        em410x.decode("0xff8cac7c64311c66")
        assert False
    except ValueError as e:
        assert True
