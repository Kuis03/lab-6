import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        return

    pathFile1 = sys.argv[1]
    pathFile2 = sys.argv[2]

if __name__ == "__main__":
    main()

import json

def load_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON syntax in file '{filename}'.")
        return None

data = load_json('pathFile1.json')
if data:
    print(data) 
