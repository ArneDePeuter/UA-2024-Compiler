import os
import re

class IncludeFileNotFoundError(Exception):
    pass

class Preprocessor:
    def __init__(self):
        self.include_files = {}
        self.defines = {}

    def preprocess(self, input_code, include_paths):
        self.collect_includes(input_code, include_paths)
        preprocessed_code = self.replace_includes(input_code, include_paths)
        preprocessed_code = self.replace_defines(preprocessed_code)
        return preprocessed_code

    def collect_includes(self, input_code, include_paths):
        include_pattern = re.compile(r'#include\s*"(.+?)"')
        includes = include_pattern.findall(input_code)
        for include_file in includes:
            file_path = self.find_include_file(include_file, include_paths)
            if file_path:
                with open(file_path, 'r') as file:
                    self.include_files[include_file] = file.read()

    def find_include_file(self, include_file, include_paths):
        for path in include_paths:
            file_path = os.path.join(path, include_file)
            if os.path.exists(file_path):
                return file_path
        return None

    def replace_includes(self, input_code, include_paths):
        include_pattern = re.compile(r'#include\s*"(.+?)"')
        return include_pattern.sub(lambda match: self.include_replace(match, include_paths), input_code)

    def include_replace(self, match, include_paths):
        include_file = match.group(1)
        if include_file in self.include_files:
            return self.include_files[include_file]
        else:
            file_path = self.find_include_file(include_file, include_paths)
            if file_path:
                with open(file_path, 'r') as file:
                    return file.read()
            else:
                raise IncludeFileNotFoundError(f"Include file not found: {include_file}")

    def replace_defines(self, input_code):
        define_pattern = re.compile(r'#define\s+(\w+)\s+(.+)')
        self.collect_defines(input_code)
        for define, value in self.defines.items():
            input_code = re.sub(r'\b' + re.escape(define) + r'\b', value, input_code)
        input_code = define_pattern.sub('', input_code)  # Remove the #define lines
        return input_code

    def collect_defines(self, input_code):
        define_pattern = re.compile(r'#define\s+(\w+)\s+(.+)')
        defines = define_pattern.findall(input_code)
        for define, value in defines:
            self.defines[define] = value