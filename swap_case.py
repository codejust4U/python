"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""



def swap_case(s):
    result = []
    for letter in s:
        if letter == letter.lower():
            result.append(letter.upper())
        elif letter == letter.upper():
            result.append(letter.lower())
        else:
            result.append(letter)
            
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
