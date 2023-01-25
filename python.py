while True:
    code=input(">>> ")
    try:
        exec(code)
    except BaseException as error:
        print(error)
