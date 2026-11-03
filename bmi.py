def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)

    print(f"Your BMI is {bmi}") 

    
    if bmi <18.5:
        print("Under Weight")
        return -1
    elif bmi <= 25.0:
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1
    

def main():
    calculate_bmi(weight=50, height=1.73)
    calculate_bmi(weight=57, height=1.73)
    calculate_bmi(weight=80, height=1.73)

if __name__ == "__main__":
    main()

    