#Norma
#test_f2c.py

def f2c(fahr):
    c = (fahr-32.0)*(5/9)
    celsius = round(c, 2)
    return celsius


def test_1():
    assert f2c(32)==0


def test_2():
    assert f2c(1)==-17.22

def test_3():
    assert f2c(212)==100

def test_4():
    assert f2c(300)==148.89

def test_5():
    assert f2c(100) == 37.78

def test_6():
    assert f2c(80) == 26.67

def test_7():
    assert f2c(-10) == -23.33

def test_8():
    assert f2c(-100) == -73.33

def test_9():
    assert f2c(30000000) == 16666648.89

def test_10():
    assert f2c(122.567824) == 50.32


