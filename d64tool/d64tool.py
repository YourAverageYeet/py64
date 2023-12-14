###
### Main D64TOOL script file
### Mike Hensley 2023
###

from os.path import isfile
from sys import argv
import d64t_func as d64f

def main():
    argc = len(argv)
    if(not (argc - 1)):
        print("\nd64tool.py [option] disk_image.d64\n")
        pass
    else:
        print(f"Displaying BAM for {argv[1]}...\n")
        with open(argv[1], "rb") as d64:
            bam = d64f.pull_BAM(d64)
            d64f.print_block(bam)
            pass
        pass
    return 0

if __name__ == "__main__":
    main()
    pass
