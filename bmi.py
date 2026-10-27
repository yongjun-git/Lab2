def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)
    if bmi <18.5:
        print("Under Weight")
    elif bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")
    
    print (f"Your BMI is {bmi}")
    

calculate_bmi(weight=57, height=1.73)

calculate_bmi(weight=50, height=1.73)   # BMI ≈ 16.7 → Under Weight

calculate_bmi(weight=57, height=1.73)   # BMI ≈ 19.0 → Normal Weight

calculate_bmi(weight=80, height=1.73)   # BMI ≈ 26.7 → Over Weight

    