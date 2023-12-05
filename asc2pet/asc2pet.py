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
        conv_list = a2pf.change_words(argv[1:])
        new_sentence = ""
        print("\nConverted sentence: ", end="")
        for word in conv_list:
            for b in word:
                print(chr(b), end="")
                pass
            if(conv_list.index(word) == (len(conv_list) - 1)):
                print("\n")
                pass
            else:
                print(" ", end="")
                pass
            pass
        return 0
    pass

if __name__ == "__main__":
    main()
    pass
