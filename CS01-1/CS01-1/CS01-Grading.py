a = int(input("รับค่าคะแนนเก็บ:"))
if (a<0 or a>30):
    print("invalid score")
    quit()
b = int(input("รับค่าคะแนนสอบกลางภาค:"))
if (b<0 or b>30):
    print("invalid score")
    quit()
c = int(input("รับค่าคะแนนสอบปลายภาค:"))
if (c<0 or c>40):
    print("invalid score")
    quit()
grade = a+b+c
if (grade>=80 and grade<=100):
    print("A")
elif (grade>=75 and grade<=79):
    print("B+")
elif (grade>=70 and grade<=74):
    print("B")
elif (grade>=65 and grade<=69):
    print("C+")
elif (grade>=60 and grade<=64):
    print("C")
elif (grade>=55 and grade<=59):
    print("D+")
elif (grade>=50 and grade<=54):
    print("D")
elif (grade>=0 and grade<=49):
    print("F")