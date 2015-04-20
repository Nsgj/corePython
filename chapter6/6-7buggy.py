number_str = raw_input('Enter a number ')
num_num = int(number_str)

fac_list = range(1,num_num+1)
print "BEFORE:",fac_list

i = 0

while i < len(fac_list):
    print len(fac_list)
    if num_num % fac_list[i] == 0:
       print fac_list[i]
       del fac_list[i]
       i = 0
       continue

    i = i+1

print "AFTER",fac_list
#去除自己的yue数
