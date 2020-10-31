
#I C E  I C E   I C E 


def single_byte_XOR(input_bytes,char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes+=bytes([byte^char_value])

    return output_bytes

def main():
    input = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    key = "ICE"
    input_bytes=bytes(input,'utf-8')
    key_bytes= bytes(key,'utf-8')
    
    for byte in input_bytes:
        #print(byte,end=' ')
    for byte in key_bytes:
        print(byte,end=' ')
   





main()