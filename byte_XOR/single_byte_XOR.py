CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


def single_byte_XOR(input_bytes,char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes+=bytes([byte^char_value])

    return output_bytes


#frequency in english of letters. E is the most common count # of occurences, then divide by length, find the difference, add difference
#smallest difference is equal to the score. 

#bruh please starts with a,b,c,d,
#input the actual bytes
def score(input_bytes,char_value):

    sum = 0
    output_bytes=single_byte_XOR(input_bytes,char_value)
    for i in output_bytes:
        sum+=CHARACTER_FREQ.get(chr(i).lower(),0)

    return sum

   

def main():

    input_1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    input_bytes= bytes.fromhex(input_1)
    get_score = 0
    stored = ''
    largest_score=0
    for i in range(256):
        get_score=score(input_bytes,i)
        output_bytes=single_byte_XOR(input_bytes,i)
        #print(output_bytes)
        if(get_score>largest_score):
            stored= output_bytes
            largest_score=get_score
           # print(output_bytes)
        
    print(stored)

        
        

    

    



main()