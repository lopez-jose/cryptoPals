import base64

def main():
    print("hello world")
    input_1 = "this is a test"
    input_2 = "wokka wokka!!!"



    input_1_bytes = bytes(input_1,'utf-8')
    input_2_bytes = bytes(input_2,'utf-8')
    matching_bits = b''
    for byte in input_1_bytes:
        matching_bits+=bytes([input_1_bytes]^input_2_bytes[byte])

    print(matching_bits)
    for i in input_1_bytes:
        print(i)
    print(input_1_bytes)




main()