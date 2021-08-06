"""custom io module created by athar mujtaba wani"""

def printf(a):
    try:
        print(a)
    except Exception as e:
        print(e)

def scanf(str:str):
    input()

def scanf(int:int):
    try:
        int(input())
    except Exception as e:
        print(e)

def scanf(float:float):
    try:
        float(input())
    except Exception as e:
        print(e)

# more functions to be added
