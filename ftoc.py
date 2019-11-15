#Norma
#ftoc.py

def f2c(fahr):
    c = (fahr-32.0)*(5/9)
    celsius = round(c, 2)
    return celsius

def main():
    fahr = float(input("Temperature in F degrees: "))
    f2c(fahr)
    answer = f2c(fahr)
    print("Degrees in Celsius: ", answer)

main()