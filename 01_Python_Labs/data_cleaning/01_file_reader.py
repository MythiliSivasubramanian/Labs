"""
01_file_reader.py

1.Different ways of Opening a file : 

Basic types
    1. open() + close()
    2. with open()
    3. pathlib.Path().open()
    4. Path.read_text() / read_bytes()
 
Reading a file:
    1. Read entire file    :   f.read()
    2. Read fixed amount   :   f.read(100)
    3. Read line by line (streaming)   : for line in f:
    4. Read one line at a time manually : f.readline()
    5. Read all lines into list    :   f.readlines()
 
Memory vs Performance experiments:
    1. File size vs time to read
    2. Memory heavy vs streaming
    3. Readlines vs loop speed
    4. Read chunk size effects

Modes & encodings:
    Modes:
        r, w, a, x, b, t
        
    Encoding:
        utf-8 
        utf-16 
        latin1
    
    Error handling:
        errors="ignore"
        errors="replace"
    

Realworld safety checks:
    
    File exsistance:
        1. Path(path).exists()
        
    Check file size before reading:
        1. Path(path).stat().st_size
        
    Try/except blocks


 
2.Modes & Encoding:
 Different modes for opening a file:
    - ("r" - Read) : Default value. Opens a file for reading, error if the file does not exist
    - ("a" - Append) : Opens a file for appending, creates the file if it does not exist
    - ("w" - Write) : Opens a file for writing, creates the file if it does not exist
    - ("x" - Create): Creates the specified file, returns an error if the file exists
    Basic types of files, 
    "t" - Text mode - Default value. rt
    "b" - Binary mode  rb
    
    2.1 Encoding variations (utf-8, utf-16, latin1):
        (utf-8, utf-16, latin1)
        Errors when encoding mismatch
    
"""
print(f"\n\nExperiment on different methods of Opening & Reading a file using Python")
print("-" * 75,)

raw_data_path = "/Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/Labs/01_Python_Labs/data_cleaning/raw_data.txt"

# Opening a File

# Method 1. Open(filename,mode) 
# Raises error if file not found
# Need to close the file once done

try:
    f = open("raw_data.txt")  # Default mode is "rt" 
    print(f.read()) # whole file is loaded to memory
    f.close() # Need to close the file once done
except FileNotFoundError as e:
    print("\nReading the file raw_data_txt using Method 1: 'open' using filename :"
          f"\nError: ",e,"\n\n")

f1 = open(raw_data_path)  
print(f"\nReading the file using Method 1 'open' using path of filename :\n"
      f"{f1.read()}") # whole file is loaded to memory
f1.close() # Need to close the file once done

# Method 2. using with open

with open (raw_data_path) as f2:  
    print(f"\n\nReading the file using Method 2 . 'with open' : \n"
          f"\n{f2.read()}") # whole file is loaded to memory
# With open automatically closes the file

# Method 3. Using from pathlib import path

from pathlib import Path  
data = Path(raw_data_path).read_text(encoding = "utf-8") # whole file is loaded to memory
print(f"\nReading the file using Method 3. 'from pathlib import Path' :\n\n{data}\n\n")

"""
opens the file, read it and closes the file.
Strings : read_text() Bytes : read_bytes()
"""

# Line-by-Line Reading 
# Goal : Memory-efficient reading

# 1. Using for loop
print(f"\n\nMethods of reading a file:"
      f"\nMethod 1: -read() :\n"
      f"\tLoads entire file into memeory."
      f"\nMethod 2: Line-by-Line Reading :"
      f"\n1.Using for loop :\n"
      f"\n2.Using .readline()\n\n")

print("\n\nReading a file using a for loop :\n")
with open(raw_data_path) as f3:
    for line in f3:
        print(line.strip())  # or print(line, end = "")
        
        # Each line read from a text file usually already ends with \n.
        # print(line) adds another newline by default (end="\n"), 
        # so we see a blank line between lines.

# 2. Using .readlines()

print(f"\n\nReading a file Using .readlines() :\n")
with open(raw_data_path) as f4:
    # print(f4.readlines()) This prints the entire list including \n characters, hard to read
    lines = f4.readlines()
    for line in (lines):
        print(f"{line.strip()}")

# 2.1 Modes & Encoding


