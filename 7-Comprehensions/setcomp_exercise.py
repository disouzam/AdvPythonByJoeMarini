# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    ftemps1 = [(t*9/5)+32 for t in ctemps]
    ftemps2 = {(t*9/5)+32 for t in ctemps}
    print(ftemps1)
    print(ftemps2)

    # build a set of unique Fahrenheit temperatures
    s_temp = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in s_temp}
    print(chars)

    chars = {c.upper() for c in s_temp if not c.isspace()}
    print(chars)

    # TODO: build a set from an input source


if __name__ == "__main__":
    main()
