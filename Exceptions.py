filename = "Leason_List.txt"

try:
    print("Inside TRY")
    myfile = open(filename, mode='r', encoding='utf_8')
except Exception:
    print("Inside EXCEPT")
    print("Error Found")
else:
    print("Inside ELSE")
    print(myfile.read())
finally:
    print("Inside FINALLY")