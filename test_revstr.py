#Norma
#test_revstr.py

def reverse(s):
    reversed = ''
    for char in s:
        reversed = char + reversed
    return reversed

# def main():
#     s = str(input("Input your string here: "))
#     answer= reverse(s)
#     print("Your string reversed is: ", answer)
#
# main()


def test_1():
    assert reverse('1.0')=='0.1'

def test_2():
    assert reverse('apples and oranges')=='segnaro dna selppa'

def test_3():
    assert reverse('?/!') == '!/?'

def test_3():
    assert reverse('hElL0!')=='!0LlEh'

def test_4():
    assert reverse('1')=='1'

def test_5():
    assert reverse('reverse')=='esrever'

def test_6():
    assert  reverse('8 oclock')=='kcolco 8'

def test_7():
    assert reverse('   ') == '   '

def test_8():
    assert reverse('¯\_( ಠ_ಠ)_/¯') == '¯/_)ಠ_ಠ (_\¯'

def test_9():
    assert reverse('string')=='gnirts'

def test_10():
    assert reverse('fini')=='inif'