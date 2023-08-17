#!usr/bin/python3
if __name__ == "__main__":
    """get the sum, difference, multiple, quotient of 10 and 5"""
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    sum_result = add(a, b)
    diff_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    print(f"sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Multiple: {mul_result}")
    print(f"Division: {div_Result}")
