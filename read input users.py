
message = ""

while True:
    message = input("ENter password")
    if message == 'secret': break
    print(message + "Password Not Correct")

print("Password was:" + message)
