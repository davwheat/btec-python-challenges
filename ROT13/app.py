import codecs

option = input("Press 1 to decode or 2 to encode by ROT13.")

if option == "1":
    text = input("Enter text to encode with ROT13: ")
    print(codecs.encode(text, "rot_13"))
elif option == "2":
    text = input("Enter text to decode from ROT13: ")
    print(codecs.decode(text, "rot_13"))
