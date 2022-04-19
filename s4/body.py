from pathlib import Path
filename = input("File's name: ")

try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    print(f"Body of the {filename} file:")
    for line in body:
        print(line)
except FileNotFoundError:
    print(f"[ERROR]: file'{filename}'not found")
except IndexError:
    print(f"file'{filename}' is empty")