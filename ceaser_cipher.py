import string
import collections

def caeser(rotate_string, number):
	upper = collections.deque(string.ascii_uppercase)
	lower = collections.deque(string.ascii_lowercase)
	upper.rotate(number)
	lower.rotate(number)
	upper = ''.join(list(upper))
	lower = ''.join(list(lower))
    a = rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))
    return a


print(caeser("this is bad", 1))
