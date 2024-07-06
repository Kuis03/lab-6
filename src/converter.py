import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        return

    pathFile1 = sys.argv[1]
    pathFile2 = sys.argv[2]

if __name__ == "__main__":
    main()
