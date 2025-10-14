import rsa
def rsa_algo(password):
    publickey,privatekey=rsa.newkeys(512)
    print("public key:",publickey)
    print("private key:",privatekey)
    message=password.encode('utf -8')
    cipertext=rsa.encrypt(message,publickey)
    print("ciper text",cipertext)
    decrypted_message=rsa.decrypt(cipertext,privatekey)
    print("decrypted message",decrypted_message.decode('utf-8'))
password=input("input your text")
rsa_algo(password)