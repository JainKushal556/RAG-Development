# Created a utility for counting word character words frequency of a string  or sentece 

def count_words(sentence):
    words_list = sentence.split()
    words_count = len(words_list)
    return words_count 

def count_characters(sentence):
    characters_count = len(sentence)
    return characters_count

def count_lines(sentence):
    lines_count = sentence.count('\n')
    return lines_count

def count_frequency(sentence):
    words=[]
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        word_count = words.count(word)
        if frequency.get(word) != None:
            continue
        else:
            frequency[word] = word_count
    return frequency

# def clean_text(sentence=""):
#     sentence = sentence.strip().lower()
#     return sentence

print("Utility Program Executed")


# print(count_words("My Name Is Kushal Jain"))
# print(count_characters("Kushal Jain"))
# sentence = input()
# print(count_lines(sentence))