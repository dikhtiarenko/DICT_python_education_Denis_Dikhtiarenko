bot_name = "DICT_Bot"
birth_year = 2026
print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")
print("Please, remind me your name.")

your_name = input("> ")
print(f"What a great name you have, {your_name}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

rem3 = int(input(">"))
rem5 = int(input(">"))
rem7 = int(input(">"))
age = sum([rem3 * 70, rem5 * 21, rem7 * 15]) % 105
print(f"Your age is {age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
count_to = int(input("> "))

for i in range(sum([count_to, 1])):
    print(f"{i}!")
print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

while True:
    answer = int(input("> "))
    if answer ==2:
        break
    print("Please, try again.")

print("Congratulations, have a nice day!")