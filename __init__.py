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
    rlist = []
    while True:
        try:
            path = os.getcwd()
            search_t = input() 
            os.system('clear')
            if not search_t:
                os.system(f'nvim {last_path}')
                exit()
            elif search_t.isdigit():
                os.system(f'nvim {rlist[int(search_t)][1]}')
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
            rlist = sorted(rlist, reverse=True)
            for i in range(9, -1, -1):
                if i == 0: 
                    print(f'--> {rlist[i][1]}')
                else:
                    print(f'[{i}] {rlist[i][1]}')
            last_path = rlist[0][1]
        except KeyboardInterrupt:
            exit()

