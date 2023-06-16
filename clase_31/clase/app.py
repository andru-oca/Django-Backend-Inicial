def division(a,b):
    try:
        b = int(b)
        return a/b

    except ValueError as e:
        print(e)
        print("que me pasaste?")
        
    except ZeroDivisionError as e:
        print(e)
        print("no me dividas por cero")

    except Exception as e :
        print(e)
        

division(1,"0.")

print("ola k ase!")
