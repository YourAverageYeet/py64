###
### Constatnts for ASC2PET
### Mike Hensley, 2023
###

from sys import argv

pass_chars = """ !"#$%&'()*+,-./0123456789:;<=>?@[]^"""

skip_chars = """\_`{|}~"""

def _asc2pet(char):
    byte = ord(char)
    if(char in skip_chars):
        return 0
    elif(byte >= 0 and byte < 32):
        return 1
    elif(char in pass_chars):
        return byte
    elif(byte > 64 and byte < 91):
        return (byte + 32)
    elif(byte > 96 and byte < 123):
        return (byte - 32)
    else:
        return -1
    pass

def char_notif(conv_val):
    if(not conv_val):
        print("Unsupported character found, skipping...")
        return 0
    elif(conv_val == 1):
        print("Control character found, skipping...")
        return 0
    elif(conv_val == -1):
        print("Extended ASCII or Unicode character found, skipping...")
        return 0
    else:
        return 0
    pass

def change_words(word_list):
    ret_list = []
    for word in word_list:
        tmp_word = []
        for c in word:
            new_c = _asc2pet(c)
            char_notif(new_c)
            tmp_word.append(new_c)
            pass
        ret_list.append(tmp_word)
        pass
    return ret_list

def main():
    argc = len(argv)
    if(not (argc - 1)):
        print("\nUSAGE: asc2pet.py word1 [word2 ...]\n")
        return 0
    else:
        print(f"\nProcrssing the following snippets: {argv[1:]}")
        print(f"{len(argv[1:])} total sentence snippets.\n")
        conv_list = change_words(argv[1:])
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
