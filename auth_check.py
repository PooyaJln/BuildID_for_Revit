import os
import sys

filename = ".env1"  

if os.path.exists(filename):
    print("File exists in the current directory.")
else:
    print("File does not exist in the current directory.")
    with open(filename, "w") as file:
        
        print("File created.")