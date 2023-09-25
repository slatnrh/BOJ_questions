T = int(input())

for _ in range(T):
    money = int(input())
    C = {"Quarter" : 0, "Dime" : 0, "Nickel" : 0, "Penny" : 0}
    C["Quarter"] = money // 25
    money %= 25
    C["Dime"] = money // 10
    money %= 10
    C["Nickel"] = money // 5
    money %= 5
    C["Penny"] = money

    print(C["Quarter"], C["Dime"], C["Nickel"], C["Penny"])