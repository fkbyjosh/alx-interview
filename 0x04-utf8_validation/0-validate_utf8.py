#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: List of integers, each representing 1 byte of data.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes_to_process = 0

    # Masks for checking UTF-8 bytes
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Keep only the 8 least significant bits
        byte = byte & 0xFF

        # If we are not processing a multi-byte character
        if num_bytes_to_process == 0:
            # Count how many bytes this character is
            if byte >> 7 == 0:  # 0xxxxxxx - 1 byte character
                continue
            elif byte >> 5 == 0b110:  # 110xxxxx - 2 byte character
                num_bytes_to_process = 1
            elif byte >> 4 == 0b1110:  # 1110xxxx - 3 byte character
                num_bytes_to_process = 2
            elif byte >> 3 == 0b11110:  # 11110xxx - 4 byte character
                num_bytes_to_process = 3
            else:
                return False
        else:
            # Check if the byte starts with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes_to_process -= 1

    # All characters must be complete
    return num_bytes_to_process == 0
