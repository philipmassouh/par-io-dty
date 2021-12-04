n = input("Please enter an integer: ")
while (not n.isdigit()) and not (n[0] == '-' and (n := n[1:]).isdigit()):
    n = input(f"You entered {n}, that is not an integer you imbecile! Try again: ")
print(f"{n} is {('even', 'odd')[(int(n) % 2)]}!")

