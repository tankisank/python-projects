    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cond=True
cond1=True
cond2=True
def encrypt(shift,text):
    newword=""
    for i in text:
        newword+=alphabet[alphabet.index(i)+shift]
    print(newword)
def decrypt(shift,text):
    newword = ""
    for i in text:
        newword += alphabet[alphabet.index(i) - shift]
    print(newword)
while cond==True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if (direction == 'encode'):
        while cond1==True:
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            encrypt(shift, text)
            x = input("do you want to continue to encrypt? y/n")
            if (x == 'y'):
                cond1 = True
            else:
                cond1 = False
    if (direction == 'decode'):
        while cond2==True:
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            decrypt(shift, text)
            x = input("do you want to continue to decrypt? y/n")
            if (x == 'y'):
                cond2 = True
            else:
                cond2 = False
    z=input("do you want to continue to encrypt or decrypt y/n")
    if(z=='y'):
        cond==True
    else:
        cond=False






