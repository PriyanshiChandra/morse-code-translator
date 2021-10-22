MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(msg):
    encrypt_msg=''
    for letter in msg:
        if letter!=' ':
            encrypt_msg+=MORSE_CODE_DICT[letter.upper()]+" "
        else:
            encrypt_msg+=" "
    
    return encrypt_msg

def decrypt(msg):
    decrypt_msg=""
    temp=""
    # spaces=0
    for letter in msg:
        if letter !=" ":
            temp+=letter
        elif temp!="":
            i=0
            for k in MORSE_CODE_DICT.values():
                if k==temp:
                    decrypt_msg+=list(MORSE_CODE_DICT.keys())[i]
                    break
                else:
                    i+=1
            temp=""
        else:
            decrypt_msg+=" "
    return decrypt_msg





print("Please choose an option: ")
ch = input("Press 1 for English -> Morse Code"+"\n"+"Press 2 for Morse Code -> English"+"\n")
if ch=='1':
    message=input("Enter the message in English to display its Morse code: ")
    en_str=encrypt(message)
    print("\n"+en_str)

elif ch=='2':
    message=input("Enter the message in Morse Code to display its English: ")
    de_str=decrypt(message)
    print("\n"+de_str)


