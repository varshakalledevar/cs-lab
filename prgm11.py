import base64
my_string="BCA"
encoded_string=base64.b64encode(my_string.encode("utf-8"))
print("encode string:",encoded_string)
my_string="QkNB"
decoded_string=base64.b64decode(my_string)
print("decoded string:",decoded_string.decode("utf-8"))