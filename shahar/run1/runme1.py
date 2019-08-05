import os
import sys
def main():
    if len(sys.argv) != 2:
        print("Python runme1.py [YOUR_NAME]")
    else:
        print(f'{sys.argv[1]}, Your computer name is {os.environ["COMPUTERNAME"]}')


if __name__ == '__main__':
    main()