def unit_converter():
    print("Welcome to the Unit converter, which conversion would you like to do?: ")
    print("1: Kilometers to miles")
    print("2: Miles to Kilometers")
    print("3: Celsius to Fahrenheight")
    print("4: Fahrenheight to Celsius")
    print("5: Mph to Kph")
    print("6: Kph to Mph")

    choice = int(input("\nPlease Select the conversion you would like to do: "))

    if choice == 1:
        kilometers = float(input("Please enter the kilometer amount: "))
        miles = kilometers * 0.621371
        print(f"{kilometers} Kilometers is equal to {miles:.2f} Miles.")
    elif choice == 2:
        miles = float(input("Please enter the amount of miles: "))
        kilometers = miles * 0.621371
        print(f"{miles} Miles is equal to {kilometers} Kilometers.")
    elif choice == 3:
        celsius = float(input("Please enter the celsius value: "))
        fahrenheight = (celsius * 9/5) + 32 
        print(f"{celsius} celsius is equal to about {fahrenheight} fahrenheight")
    elif choice == 4:
        fahrenheight = float(input("Please enter the fahrenheight value: "))
        celsius = (fahrenheight - 32) * 5/9
        print(f"{fahrenheight} fahrenheight is equal to {celsius} celsius")
    elif choice == 5:
        mph = float(input("Please enter the speed in mph: "))
        kph = mph * 1.60934
        print(f"{mph} mph is equal to {kph} kph")
    elif choice == 6:
        kph = float(input("Please enter a speed in kph: "))
        mph = kph * 0.621371
        print(f"{kph} Kph is equal to {mph} Mph.")

def main():
    while True:
        unit_converter()
        convert_another = input("Would you like to convert something else? y/n: ")
        if convert_another != "y":
            print("Goodbye")
            break

main()



