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
    else:
        print("Extended ASCII or Unicode character found, skipping...")
        return 0
    pass

def change_string(input_obj):
    """Converts a string `ASCII` and `PETSCII`. It will also construct a string
    if it is passed a list of words, where a "word" is a series of characters.

    Arguments:
        input_obj -- Either a string or a list of words to be converted

    Returns:
        A converted string.
    """
    if(type(input_obj) is not str and type(input_obj) is not list):
        obj_type = type(input_obj)
        raise TypeError(f"change_string cannot operate on a object of type \"\
{obj_type},\" only \"str\" and \"list.\"")
    else:
        ret_str = ""
        if(type(input_obj) == list):
            tmp_str = ""
            final = len(input_obj) - 1
            for word in input_obj:
                tmp_str += word
                word_index = input_obj.index(word)
                if(word_index != final):
                    tmp_str += " "
                    pass
                pass
            input_obj = tmp_str
            pass
        ret_str = ""
        for char in input_obj:
            new_c = _asc2pet(char)
            if(new_c in [-1, 0, 1]):
                _char_notif(new_c)
                continue
            else:
                ret_str += chr(new_c)
                pass
            pass
        return ret_str
    pass
