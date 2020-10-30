
def single_byte_XOR(input_bytes,char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes+=bytes([byte^char_value])

    return output_bytes


#frequency in english of letters. E is the most common count # of occurences, then divide by length, find the difference, add difference
#smallest difference is equal to the score. 

#def score():

#array = [12,9,8,7,7,7,6,6]
    


def main():

    input_1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    input_bytes = bytes.fromhex(input_1)
   

    for i in range(256):
        print(single_byte_XOR(input_bytes,i))

    

    



main()