# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)),
                  ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                  ("Kings", (15, 15)), ("Chargers", (20, 10)),
                  ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)

    # Use popitem to remove the top item
    tw, wl = teams.popitem(False)
    print("Top team: ", tw, wl)
    print(teams)

    # What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})
    assert a == b, "Ordered dictionaries are equal if elements are the same and order is the same"
    print("Equality test: ", a == b)

    a = OrderedDict({"a": 1, "c": 3, "b": 2})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})
    assert a != b, "Ordered dictionaries are different if elements are the different or if order is different"
    print("Equality test: ", a == b)

    a = OrderedDict({"a": 1, "c": 3, "b": 2})
    b = {"a": 1, "b": 2, "c": 3}
    assert a == b, "Regular Dictionaries are equal if elements are the same"
    print("Equality test: ", a == b)


if __name__ == "__main__":
    main()
