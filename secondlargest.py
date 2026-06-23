def secondlargest(a):
    l=float("-inf")
    sl=float("-inf")
    for i in range(len(a)):
        if l < a[i]:
            sl=l
            l=a[i]
        elif a[i]> sl and a[i]!=l:
            sl=a[i]
    return [sl]

op=[5,5,2,1,4,3,2,1]
print(secondlargest(op))