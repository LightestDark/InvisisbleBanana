import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file_path = askopenfilename(title="Pick a file to encode")

if not file_path:
    print("No file selected")
    exit()

with open(file_path, "rb") as f:
    data = f.read()

length = len(data)
lines = []

for i in range(0, length, 6):
    chunk = data[i:i+6].ljust(6, b'\x00')
    bits = int.from_bytes(chunk, "big")
    bit_str = f"{bits:048b}"  # 48-bit string
    line = ''.join('n' if b == '0' else 'a' for b in bit_str)
    lines.append(line)

folder = os.path.join(os.path.dirname(file_path), "Banana_image")
os.makedirs(folder, exist_ok=True)

base_name = os.path.basename(file_path)
name, ext = os.path.splitext(base_name)
text_file = os.path.join(folder, f"{name}_nan.txt")

with open(text_file, "w") as f:
    f.write(f"{length}\n")
    for line in lines:
        f.write(line + "\n")

shutil.copy(file_path, folder)

print(f"Invisibananfication done! Saved text file and original into {folder}")


#DONEEE!!! 

