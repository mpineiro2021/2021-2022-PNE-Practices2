from pathlib import Path
from typing import List

filename = input("File's name: ")

try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    total = 0
    for line in body:
        total = total + len(line)
    print(f"Total number of bases: {total}")
except FileNotFoundError:
    print(f"[ERROR]: file'{filename}'not found")
except IndexError:
    print(f"file'{filename}' is empty")