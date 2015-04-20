def findchr(string,char):
    n = 0
    for i in string:
        if i == char:
            return n
        else:
            n += 1
    if n == len(string):
        return -1
def rfindchr(string,char):
    n = -1
    n1 = -len(string)
    while n > n1:
        if string[n] == char:
            return -n1 + n
        else:
            n -= 1
    if n == n1:
        return -1
def subchr(string,origchar,newchar):
    n = findchr(string,origchar)
    if n != -1:
        return string[:n] + newchar + string[n+1:]
if __name__ == '__main__':
    print findchr('ewqdaf','q')
    print rfindchr('ewqdaf','q')
    print subchr('ewqdaf','q','x') 
