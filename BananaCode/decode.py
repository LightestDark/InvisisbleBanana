import os
import subprocess
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file_path = askopenfilename(title="Pick a nanana text file", filetypes=[("NaN text", "*.txt")])

if not file_path:
    print("No file selected")
    exit()

with open(file_path, "r") as f:
    lines = f.read().splitlines()

length = int(lines[0])
data_lines = lines[1:]
output = bytearray()

for line in data_lines:
    bits = ''.join('0' if c == 'n' else '1' for c in line)
    payload = int(bits, 2)
    output.extend(payload.to_bytes(6, "big"))

output = output[:length]

folder = os.path.dirname(file_path)
base_name = os.path.basename(file_path).replace("_nan.txt", "")

original_copy = os.path.join(folder, base_name)
if os.path.exists(original_copy):
    _, ext = os.path.splitext(original_copy)
else:
    ext = ".png"

restored_file = os.path.join(folder, f"{base_name}_restored{ext}")

with open(restored_file, "wb") as f:
    f.write(output)

print("Banana restored! Saved as", restored_file)

try:
    if os.name == 'nt':
        os.startfile(restored_file)
    elif os.name == 'posix':
        subprocess.run(['xdg-open', restored_file])
    else:
        print("Open manually:", restored_file)
except Exception:
    print("Could not auto-open. Open manually:", restored_file)
