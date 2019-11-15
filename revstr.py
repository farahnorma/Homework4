#Norma
#revstr.py

def reverse(s):
    reversed = ''
    for char in s:
        reversed = char + reversed
    return reversed

def main():
    s = str(input("Input your string here: "))
    answer= reverse(s)
    print("Your string reversed is: ", answer)

main()