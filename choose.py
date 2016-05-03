# coding: utf-8

import pathlib
import os


def main():
    d = {i:f.name for i, f in enumerate(pathlib.Path('.').glob('*.bat'), start=1)}
    maxl = max([len(x) for x in d.values()])
    print('\n\n')
    for i, f in d.items():
        print('\t\t[{}]--->{:>{}}*'.format(i, f, maxl))
    while 1:
        num = input('Choose a way to run a file:\n\tFilename: like "python" or "python.bat"\n\tIndex: like a number of pre in "1"\n\t[Q]uit: quit command\nChoose a way of above>>>:')
        num = num.lower()
        if num == 'q' or num == 'quit':
            print('GoodBye')
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
                print('Not Found. choose another file')

    print('You are choose running "{}"'.format(file), 'Please waiting...')
    os.system('call '+file)


if __name__ == '__main__':
    main()
    # os.system('pause')

