mark=int(input("Enter your mark: "))
if(mark<=35):
    print("poor student")
elif(mark>=35 and mark<=70):
    print("average student")
elif(mark>70):
    print("good student")
else:
    print("invalid input")