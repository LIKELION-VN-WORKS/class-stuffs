#1
a = 10 # global variable

def function():
    a = 5 # local variable
    print(a)

function()
print(a)

#2
a = 10 # global variable

def function():
    global a # global variable
    print(a)

function()
print(a)

#3
i = 0 # global variable
def count():
    global i # convert i into global variable
    i += 1
    return i

for i in range (10): # Here, 'i' is a local variable. (i=0~9) 
    print(count())



