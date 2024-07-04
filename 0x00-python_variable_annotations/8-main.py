#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
functionX = make_multiplier(2.22)
print("{}".format(functionX(2.22)))
