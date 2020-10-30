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

    array = [12.02,9.10,8.12,7.68,7.31,6.95,6.28,6.02,5.92,4.32,3.98,2.88]
    array_hold=[]
    #E T A 0 I N S R H D L U 
    output_bytes=single_byte_XOR(input_bytes,char_value)
    
    sum_e = 0

    for i in range(0,len(output_bytes)):
        if(output_bytes[i]==101):
            #print(output_bytes[i])
            sum_e+=1
        

    expected_e=(sum_e/len(output_bytes))*100

   # print(expected_e)
    if(expected_e>4):
        if(expected_e<20):
            print(output_bytes)
    
    return   (array[0]-expected_e)



def main():

    input_1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    input_bytes= bytes.fromhex(input_1)
    get_score = 0
    smallest_score = 0

    for i in range(256):
        get_score=score(input_bytes,i)
        

        
        

    

    



main()