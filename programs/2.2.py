#program to print name given by user and also how many times it should be repeated

name=input('enter ur name')
n=int(input('how many times do you want to print'))
for n in range(1,n+1):
    print("{}\n".format(name))
