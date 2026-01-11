p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe now"
p4 = "click this"

message = input("Enter your message ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("Alert this is a spam message")
else:
    print("you are safe")

# in keyword is use to check the existence in the string if exist then it will return true otherwise it will return false