
#I C E  I C E   I C E 


def single_byte_XOR(input_bytes,char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes+=bytes([byte^char_value])

    return output_bytes

def main():
    input = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    key = "ICE"
    count = 0
    output = ''
    for i in input:
        #print (i)
        xor = i^key[count]
        output+=xor
        if(count == 2):
            count = 0
    print(output)



main()