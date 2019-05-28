"""
Module with main technical task logic: reading, writing, deleting and processing files.
"""

import os


def get_file_content(file_name: str) -> bytes:
    with open(file_name, 'br') as file:
        file_content = file.read()
    return file_content


def append_content(file_name: str, content: bytes) -> int:
    with open(file_name, 'ab') as file:
        file.write(content)
    return len(content)


def delete(file_name: str) -> None:
    os.remove(file_name)


def calculate_checksum(file_content: bytes) -> str:
    return str(file_content.count(b'e'))