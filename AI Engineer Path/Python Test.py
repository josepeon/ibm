message_to_solve = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
abc = 'abcdefghijklmnopqrstuvwxyz'
shift = 16

decoded_message = ""

for word in message_to_solve.split():
    for letter in word:
        if letter in abc:
            index = abc.index(letter)
            new_index = (index - shift) % 26
            decoded_letter = abc[new_index]
            decoded_message += decoded_letter
        else:
            decoded_message += letter
    decoded_message += " "

print(decoded_message)

message_to_encode = "dale pa la pinga maricona"
abc = 'abcdefghijklmnopqrstuvwxyz'
shift = 16

encoded_message = ""

for word in message_to_encode.split():
    for letter in word:
        if letter in abc:
            index = abc.index(letter)
            new_index = (index + shift) % 26
            encoded_letter = abc[new_index]
            encoded_message += encoded_letter
        else:
            encoded_message += letter
    encoded_message += " "

print(encoded_message)