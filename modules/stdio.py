"""custom io module created by athar mujtaba wani"""
def scanf(str:str):
    input()
    try:
        int(input())
    except Exception as e:
        
        try:
            float(input())
        except Exception as e:
            print(e)


# more functions to be added
