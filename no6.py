a = []
def sortStringByChar(myData) :
    for x in myData :
        c = x
        a.append(c)
    a.sort()
    a.reverse()
    print(a)
myData=['nanas','pisang','jambu','mangga']
sortStringByChar(myData)
