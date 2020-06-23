
#print("Hello world2!")

#print("hello, " "Aurélien!", "How are you?")

#print(1,"plus", 2, "equals", 1+2)

#name = input("Give me your name: Jarkko")
#print("Hello,", name)


import itertools

dice = [1,2,3,4,5,6]

def subsets(n, m):
    perms = itertools.combinations_with_replacement(dice, n)
    for i in perms:
        if sum(i) == m:
            yield i
        else:
         return

print(list(subsets(10,35)))



import itertools

dice = [1,2,3,4,5,6]

#10(n) is the number of dice throughting at once... 35(m) is the sum of the two dice facing up...

def subsets(2, 5):
    perms = itertools.combinations_with_replacement(dice, 2)
    for i in perms:
        if sum(i) == 5:
            yield i
        else:
            return

print(list(subsets(2, 5)))