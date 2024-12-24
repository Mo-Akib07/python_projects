print("Welcome To Love Calculater")
name1 = input("Enter Your Name : ")
name2 = input("What is Their Name : ")
love_name = name1 + name2
love_name.lower()
t = love_name.count("t")
r = love_name.count("r")
u = love_name.count("u")
e = love_name.count("e")
l = love_name.count("l")
o = love_name.count("o")
v = love_name.count("v")
e = love_name.count("e")

addTrue = str(t + r + u + e)
addLove = str(l + o + v + e)
total = addTrue + addLove
loveScore = int(total)
if loveScore < 10 or loveScore > 90:
    print(f"Your Love Score is {loveScore}, You go together like Coke and Mentos.")
elif loveScore > 40 and loveScore < 50:
    print(f"Your Love Score is {loveScore}, You are alright together.")
else:
    print(f"Your Score is {loveScore}")


