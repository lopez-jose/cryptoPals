import base64

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


def single_byte_XOR(input_bytes, char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])

    return output_bytes


# takes the input_bytes string and the char value and calculates the score using a xor of said bytes with a specific char
# takes the result of the xor and gives it a score according to the dictionary value

def score(input_bytes, char_value):

    sum = 0
    output_bytes = single_byte_XOR(input_bytes, char_value)
    for i in output_bytes:
        sum += CHARACTER_FREQ.get(chr(i).lower(), 0)

    return sum

# finds the hamming distance between two even sized byte strings


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
    # Opens the file and reads
    f = open("file.txt", "r")
    line = f.readline()

    s = ""
    s += line
    #loops f.readline and adds input to the s string
    while line:
        line = f.readline()
        s += line

    #converts s into bytes and removes utf-8 encoding
    string_bytes = bytes(s, 'utf-8')
 
    strings = []
    decrypted_strings = []
    length = 6
    # here each respective array of strings for strings and decrypted_strings
    for i in range(length):
        strings.append("")
        decrypted_strings.append("")

    pos = 0
    # here the string is split into substrings length times
    for i in range(len(string_bytes)):
        strings[pos] += str(string_bytes[i])
        pos += 1
        if(pos > length-1):
            pos = 0
    # here each substring is then decrypted using a single char XOR
    # the result is then stored in decrypted_strings[i]
    for i in range(length):
        input_bytes = bytes(strings[i], 'utf-8')
        get_score = 0
        stored = ''
        largest_score = 0
        for p in range(256):
            get_score = score(input_bytes, p)
            output_bytes = single_byte_XOR(input_bytes, p)

            if(get_score > largest_score):
                stored = output_bytes
                largest_score = get_score
        decrypted_strings[i] = stored

    pos = 0
    decrypted = ""
    # here we combine the split decrypted substrings into one original string
    for i in range(int(len(string_bytes)/length)):
        print(chr(decrypted_strings[pos][i]), end="")
        pos += 1
        if(pos > length-1):
            pos = 0
    print(decrypted)


    #the hamming class is used to store an object where index and distance are recorded
    class Hamming:
        def __init__(self,index,distance):
            self.index = index  
            self.distance = distance
    my_hamming = []
    
    for i in range(39):
        i += 2
        length = len(string_bytes[:i])
        avg_hamming = hamming_distance(
            string_bytes[:i], string_bytes[i:2*i])/length
        my_hamming.append(Hamming(i,avg_hamming))
    new_hamming_list = sorted(my_hamming,key = lambda Hamming: Hamming.distance)
    print("The sorted list will now be printed")    
    for i in range (len(new_hamming_list)):
        print("Length = ", end = " ")
        print(new_hamming_list[i].index, end = " \t")
        print (" Hamming Distance = ", end = " \t")
        print(round((new_hamming_list[i].distance),3))
        
main()
