import base64

input1 = "1c0111001f010100061a024b53535009181c"
input2= "686974207468652062756c6c277320657965"

#message1=   input1.upper()
#message2=   input2.upper()  

dec1 = int(input1,16)
dec2=int(input2,16)
xor=dec1^dec2

#xor = input1_bytes^input2_bytes


print(xor)