def show_name_error():
    print(i_do_not_exist)


def show_type_error():
    error = 5 + "I can't be added to 5"


def show_syntax_error():
    print("Syntax error here")


def show_attribute_error():
    print("Attr error here")


if __name__ == "__main__":
    while True:
        errorType = raw_input("Type a letter to see the error: "
                              "(N)ameError, (T)ypeError, (S)yntaxError, (A)ttributeError: ")
        errorType = errorType.upper()

        if errorType == "N":
            show_name_error()
        elif errorType == "T":
            show_type_error()
        elif errorType == "S":
            show_syntax_error()
        elif errorType == "A":
            show_attribute_error()