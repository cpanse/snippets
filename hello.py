#!/usr/bin/env python3
#
def hello() -> None:
    print("Hello, World!")


def add(a: int, b: int) -> int:
    return a + b


hello()
print(add(1, 3.14))
