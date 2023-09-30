import random

luckynumber=random.randint(1,20)
print(luckynumber)

match luckynumber:
    case 1:
        print("chinese")
    case 2:
        print("mexican")
    case 3:
        print("greek")
    case 4:
        print("ethiopian")
    case 5:
        print("vegan")
    case 6:
        print("indian")
    case 7:
        print("seafood")
    case 8:
        print("american")
    case 9:
        print("thai")
    case 10:
        print("pizza")
    case 11:
        print("subs")
    case 12:
        print("japanese")
    case 13:
        print("bbq")
    case 14:
        print("ramen")
    case 15:
        print("vietnamese")
    case 16:
        print("buffet")
    case 17:
        print("brazillian")
    case 18:
        print("cuban")
    case 19:
        print("jamaican")
    case 20:
        print("pub")
    case _:
        print("jacked")
