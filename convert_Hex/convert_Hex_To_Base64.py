import base64

#converts a hex string into a base64 string and prints it to output

message_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

message = message_input.upper()
message_bytes = message.encode('ascii') #Now I have a raw bitstring
print(message_bytes)
base64_bytes = base64.b16decode(message_bytes)
base64_message=base64.b64encode(base64_bytes)



print(base64_message)
