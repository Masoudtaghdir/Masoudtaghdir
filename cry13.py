def rot13(text):
    trans = text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" , "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
    text = text.translate(trans)
    return text

while True :    
    text = input("text : ")
    text = rot13(text)
    print(text)