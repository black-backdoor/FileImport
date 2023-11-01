#
# Script: replace_file_content.py
# Description: This script replaces lines in a file that contain the text ![PATH] with the contents of the specified file path.
# Version: 1.0.0
# Author: black-backdoor
# GitHub: https://github.com/black-backdoor/FileImport
#

# EXAMPLE FOR STRING
# ![PATH] "example.txt"


import re
import argparse


def replace_file_content(output_path, file_path):

    # Read the contents of the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Search for lines that contain the text ![PATH]
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if '![PATH]' in line:

            # Extract the file path from the line
            pattern = r'!\[PATH\] "(.*?)"'
            match = re.search(pattern, line)
            path = match.group(1)


            try:
                # Read the content of the specified file
                with open(path, 'r') as replacement_file:
                    replace_file_content = replacement_file.read()
                
                # Replace the ![PATH] text with the content of the file
                lines[i] = replace_file_content
                print(f"ADDED FILE:{path}")
            
            except FileNotFoundError:
                print(f"File not found: {path}")

    # Write the modified content back to the original file
    with open(output_path, 'w') as file:
        file.write('\n'.join(lines))


def main():
    parser = argparse.ArgumentParser(description='Script description')
    parser.add_argument('file_path', help='Path to the file')
    parser.add_argument('--output_path', help='Path to the output file (optional)')

    args = parser.parse_args()

    if args.output_path:
        output_path = args.output_path
    else:
        output_path = args.file_path

    replace_file_content(output_path, args.file_path)


if __name__ == '__main__':
    main()
