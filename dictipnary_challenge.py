words_dic={
    "Apple":'Fruit,can be eaten',
    "Car":'A vehicle that can be driven',
    "Shoe":'Leather material that can be worn for the feet'
}

long_word=''
short_word=''
long_length=0
short_length=float('inf')

for word in words_dic:
    meaning_length=len(words_dic[word])
    if meaning_length>long_length:
        long_word=word
        long_length=meaning_length
    if meaning_length<short_length:
        short_word=word
        short_length=meaning_length

print(f"The longest meaning is '{words_dic[long_word]} (Word:{long_word})' with length {long_length}")
print(f"The shortest meaning is '{words_dic[short_word]} (Word:{short_word})' with length {short_length}")