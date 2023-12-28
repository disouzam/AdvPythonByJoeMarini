"""Check truth values"""
from decimal import Decimal
from fractions import Fraction

# False and Note evaluate to false
BOOLFALSE = False
if not BOOLFALSE:
    print("False from a boolean False")

BOOLNONE = None
if not BOOLNONE:
    print("False from a None value")

# Numeric zero values evaluate to false
INTEGERZERO = 0
if not INTEGERZERO:
    print("False from an integer Zero")

FLOATZERO = 0.0
if not FLOATZERO:
    print("False from a floating zero")

COMPLEXZERO = 0j
if not COMPLEXZERO:
    print("False from a complex zero")

# Decimal and Fraction zeros
DECIMALZERO = Decimal(0)
if not DECIMALZERO:
    print("False from a decimal zero")

FRACTIONZERO = Fraction(0, 5)
if not FRACTIONZERO:
    print("False from a fractional zero")

# Empty sequences and collections
EMPTYSTRING = ''
if not EMPTYSTRING:
    print("False from a empty string")

EMPTYTUPLE = ()
if not EMPTYTUPLE:
    print("False from a empty tuple")

EMPTYLIST = []
if not EMPTYLIST:
    print("False from a empty list")

EMPTYDICTIONARY = {}
if not EMPTYDICTIONARY:
    print("False from a empty dictionary")

# Empty sets and ranges
EMPTYSET = set()
if not EMPTYSET:
    print("False from a empty set")

EMPTYRANGE = range(0)
if not EMPTYRANGE:
    print("False from a empty range")

# Custom objects


class MyClassAsTrue:
    """A blank class definition with no overload of __bool__ and __len__ methods"""


instance1 = MyClassAsTrue()

if instance1:
    print("True from a default class - no overloading of bool and len methods")


class MyClassAsFalse:
    """__bool__ and __len__ methods were overriden"""

    def __bool__(self):
        return False

    def __len__(self):
        return 0


instance2 = MyClassAsFalse()

if not instance2:
    print("False from a modified class")
