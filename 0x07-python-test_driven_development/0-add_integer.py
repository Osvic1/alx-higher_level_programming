def add_integer(a, b=98):
    """
    This functn adds 2 integers,or 1 integer & 1 float thats castd to int
    :param a: first number to add.Must be integer or float
    :param b: second number to add.Must be integer or float.Default value is 98
    :return: the addition of a and b as an integer
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
