"""
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
"""


from string import ascii_lowercase as alc
def print_rangoli(size):
    #exception case, normal method would give '-a-'
    if size == 1: 
        print(alc[0])
        return
    
    alphaSlice = [*alc[:size]]
    rangoli = []
    
    #iterate through alphabet, get progressive smaller chunks, insert to list
    for i in range(size):
        # isolate center letter for easy padding
        center = alphaSlice[i]
        halfLine = '-'.join([y for y in alphaSlice[i+1:]])
        line = halfLine[::-1]+f'-{center}-'+halfLine
        rangoli.append(line)
        
    # every line will have the same width as the longest line
    padding = len(rangoli[0])
    #duplicate and mirror list
    mirrorRangoli = [*rangoli[::-1],*rangoli[1:]]
    
    for line in mirrorRangoli:
        print(line.center(padding, '-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
