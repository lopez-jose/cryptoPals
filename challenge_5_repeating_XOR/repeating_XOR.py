
def main():
    input = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    key = "ICE"
    count = 0
    output = ""
    for i in input:
        #print (i)
        xor = i^key[count]
        output+=xor
        if(count == 2):
            count = 0
    print(output)



main()