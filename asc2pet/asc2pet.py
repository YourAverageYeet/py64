###
### Main Script for ASC2PET
### Mike Hensley, 2023
###

from sys import argv
import a2p_func as a2pf

def main():
    argc = len(argv)
    if(not (argc - 1)):
        print("\nUSAGE: asc2pet.py word1 [word2 ...]\n")
        return 0
    else:
        print(f"\nProcrssing the following snippets: {argv[1:]}")
        print(f"{len(argv[1:])} total sentence snippets.\n")
        conv_str = a2pf.change_string(argv[1:])
        print(f"\nConverted string:\n\t{conv_str}\n")
        return 0
    pass

if __name__ == "__main__":
    main()
    pass
