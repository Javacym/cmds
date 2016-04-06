# coding: utf-8

import pathlib
import os

def main():
    d = {i:f.name for i, f in enumerate(pathlib.Path('.').glob('*.bat'), start=1)}
    maxl = max([len(x) for x in d.values()])
    print('**********Call of Command**********')
    for i, f in d.items():
        print('**********[{}]--->{:>{}}*'.format(i, f, maxl))
    while 1:
        num = input('Choose a file to run\n\tfilename: like python or python.bat\n\tnumber: like a number of pre in [1]\n\t[Q]uit: quit)\n\tchoose a way of above>>>:')
        if num.lower() == 'q' or num.lower() == 'quit':
            print('GooBye')
            return
        try:
            file = d.get(int(num))
            break
        except Exception:
            num = num if num.endswith('.bat') else num +'.bat'
            if num in d.values():
                file = num
                break
            else:
                print('Not Found. choose right file')
    print('You are choose running "{}"'.format(file))
    os.system('call '+file)


if __name__ == '__main__':
    main()
    os.system('pause')

