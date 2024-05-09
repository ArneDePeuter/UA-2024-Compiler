import re
import os

class Preprocessor:
    def __init__(self):
        self.include_files = {}
        self.defines = {}
        self.stdio_included = False

    def preprocess(self, input_code, include_paths):
        self.collect_includes(input_code, include_paths)
        preprocessed_code = self.replace_includes(input_code, include_paths)
        preprocessed_code = self.replace_defines(preprocessed_code)
        return preprocessed_code

    def collect_includes(self, input_code, include_paths):
        include_pattern = re.compile(r'^\s*#include\s*[<"](.+?)[>"]', re.MULTILINE)
        comment_pattern = re.compile(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"', re.DOTALL | re.MULTILINE)

        # Remove comments from the input code
        input_code = comment_pattern.sub('', input_code)

        includes = include_pattern.findall(input_code)
        for include_file in includes:
            if include_file == 'stdio.h':
                self.stdio_included = True
                self.include_files[include_file] = ""
            elif include_file not in self.include_files:
                file_path = self.find_include_file(include_file, include_paths)
                if file_path:
                    with open(file_path, 'r') as file:
                        included_code = file.read()
                        self.include_files[include_file] = included_code
                        self.collect_includes(included_code, include_paths)  # Recursively collect includes

    def find_include_file(self, include_file, include_paths):
        for path in include_paths:
            file_path = os.path.join(path, include_file)
            if os.path.exists(file_path):
                return file_path
        return None

    def replace_includes(self, input_code, include_paths):
        include_pattern = re.compile(r'^\s*#include\s*[<"](.+?)[>"]', re.MULTILINE)
        return include_pattern.sub(lambda match: self.include_replace(match, include_paths), input_code)

    def include_replace(self, match, include_paths):
        include_file = match.group(1)
        if include_file in self.include_files:
            return self.replace_includes(self.include_files[include_file], include_paths)  # Recursively replace includes
        else:
            file_path = self.find_include_file(include_file, include_paths)
            if file_path:
                with open(file_path, 'r') as file:
                    included_code = file.read()
                    self.include_files[include_file] = included_code
                    return self.replace_includes(included_code, include_paths)  # Recursively replace includes
            else:
                return f"Include file not found: {include_file}"

    def replace_defines(self, input_code):
        define_pattern = re.compile(r'^\s*#define\s+(\w+)\s+(.+)', re.MULTILINE)
        self.collect_defines(input_code)
        for define, value in self.defines.items():
            input_code = re.sub(r'\b' + re.escape(define) + r'\b', value, input_code)
        input_code = define_pattern.sub('', input_code)
        return input_code

    def collect_defines(self, input_code):
        define_pattern = re.compile(r'^\s*#define\s+(\w+)\s+(.+)', re.MULTILINE)
        comment_pattern = re.compile(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"', re.DOTALL | re.MULTILINE)

        # Remove comments from the input code
        input_code = comment_pattern.sub('', input_code)

        defines = define_pattern.findall(input_code)
        for define, value in defines:
            self.defines[define] = value