# FileImport
This script allows you to replace lines in a file that contain the text `![PATH]` with the contents of the specified file path.

## Usage

1. Make sure you have Python installed on your system.

2. Run the script by executing the following command in the terminal:

    ```python replace_file_content.py [file_path]```  
   Replace `[file_path]` with the path to the file you want to modify.

3. The script will search for lines in the file that contain the text `![PATH]`. If a line contains a file path, it will replace the line with the contents of the specified file.

4. If the specified file is not found, the script will print an error message.

## Example

Suppose you have a file named `input.txt` with the following content:
```
This is some text.
![PATH] "test.txt"
More text.
```

Running the script with the command `python replace_file_content.py input.txt` will replace the line `![PATH] "test.txt"` with the contents of the file `test.txt`.
