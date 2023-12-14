###
### D64TOOL Function File
### Mike Hensley 2023
###

# Imports

from io import BufferedReader as bin_file # Needed to check if binary file

# Custom Error Definitions

class SizeError(ValueError):
    pass

class TrackError(ValueError):
    pass

class SectorError(ValueError):
    pass

# Variables

BAM_OFF = 0x16500 # Offset for the [B]lock [A]llocation [M]ap

DIR_OFF = BAM_OFF + 256 # Offset for the directory of the disk

DIR_INTER = 256 * 3 # Standard sector interleave for the directory

SIZES = [174848, 175531, 196608, 197376]

TRACK_OFFS = { # Track offsets
     1 : 0x00000,  2 : 0x01500, # Guaranteed Tracks
     3 : 0x02A00,  4 : 0x03F00,
     5 : 0x05400,  6 : 0x06900,
     7 : 0x07E00,  8 : 0x09300,
     9 : 0x0A800, 10 : 0x0BD00,
    11 : 0x0D200, 12 : 0x0E700,
    13 : 0x0FC00, 14 : 0x11100,
    15 : 0x12600, 16 : 0x13B00,
    17 : 0x15000, 18 : 0x16500,
    19 : 0x17800, 20 : 0x18B00,
    21 : 0x19E00, 22 : 0x1B100,
    23 : 0x1C400, 24 : 0x1D700,
    25 : 0x1EA00, 26 : 0x1FC00,
    27 : 0x20E00, 28 : 0x22000,
    29 : 0x23200, 30 : 0x24400,
    31 : 0x25600, 32 : 0x26700,
    33 : 0x27800, 34 : 0x28900,
    35 : 0x29A00, 36 : 0x2AB00, # Start of Extra Tracks (36)
    37 : 0x2BC00, 38 : 0x2CD00,
    39 : 0x2DE00, 40 : 0x2EF00
}

# Disk Operation Functions

def _check_d64_file(file_obj): # Checks if a given open file is in binary mode
    if(not isinstance(file_obj, bin_file)):
        t_ = type(file_obj)
        raise TypeError("These functions can only operate on binary file\
objects.", f"Supplied object is of type \"{t_}.\"")
    disk_size = file_obj.seek(0, 2)
    if(disk_size not in SIZES):
        raise SizeError("File is not a valid D64 image.")
    else:
        return 0
    pass

def _check_trak_sect(track, sector): # Checks that a given track/sector pair are valid
    if(track not in range(1, 41)):
        raise TrackError(f"Invalid track number ({track}); should be within 1- 40")
    elif(track in range(1, 18) and sector not in range(1, 22)):
        raise SectorError(f"Invalid sector number ({sector}); should be within 1-21")
    elif(track in range(18, 25) and sector not in range(1, 20)):
        raise SectorError(f"Invalid sector number ({sector}); should be within 1-19")
    elif(track in range(25, 31) and sector not in range(1, 19)):
        raise SectorError(f"Invalid sector number ({sector}); should be within 1-18")
    elif(track in range(31, 41) and sector not in range(1, 18)):
        raise SectorError(f"Invalid sector number ({sector}); should be within 1-17")
    pass

def _pull_block(d64_file_obj, block_offset): # Pulls a single block (256 bytes) from the disk
    start_off = d64_file_obj.tell()
    d64_file_obj.seek(block_offset)
    block = []
    for i in range(0, 256):
        byte = d64_file_obj.read(1)
        block.append(byte[0])
        pass
    d64_file_obj.seek(start_off)
    return block

def _pull_linked(d64_file_obj, starting_block):
    block_list = []
    block_offset = starting_block
    read_block = True
    while(read_block == True):
        _block = _pull_block(d64_file_obj, block_offset)
        block_list.append(_block)
        trak_sect = _block[0:2]
        if(trak_sect == [0, 0]):
            read_block = False
            continue
        else:
            _check_trak_sect(trak_sect[0], trak_sect[1])
            block_offset = TRACK_OFFS[trak_sect[0]] + (256 * trak_sect[1])
            pass
        pass
    return block_list

def pull_BAM(d64_file_obj): # Pulls the BAM from a disk (wrapper for _pull_block)
    _check_d64_file(d64_file_obj)
    BAM = _pull_block(d64_file_obj, BAM_OFF)
    return BAM

def pull_dir_blocks(d64_file_obj): # Pulls the directory blocks of a disk (wrapper for _pull_linked)
    _check_d64_file(d64_file_obj)
    dir_ = _pull_linked(d64_file_obj, DIR_OFF)
    return dir_

# Miscellaneous Functions

def print_block(block_obj):
    for i in range(0, 16):
        off = 16 * i
        end = off + 16
        print(f"{off:02X}: ", end="")
        for b in block_obj[off:end]:
            print(f"{b:02X}", end=" ")
            pass
        print("  ", end="")
        for b in range(off, end):
            b2 = block_obj[b]
            if(b2 in range(0, 32) or b2 == 0x7F):
                print(".", end="")
                pass
            else:
                print(chr(b2), end="")
                pass
            pass
        print("")
        pass
    return 0
    