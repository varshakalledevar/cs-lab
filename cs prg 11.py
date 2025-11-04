import base64
my_string="Hello,World!"
encode3d_string=base64.b64encode(my_string.encode("utf-8"))
print("encode string:",encode_string)
my_string="SGVabGBsTFdvcmxIQ=="
decode_string=bas64.b64decode(my_string)
print("decoded string:",decoded_string.decode("utf-8"))