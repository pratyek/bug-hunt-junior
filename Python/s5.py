# Program: How are you doing?

answer1 = input("Are you enjoying Vashisht? ([Y]es/[N]o) ")
if answer1.lower() in ["y", "yes"]:
    print("That's great! We hope you're having fun hunting for bugs.")
elif answer1.lower() in ["n", "no"]:
    print(":( We're sorry to hear that. We hope you'll have fun soon.")
else:
    print("404 Not Found!")

print()

answer2 = input("Do you want me to print bugs for all Python files? ;) ([Y]es/[N]o) ")
if answer2.lower() in ["y", "yes"]:
    print("Nice try :P")
elif answer2.lower() in ["n", "no"]:
    print("That's the spirit!")
else:
    print("404 Not Found!")
