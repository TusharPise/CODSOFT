a = float(input("first number: "))
b = float(input("second number: "))

print("1 for add")
print("2 for subtract")
print("3 for multiply")
print("4 for divide")

ch = input("pick one: ")

if ch == "1":
    ans = a + b
    print("answer =", ans)

elif ch == "2":
    ans = a - b
    print("answer =", ans)

elif ch == "3":
    ans = a * b
    print("answer =", ans)

elif ch == "4":
    if b == 0:
        print("can't divide by 0")
    else:
        ans = a / b
        print("answer =", ans)

else:
    print("wrong choice")