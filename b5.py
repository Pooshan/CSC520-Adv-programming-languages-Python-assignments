
a = list("abc")
b = list("lmn")

print ([x + y for x in a for y in b])


def check(*args, **keyargs):
    print(keyargs)
    print(args)

check([1,2,3],{'l':'abc'},k=9,i=8)

