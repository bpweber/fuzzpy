import os
import sys
import re

def rate(str1, str2):
    rating = 1
    restring = ''
    for char in str2:
        if char in str1:
            restring += f'{char}.*' if not re.match('[\.\*\/]', char) else 'f\{char}'
            rating *= 2
    if re.search(restring, str1):
        rating *= 4
    if str2 in str1:
        rating *= rating
    rating *= 1 + (len(str2) / len(str1))
    return round(rating)
    
if __name__ == '__main__':
    os.system('clear')
    last_path = ''
    while True:
        path = os.getcwd()
        search_t = input() 
        os.system('clear')
        if not search_t:
            if os.path.isdir(last_path):
                os.system('clear')
                print(last_path)
            else:
                os.system(f'nvim {last_path}')
            exit()
        rlist = []
        dlist = []
        flist = []
        for r, d, f in os.walk(path):
            for n in f:
                flist.append(os.path.join(r, n))
            for n in d:
                dlist.append(os.path.join(r, n))
        for n in flist:
            rlist.append([rate(n, search_t), n])
        for n in dlist:
            rlist.append([rate(n, search_t), n])
        rlist = sorted(rlist, reverse=False)
        for i in range(10, 0, -1):
            print(rlist[-i])
        last_path = rlist[-1][1]

