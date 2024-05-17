def bmi_calculator(weight, height):
    bmi=float(weight/(height*height))
    return bmi

def bmi_classifier(bmi):
    if bmi<18.5:
        return "underweight"
    elif bmi<25:
        return "healthy weight"
    elif bmi<30:
        return "overweight"
    else:
        return "obese"

def main():
    weight=float(input("enter your weight in kg: "))
    height=float(input("enter your height in m: "))

    if weight<=0 or height<=0:
        print("Invalid input")
    else:
        bmi=bmi_calculator(weight, height)
        result=bmi_classifier(bmi)
        print("BMI is: ",bmi)
        print("Result: ",result)

if __name__=="__main__":
    main()
