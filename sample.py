# generate_binary_file.py

import os

# Define file name and size
file_name = "sample.bin"
file_size = 1024  # 1 KB

# Generate random binary data
with open(file_name, "wb") as file:
    file.write(os.urandom(file_size))

print(f"Binary file '{file_name}' of size {file_size} bytes created successfully.")
