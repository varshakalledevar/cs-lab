def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char)+s -65)%26+65)
        else:
            result += chr((ord(char)+s -97)%26+97)
    return result
text=input("enter the text.txt:")
s=int(input("enter the shift between 1 to 25:"))
print("text.txt:"+text)
print("shift:"+str(s))
print("cipher:"+encrypt(text,s))