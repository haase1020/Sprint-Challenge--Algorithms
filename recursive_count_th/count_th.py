'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    th_string = 'th'
    # base case
    if len(word) < 2:
        return 0

    if th_string == word[0:2]:
        print(word)
        return 1 + count_th(word[2:])
    else:
        print(word)
        return count_th(word[1:])


print(count_th('the theater was thoroughly thronging with thistles'))
