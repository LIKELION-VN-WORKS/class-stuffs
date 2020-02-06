#0 format

# def function_name (parameter1, parameter2): 
#     function processing
#     ...
#     return 

# function_name(argument1, argument2) # call the function with input value

# def function():
#     function processing
#     ...
#     return

# function() # call the function without input value.

#1 매개변수, 인자(값 리턴) : function that has a return value.(return the values)

def lionQueen(name,age):
    return name,age

a,b = lionQueen("queen", 25)
print(a)
print(b)

#2 매개변수, 인자(콘솔에 출력) : parameters, arguments(print to the console)

def lionKing(name,age):
    print(name,age)

lionKing("king", 22)



# 자바스크립트 -> 파이썬 : https://github.com/aimclee/javascript-2019-/tree/master/advanced_javascript