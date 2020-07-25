'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #if there's less than the count of the substring ("th") left
    if len(word) < 2:
        return 0
    #match, pass in everything from the next character on and increment the count by 1
    if word[0 : 2] == "th":
        return count_th(word[1:]) + 1
    #no match, pass in everything from the next character on
    return count_th(word[1:])