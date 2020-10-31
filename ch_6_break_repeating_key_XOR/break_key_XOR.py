import base64



def main():
    input_1 = "this is a test"
    input_2 = "wokka wokka!!!"


    index = 0

    input_1_bytes = bytes(input_1,'utf-8')
    input_2_bytes = bytes(input_2,'utf-8')
    AND_bytes = b''
    for byte in input_1_bytes:
        x = bytes([byte^input_2_bytes[index]])
        AND_bytes+=bytes([byte^input_2_bytes[index]])
        print(bytes([byte^input_2_bytes[index]]))
        
        index+=1

    

    count = 0
    for byte in AND_bytes:
        print(byte)
        temp = byte
        #print(temp)
        for i in range(7):
            if(temp&1!=0):
                count+=1
            temp>>1
            #print(temp)
        #print(count)    
    #print(count)



main()