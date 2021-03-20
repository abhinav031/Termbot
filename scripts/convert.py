# Weight Converter

def convert():
    print("Welcome to weight converter!")
    weight = float(input("Enter weight (number only): "))
    unit = input("Enter unit to convert to [(K)g or (L)bs]: ")

    if unit.lower() == "k":         # convert to kilogram
        conv = weight / 2.205
        print(str(weight) + " Pounds is " + str(conv) + " Kilograms")
    elif unit.lower() == "l":       # convert to lbs
        conv = weight * 2.205
        print(str(weight) + " Kilograms is " + str(conv) + " Pounds")
