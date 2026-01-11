marks1 = int(input("Enter subject1 marks: "))
marks2 = int(input("Enter subject2 marks: "))
marks3 = int(input("Enter subject3 marks: "))

total_marks = (100*(marks1+marks2+marks3))/300
if(total_marks>40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("student has cleared all subject with ",total_marks)
else:
    print("student is failed ",total_marks)