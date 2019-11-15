#Norma
#InfiniteFor.py
#extra credit
import itertools

def infinite():
    count =0
    for i in itertools.count():
        count = count +1
        print(count)
    return count



def main():
    infinite()
    print(infinite())

main()