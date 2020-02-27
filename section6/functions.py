def say_hello(name='NAME'):
    '''
    DOCSTRING: Information about the function
    INPUT: no input
    OUTPUT: Hello
    '''
    return 'Hello, ' + name


who = say_hello('Zohaib')
print(who)


def add(n1, n2):
    return n1+n2


cal = (add(10, 20))
print(cal)

# Find out if the word 'dog' is in a string


def dog_check(mystring):
    return 'dog' in mystring.lower()


print(dog_check('Dog ran away'))
print(dog_check('My cat ran away'))

# pig latin


def pig_latin(word):
    first_letter = word[0]
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        # from index 1 all the way to the end
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word


print(pig_latin('word'))
print(pig_latin('apple'))
