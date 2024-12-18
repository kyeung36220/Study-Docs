def meow(n: int) -> str: #-> None means that it does not return anything and -> str means return string
    """
    Meow n times
    :param n: Number of times to meow
    "type n: int
    :raise TypeError: If n is not an int
    "return: A string of n meows, one per line
    :rtype: str
    """
    #docstring, kind of like hashtag but with more functions, convention to documentation like param, return, etc.
    return "meow\n" * n


number: int = int(input("Number: ")) #": int" means that this should be a hint (type hint) can mypy meows1.py to check
meows: str = meow(number)
print(meows, end="")
