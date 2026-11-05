"""
All this binary to decimal and decimal to binary stuff...
you're at your wits end! This time you're going to try the
*octal* number system.

Octal is similar to binary, except instead of only two unique
characters per digit (0 or 1), octal has 8 (0, 1, 2, ...7)!!
This means an octal number system has a base of 8, so
10 OCTAL is 8 DEC.

Your task is to write a function to convert an octal string
into a decimal value

Directions:
  *USE A LOOP* to convert an octal string into a decimal value

Arguments:
  string of digits from 0 to 7

Returns:
  decimal integer

Examples:
  >>> print(octal_to_decimal("10"))
  8
  >>> print(octal_to_decimal("125"))
  85
"""
def octal_to_decimal(octal_number):
  # Your code below


  return None


# Test cases
print(octal_to_decimal("0"))    # 0
print(octal_to_decimal("1"))    # 1
print(octal_to_decimal("7"))    # 7
print(octal_to_decimal("10"))   # 8
print(octal_to_decimal("17"))   # 15
print(octal_to_decimal("125"))  # 85
print(octal_to_decimal("701"))  # 449
