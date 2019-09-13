def word_flipper(our_string):
    words = our_string.split(" ")
    for i in range(len(words)):
        words[i] = words[i][::-1]

    return " ".join(words)


print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
