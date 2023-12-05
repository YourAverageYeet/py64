###
### Functions used in ASC2PET
### Mike Hensley, 2023
###

# Character Strings

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

def _char_notif(conv_val):
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
            _char_notif(new_c)
            tmp_word.append(new_c)
            pass
        ret_list.append(tmp_word)
        pass
    return ret_list
