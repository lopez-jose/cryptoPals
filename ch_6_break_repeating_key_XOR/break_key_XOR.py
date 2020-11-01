import base64

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

   
def hamming_distance(bytes_1, bytes_2):
    index = 0
    XOR_bytes = b''
    for byte in bytes_1:
        x = bytes([byte ^ bytes_2[index]])
        XOR_bytes += x
        index += 1

    count = 0
    for byte in XOR_bytes:
        temp = byte
        for i in range(7):
            if(temp & 1 != 0):
                count += 1
            temp = temp >> 1

    return count


def main():
    f = open("file.txt","r")
    line = f.readline()
    s = ""
    s+=line
    while line:
        #print(line)
        line =f.readline()
        s+=line
    print(s)
    string_bytes = bytes(s,'utf-8')
    lowest_avg_hamming = hamming_distance(string_bytes[:2],string_bytes[2:4])/2
    print(lowest_avg_hamming)
    key_length = 0
    key_lengths =[3,5.0]
    
    #listname.sort
    for i in range(39):
        i+=2
        length = len(string_bytes[:i])
        #print(len(string_bytes[i:i*2]))
        avg_hamming = hamming_distance(string_bytes[:i],string_bytes[i:2*i])/length
        print(avg_hamming)
        key_lengths.append([(i,avg_hamming)])
    
    #key_lengths.sort()

    print(key_lengths)
   # print(key_length)
main()
