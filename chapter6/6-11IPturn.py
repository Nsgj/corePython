def inputIP():
    s = raw_input('Enter a IP')
    lis = s.split('.')
    for i in lis:
        print int(i)


if __name__ == '__main__':

    inputIP()
