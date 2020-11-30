import base64

def hex_xor(input_1, input_2):
    bits_1= int(input_1, 16)
    bits_2= int(input_2,16)
    xor = bits_1^bits_2
    return hex(xor)[2:] #the [n:] removes the first two characters

def main():
    input_1 = "1c0111001f010100061a024b53535009181c"
    input_2= "686974207468652062756c6c277320657965"



    print(hex_xor(input_1,input_2))

    

    

main()