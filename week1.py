
#print("Hello world2!")

#print("hello, " "Aurélien!", "How are you?")

#print(1,"plus", 2, "equals", 1+2)

#name = input("Give me your name: Jarkko")
#print("Hello,", name)



def triple(q):
    #print("I have been called with argument", q )
    q *= 3   # q = q * 3
    #print("I will return", q)
    return q

def square(s):

    s = s **2
    return s



for x in range(1,11):

    r = triple(x)
    r2 = square(x)

    #print('triple(', x,')==', r, 'square(', x, ')==', r2)
    # to_show = f'triple({x})=={r} square({x})=={r2}'
    print(f'triple({x})=={r} square({x})=={r2}')
    # print('The square of ', x, 'is', r2)


    #y = triple(x)


    # y as string
    #print("y", y)


    # x=7
    # x *= 3
    # print("x", x)
