
#I C E  I C E   I C E 
import base64

def single_byte_XOR(input_bytes,char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes+=bytes([byte^char_value])

    return output_bytes

def key_XOR(input_bytes,key_bytes):
    return 0


def main():
    input = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    key = "ICE"
    input_bytes=bytes(input,'utf-8')
    key_bytes= bytes(key,'utf-8')
    index = 0;
    output_bytes = b''
    for byte in input_bytes:
        output_bytes+=bytes([byte^key_bytes[index]])
        index+=1
        if(index ==3):
            index = 0
    #for byte in key_bytes:
       # print(byte,end=' ')
    base16_bytes = base64.b16encode(output_bytes)
    #xor = input_bytes[0]^key_bytes[0]
    print(base16_bytes)
   





main()