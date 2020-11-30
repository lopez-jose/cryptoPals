import base64

#receives raw bytes and returns the XOR of input_bytes with key_bytes
def key_XOR(input_bytes,key_bytes):
    index = 0;
    output_bytes = b''
    for byte in input_bytes:
        output_bytes+=bytes([byte^key_bytes[index]])
        index+=1
        if(index == len(key_bytes)):
            index = 0

    return output_bytes


def main():
    input_string = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    key = "ICE"
    input_bytes=bytes(input_string,'utf-8')
    key_bytes= bytes(key,'utf-8')

    output_bytes = key_XOR(input_bytes,key_bytes)

    base16_bytes = base64.b16encode(output_bytes)
    print(base16_bytes)
   
main()