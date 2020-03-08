def quantity_consumed():
    power_rating = float(input("Enter the Power Rating of your appliance: "))
    hour = int(input("Enter the number of hours the appliance has been used; between 1-24:"))
    if hour>0 and hour<=24:
        watts = power_rating*hour
        kilowatt_per_hour = watts/1000
        print('The electricity consumed by your appliance is {}kWh'.format(kilowatt_per_hour))
    else:
        print('The hour you entered is invalid')
        
def charges():
    units = float(input("Enter units consumed: "))
    charge = 0

    if units >0 and units <= 50:
        charge = units* 0.307780
        print('For {}kWh consumed, \nYour charge is {}GHC'.format(units,charge))

    elif units >51 and units <= 300:
        charge = 15.389 +(units - 50)* 0.617488
        print('For {}kWh consumed, \nYour charge is {}GHC'.format(units,charge))
    
    elif units>301 and units <= 600:
        charge = 15.389 + 30.8744 + (units - 300)* 0.801380
        print('For {}kWh consumed, \nYour charge is {}GHC'.format(units,charge))
    else:
        charge=15.389 + 30.8744 + 40.069 +(units - 600)* 0.890422
        print('For {}kWh consumed, \nYour charge is {}GHC'.format(units,charge))

        
print(quantity_consumed())
print(charges())


    
