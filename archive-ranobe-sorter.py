# https://github.com/JumpJets/Archive-ranobelib-userscript

import os
import shutil
import zipfile

unpack_folder_name = "ranobe"

use_beautiful_name = False

remove_html = True
folder_to_remove = "chapters_html" if remove_html else "chapters_txt"
folder_to_rename = "chapters_txt" if remove_html else "chapters_html"

if not os.path.exists(unpack_folder_name):
   os.makedirs(unpack_folder_name)

class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'

print(bcolors.OKCYAN + "Ranobe renaming starts...")
counter = 0
for file_name in os.listdir('.'):
    if ".zip" in file_name:
        counter += 1
        folder_name = file_name.replace(".zip", "")
        bfname = folder_name.replace("-", " ").title()
        print(f"{bcolors.OKBLUE}{counter}. {bfname}")
        if use_beautiful_name:
            folder_name = bfname
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(f"{unpack_folder_name}/.")
        os.rename(f"{unpack_folder_name}/{folder_to_rename}", f"{unpack_folder_name}/{folder_name}")
        shutil.rmtree(f"{unpack_folder_name}/{folder_to_remove}")
        os.remove(file_name)
print(bcolors.OKGREEN + "Renaming ended!")