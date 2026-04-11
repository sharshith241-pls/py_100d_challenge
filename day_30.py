# def factorial(num):
#     if (num ==1 or num ==0):
#         return 1
#     else:
#         return (num*factorial(num-1))
# num=1;
# print("Number:",num)
# print("Factorial:",factorial(num))
###################################################################################################
def fibonacci(num):
    
       if(num==0 or num ==1 ):
        return num
       else:
        return(fibonacci(num-1)+fibonacci(num-2))

num=7;
print("Number:",num)
print(fibonacci(num))
###################################################################################################
def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

num = int(input("Enter how many numbers: "))

print("Fibonacci sequence:")

for i in range(num):
    print(fibonacci(i), end=" ")
