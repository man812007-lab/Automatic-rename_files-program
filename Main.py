import os
import sys

folder = os.getcwd()
script_name = os.path.basename(sys.argv[0])

for file in os.listdir(folder):
    old_path = os.path.join(folder, file)

    # skip the script/exe itself
    if file == script_name:
        continue

    # skip folders
    if not os.path.isfile(old_path):
        continue

    ext = os.path.splitext(file)[1]
    new_name_input = input(f"Enter new name for {file}: ")
    new_name = f"{new_name_input}{ext}"

    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)

    print(f"Renamed to: {new_name}")
    print("------")
  
