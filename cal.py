cal_oper='''
+ add
- subtract
* multiplication
/ divide
'''
print(cal_oper)

num1=int(input('enter 1st number:- '))
op=input('enter oparation:-')
num2=int(input('enter 2nd number:- '))

if op=='+':
    print(f'your answer is:= {num1+ num2}')
elif op=='-':
    print(f'your answer is"= {num1- num2}')
elif op=='*':
    print(f'your answer is:= {num1* num2}')
elif op=='/':
    print(f'your answer is:= {num1*num2}')

else:
    print('something wrong')




