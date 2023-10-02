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
days = "Friday"
match days:
    case "Monday":
        print("Today is Monday!")
    case "Tuesday":
        print("Today is Tuesday!")
    case "Wednesday":
        print("Today is Wednesday!")
    case "Thursday":
        print("Today is Thursday!")
    case "Friday":
        print("Today is Friday!")
    case "Saturaday":
        print("Today is Saturaday!")
    case "Sunday":
        print("Today is Sunday!")
    case _:
        print("Wrong")