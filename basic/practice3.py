import os

# Specify the path (use '.' for current directory)
path = '/new folder'

# List all files and directories in the given path
contents = os.listdir(path)

print(f"Contents of directory '{path}':")
for item in contents:
    print(item)
