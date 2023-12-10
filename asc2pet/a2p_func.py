###
### Functions used in ASC2PET
### Mike Hensley, 2023
###

# Character Strings

pass_chars = """ !"#$%&'()*+,-./0123456789:;<=>?@[]^"""
"""Characters `_asc2pet` should pass over"""

skip_chars = """\_`{|}~"""
"""Characters in `ASCII` that have no equivalent in `PETSCII`"""

def _asc2pet(char):
    """Converts a single string between ASCII and PETSCII
    
    Arguments:
        char -- The character to be converted

    Returns:
        An integer value dependant on what kind of character is input
    """    
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
    """Alerts the user to a notable character in their string.
    While this function does not say *where* the offending character is, it
    should be quite obvious 

    Arguments:
        conv_val -- An output value from `_asc2pet()`

    Returns:
        Always returns 0; any output is through messages printed to stdout.
    """    
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
    """Converts a list of words between `ASCII` and `PETSCII`. In this context
    a "word" is a series of characters.

    Arguments:
        word_list -- A list of words to be converted

    Returns:
        A list of converted words. Spaces not included.
    """    
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
