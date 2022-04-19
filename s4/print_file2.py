from pathlib import Path
filename = input("File's name: ")

try:
    file_contents = Path(filename).read_text()

    lines = file_contents.splitlines()
    head = lines[0]
    print(f"First line of the{filename} file: \n{head}")


except FileNotFoundError:
    print(f"[ERROR]: file'{filename}'not found")
except IndexError:
    print(f"file'{filename}' is empty")