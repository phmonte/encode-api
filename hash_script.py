def encode_number(number: int):
    return hex(number)[2:]


def decode_to_number(code: str):
    return int(code, 16)
