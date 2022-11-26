a = 10

def check():
    global a
    a = 9
    print(a)

check()
print(a)