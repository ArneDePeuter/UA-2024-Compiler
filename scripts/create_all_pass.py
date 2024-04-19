import os
import subprocess


directory = os.fsencode("./input")
for file in os.listdir(directory):
    file_str = file.decode("utf-8")
    str_list = file_str.split("_")
    if (str_list[2] != "pass"):
        continue

    subprocess.run(f"python3 -m compiler --input ./input/{file_str} --render_ast ./output --render_symb ./output --target_llvm ./output", shell=True, check=True)
