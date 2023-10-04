import math
import re

def is_a_triple(n):
    return (n % 3) == 0;
    """Return True if n is a multiple of 3; False otherwise."""

    

def is_prime(num):
    if num > 1:

        for i in range (2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def last_prime(m):
    if is_prime(m) == True:
        return m
    else:
        return last_prime(m-1)
    """Return the largest prime number p that is less than or equal to m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""



def quadratic_roots(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)

    if discriminant < 0:
        return "complex"
    
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    return (root1, root2)

    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""

def new_quadratic_function(a, b, c):
    return lambda x: (a * x ** 2) + (b * x) + c
    """Create and return a new, anonymous function (for example
    using a lambda expression) that takes one argument x and 
    returns the value of ax^2 + bx + c."""
#quad = new_quadratic_function(1, -3, 2)
#print(quad(0))

def perfect_shuffle(even_list):
    shuffled_list = []

    first_half = even_list[ :len(even_list) // 2]
    second_half = even_list[len(even_list) // 2:]

    for i in range(len(first_half)):
        shuffled_list.append(first_half[i])
        shuffled_list.append(second_half[i])
    
    return shuffled_list
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    Perfect shuffle means splitting a list into two halves and then interleaving
    them. For example, the perfect shuffle of [0, 1, 2, 3, 4, 5, 6, 7] is
    [0, 4, 1, 5, 2, 6, 3, 7]."""
#print(perfect_shuffle([10,20,30,40,50,60]))

def list_of_3_times_elts_plus_1(input_list):
    return [ (n * 3) + 1 for n in input_list ]
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 3 and had 1 added to it."""
#print(list_of_3_times_elts_plus_1([1,1,1,1]))


def triple_vowels(text):
    vowels = "aeiouAEIOU"
    new_text = ""

    for char in text:
        if char in vowels:
            new_text = new_text + char * 3
        else:
            new_text += char
    return new_text

    """Return a new version of text, with all the vowels tripled.
    For example:  "The *BIG BAD* wolf!" => "Theee "BIIIG BAAAD* wooolf!".
    For this exercise assume the vowels are
    the characters A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""
#print(triple_vowels("The *BIG BAD* wolf!"))

def count_words(text):
    num_words = dict()
    words = re.findall(r"[a-zA-Z0-9\-+*/@#%'']+", text)
    words = [words.lower() for words in words]

    for word in words:
        if word in num_words:
            num_words[word] += 1
        else:
            num_words[word] = 1
    return num_words

    """Return a dictionary having the words in the text as keys,
    and the numbers of occurrences of the words as values.
    Assume a word is a substring of letters and digits and the characters
    '-', '+', *', '/', '@', '#', '%', and "'" separated by whitespace,
    newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ] { } | : ).
    Convert all the letters to lower-case before the counting."""

#print(count_words("abc-%'. ' fox"))

