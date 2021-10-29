#!/usr/bin/env python3
import serial
from time import time
import os

def main():
    with serial.Serial('/dev/ttyACM0', 115200) as edison:
        print_timestamp = time()
        while True:
            if edison.readline().strip() == b'1':
                if (time() - print_timestamp) > 30:
                    print("Analyzing...")
                    os.system('lp report.pdf')
                    print_timestamp = time()
                else:
                    print(time() - print_timestamp)
            else:
                print("Waiting...")

if __name__ == '__main__':
    main()
