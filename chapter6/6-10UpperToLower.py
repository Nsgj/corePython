def Return():
    s = raw_input('Enter a s: ')
    i = 0
    s1 = ''
    leng = len(s)
    while i < leng:
        if s[i] == s[i].lower():
            s1 += s[i].upper()
        else:
            s1 += s[i].lower()
        i += 1
        
    return  s1

if __name__ == '__main__':
    
    print  Return()

