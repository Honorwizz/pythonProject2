inputfile = "../user_names.txt"
outputfile = "../user_names2.txt"

myfile = open(inputfile, mode='r', encoding='utf_8')
myfile2 = open(outputfile, mode='a', encoding='utf_8')
for num, line in enumerate(myfile, 1):
    print("Line №: " + str(num)+ " : " + line.strip())
    myfile2.write("Found password: " + line)


myfile.close()
myfile2.close()