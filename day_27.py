# list=[]
# for temp in range()
# question1=input("Who was the first president of India: ")
# temp=list.append(question1)
# if (question1== "Rajendra"):
#     print("Your answer is correct ,You won 1000rs")
# print(list)
###################################################################################################
# Questions list: [question, options, correct answer, prize money]
# questions = [
#     ["Capital of India?", ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"], "B", 1000],
#     ["2 + 2 = ?", ["A. 3", "B. 4", "C. 5", "D. 6"], "B", 2000],
#     ["Color of sky?", ["A. Blue", "B. Green", "C. Red", "D. Yellow"], "A", 5000]
# ]

# money = 0

# print("Welcome to KBC Game\n")

# # Loop through questions
# for q in questions:
#     print(q[0])  # question

#     # print options
#     for opt in q[1]:
#         print(opt)

#     ans = input("Enter answer (A/B/C/D): ").upper()

#     # check answer
#     if ans == q[2]:
#         money = q[3]
#         print("Correct! You won ₹", money)
#         print()
#     else:
#         print("Wrong answer!")
#         break

# print("\nGame Over")
# print("You are taking home ₹", money)
###################################################################################################
question=[['what is ur name?',["A. HArsh", "B. Chetoon", "C. BAla", "D. Vishnu"],"A",1000],
          ['what is ur age?',['A.16','B.21','C.3','D.15'],"B",2000]]
money=0
print("Welcome to KBC Game\n")
for q in question:
    print(q[0])
    for opt in q[1]:
     print(opt)

    
    ans=input("Enter(A,B,C,D):").upper()

    if ans==q[2]:
            money=q[3]
            print("Correct answer,you won ",money)
            print()
    else:
            print("Wrong answer")
            break

print("Game Over")
print("Your are taking home ₹",money)