lis = []

while True:
    s =  raw_input("Enter a number: ")
  
    if(s == 'done'):
        break
    lis.append(int(s))

lis.sort(reverse = True)
print lis
