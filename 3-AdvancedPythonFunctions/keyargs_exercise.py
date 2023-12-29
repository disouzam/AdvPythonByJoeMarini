# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(*, arg1, arg2, suppressExceptions=False):
    pass


def main():
    # try to call the function without the keyword
    myFunction(arg1=1, arg2=2, suppressExceptions=True)


if __name__ == "__main__":
    main()
