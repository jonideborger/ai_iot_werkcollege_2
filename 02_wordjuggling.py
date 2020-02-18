sentence = "an exercise about nothing but lists"

def return_the_first_and_last_word(sentence):
    return [ sentence[0], sentence[-1] ]

def sort_list(sentence):
    sentence.sort()
    return sentence

def split_sentence(sentence):
    return sentence.split()

sentence = split_sentence(sentence)
sentence = sort_list(sentence)
sentence = return_the_first_and_last_word(sentence)

print(sentence)
#['about', 'nothing']
