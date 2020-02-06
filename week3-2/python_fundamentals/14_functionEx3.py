def student():
    what = 'Question'
    print(what)
    global question
    question = input('Please type your question: ')
    print('\n')    
    return question, teacher()
    
def teacher():
    what = 'Answer'
    print(what)
    global question
    print('Question:',question)
    global answer
    answer = input('Please type the answer of the question: ')
    return answer

student()
print('\n')
print('Answer:',answer)






