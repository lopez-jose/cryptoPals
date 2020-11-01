import base64


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
    lowest_avg_hamming = 0
    for i in range(39):
        i+=2
        print(string_bytes[:i])
        print(string_bytes[i:2*i])
        print(hamming_distance(string_bytes[:i],string_bytes[i:2*i]))
    input_1 = "this is a test"
    input_2 = "wokka wokka!!!"

    bytes_1 = bytes(input_1, 'utf-8')
    bytes_2 = bytes(input_2, 'utf-8')

    print(hamming_distance(bytes_1, bytes_2))


main()
