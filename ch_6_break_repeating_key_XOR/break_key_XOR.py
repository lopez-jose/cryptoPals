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
    while line:
        print(line)
        line =f.readline()
    input_1 = "this is a test"
    input_2 = "wokka wokka!!!"

    bytes_1 = bytes(input_1, 'utf-8')
    bytes_2 = bytes(input_2, 'utf-8')

    print(hamming_distance(bytes_1, bytes_2))


main()
