name = input("ENTER YOUR NAME " )
ssc_gpa = float(input("ENTER YOUR SSC GPA "))
hsc_gpa = float(input("ENTER YOUR HSC GPA "))
admission_score = int(input("ENTER YOUR ADMISSION SCORE "))

if(ssc_gpa >=4.00 and hsc_gpa >= 4.00):
    if(admission_score>=75):
        print(f"{name} was eligible to admited.")
        
else:        
    print(f"{name} was not eligible to admited.")

