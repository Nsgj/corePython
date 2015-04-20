def myTrip(s):
    i = 0
    j = -1
    while True:
        if s[i] == " ":
            i += 1
        else:
            break
    while True:
        if s[j] == " ":
            j -= 1
        else:
            break
    rl = len(s) + j + 1
    ns = s[i:rl]
    return ns

s = raw_input("Enter a string")
print myTrip(s)
 
