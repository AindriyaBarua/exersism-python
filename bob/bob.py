def hey(string):
    if string.isupper():
        return 'Whoa, chill out!'
    elif string.rstrip().endswith('?'):
            return 'Sure.'
    elif string.isspace() or not string:
            return 'Fine. Be that way!'
    else:
        return 'Whatever.'





