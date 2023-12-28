# advanced iteration functions in the itertools package
import itertools


def testFunction(x):
    return x < 40


def main():
    # cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print("Cycle examples:")
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print()

    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print("Counter example:")
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print()

    # accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals)
    print("Accumulator example:")
    print(list(acc))
    print()

    acc = itertools.accumulate(vals, max)
    print("Accumulator example with max function:")
    print(list(acc))
    print()

    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print("Chain example:")
    print(list(x))
    print()

    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print("Dropwhile example:")
    print(list(itertools.dropwhile(testFunction, vals)))
    print()

    print("Takewhile example:")
    print(list(itertools.takewhile(testFunction, vals)))
    print()


if __name__ == "__main__":
    main()
