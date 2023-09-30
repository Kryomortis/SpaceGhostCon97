
import random
luckynumber =random.randint(1,20)
print("Your lucky number is",luckynumber)
match luckynumber:
    case 1:
        print("Let's go get some Chinese")
    case 2:
        print("Let's go get some Mexican")
    case 3:
        print("Let's go get some Greek")
    case 4:
        print("Let's go get something Heathy")
    case 5:
        print("Let's go get some Indian")
    case 6:
        print("Let's go get some Seafood")
    case 7:
        print("Let's go get some American")
    case 8:
        print("Let's go get some Thai")
    case 9:
        print("Let's go get some Pizza")
    case 10:
        print("Let's go get some Subs")
    case 11:
        print("Let's go get some Japanase")
    case 12:
        print("Let's go get some BBQ")
    case 13:
        print("Let's go get some Ramen")
    case 14:
        print("Let's go get some Vietnamese")
    case 15:
        print("Let's go get some Buffet")
    case 16:
        print("Let's go get some Brazilian")
    case 17:
        print("Let's go get some Cuban")
    case 18:
        print("Let's go get some Jamaican")
    case 19:
        print("Let's go get some Ethiopian")
    case 20:
        print("Let's go get some Pub")
    case _:
        print("Let's go get some Soul Food")

