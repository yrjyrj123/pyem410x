# coding=utf-8

from bitstring import BitArray
import warnings

EM_TAG_ID_LEN = 5  # in byte


def encode(em_tag_id):
    tag_bit_array = BitArray(em_tag_id)
    if len(tag_bit_array.hex) > EM_TAG_ID_LEN * 2:
        raise ValueError("Em410x tag ID must shorter than %s bytes" % EM_TAG_ID_LEN)
    if len(tag_bit_array.hex) < EM_TAG_ID_LEN * 2:
        warnings.warn("Em410x tag ID length usually equal %s bytes" % EM_TAG_ID_LEN)
        tag_bit_array.prepend("0x" + "0" * (EM_TAG_ID_LEN * 2 - len(tag_bit_array.hex)))
    bit_with_parity = ""
    count_of_one = 0
    for i in range(0, len(tag_bit_array.bin)):
        bit_with_parity += tag_bit_array.bin[i]
        if tag_bit_array.bin[i] == "1":
            count_of_one += 1
        if (i + 1) % 4 == 0:
            if count_of_one % 2 == 0:
                bit_with_parity += "0"
            else:
                bit_with_parity += "1"
            count_of_one = 0
    col_parity = ""
    for i in range(0, 4):
        pos = i
        count_of_one = 0
        while pos < len(bit_with_parity):
            if bit_with_parity[pos] == "1":
                count_of_one += 1
            pos += 5
        if count_of_one % 2 == 0:
            col_parity += "0"
        else:
            col_parity += "1"
    bit_with_parity = bit_with_parity + col_parity
    return BitArray("0b" + "111111111" + bit_with_parity + "0")


def decode(data):
    data_bit_array = BitArray(data)
    if len(data_bit_array.bin) != 64 or data_bit_array.bin[0:9] != "111111111" or data_bit_array.bin[-1] != "0":
        raise ValueError("Not a valid em410x encoded data")
    bit_with_parity = data_bit_array.bin[9:-1]
    pos = 0
    tag_bit_string = "0b"
    while pos < 50:
        if (pos + 1) % 5 != 0:
            tag_bit_string += bit_with_parity[pos]
        pos += 1
    if encode("0x" + BitArray(tag_bit_string).hex) == data_bit_array:
        return BitArray(tag_bit_string)
    else:
        raise ValueError("Parity check error")
