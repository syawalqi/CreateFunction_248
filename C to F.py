def Conversion():
    unit = input("Masukan unit suhu ('Celcius' / 'Farenheit') :")
    suhu = float(input("masukan suhu :"))
    
    if unit.upper() == 'CELCIUS':
        fahrenheit = (suhu * 9/5) + 32
        return fahrenheit
    elif unit.upper() == 'FARENHEIT':
        Celcius = (suhu - 32) * 5/9
        return Celcius
    else:
        print("unit tidak valid")

print(Conversion())
