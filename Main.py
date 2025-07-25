import os
import time
import zipfile
import shutil
import urllib.request
import subprocess

print("Make sure you are running this program with administrative privileges.")
time.sleep(2)
print("Loading complete.")
print("Press '1' to install Bepinex (Mod software), '2' to manage your files, or '3' to exit.")
choice = input()

match choice:
    case '1':
        with urllib.request.urlopen("https://thunderstore.io/package/download/BepInEx/BepInExPack_PEAK/5.4.2403/") as response, open("BepInExPack_PEAK.zip", 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        target_dir = r"C:\Program Files (x86)\Steam\steamapps\common\PEAK"
        os.makedirs(target_dir, exist_ok=True)
        with zipfile.ZipFile("BepInExPack_PEAK.zip", 'r') as zip_ref:
            for member in zip_ref.namelist():
                if member.startswith("BepInExPack_PEAK/"):
                    target_path = os.path.join(target_dir, member[len("BepInExPack_PEAK/"):])
                    if member.endswith('/'):
                        os.makedirs(target_path, exist_ok=True)
                    else:
                        os.makedirs(os.path.dirname(target_path), exist_ok=True)
                        with zip_ref.open(member) as source, open(target_path, "wb") as target:
                            shutil.copyfileobj(source, target)
        print(f"BepInExPack extracted to {target_dir}")
    case '2':
        print("Opening plugin folder")
        directory_path = r"C:\Program Files (x86)\Steam\steamapps\common\PEAK\BepInEx\plugins"
        try:
            subprocess.Popen(f'explorer "{directory_path}"')
        except Exception as e:
            print(f"Error opening file explorer: {e}")

    case '3':
        print("Exiting the tool. Goodbye!")
        exit()
    case _:
        print("Invalid command")