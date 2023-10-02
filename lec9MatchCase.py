ip = int(input("Enter the value: "))
match ip:
    case 0 if ip <= 9:
        print("Whole numbers")
    case 1:
        print("Natural numbers")
    case 2 if ip % 2 == 0:
        print("ip % 2 == 0 than Enven number")
    case _:
        print("Not available")

# only match the case numbers otherwise it will excute default case 