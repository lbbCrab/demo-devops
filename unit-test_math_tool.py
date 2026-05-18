from math_tool import math_tool

def test_math_tool():
    assert math_tool(2, 3) == 5
    assert math_tool(-1, 1) == 0
    assert math_tool(10, -2) == 8
