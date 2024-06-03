import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Compile files in provided folder.')

parser.add_argument('--input_folder', type=str, required=True, help='The input folder to process')
parser.add_argument('--output_folder', type=str, required=True, help='The output folder')
parser.add_argument('--include_paths', nargs='*', help='Include paths for the pre-processor')

args = parser.parse_args()

directory = os.fsencode(args.input_folder)
for file in os.listdir(directory):
    file_str = file.decode()
    subprocess.run(f"python3 -m compiler --input {args.input_folder}/{file_str} --render_ast {args.output_folder} --render_symb {args.output_folder} --target_llvm {args.output_folder} --target_mips {args.output_folder} --include_paths {' '.join(args.include_paths)} ", shell=True, check=True)
