from math import cos

from calculated_values import CalculatedValues


def calculate_cos(radians: float, epsilon: float) -> CalculatedValues:
    if epsilon <= 0:
        raise ValueError('Epsilon has to be positive')

    exact_value = cos(radians)

    current_sum = 1
    difference = abs(exact_value - current_sum)
    n = 0
    sign = 1
    numerator = 1
    denominator = 1


    while difference > epsilon:
        n += 1
        sign *= -1
        numerator *= radians ** 2
        denominator = denominator * (2 * n - 1) * (2 * n)
        summand = sign * (numerator / denominator)
        current_sum += summand
        difference = abs(exact_value - current_sum)

    return CalculatedValues(exact_value, current_sum, n)


def main():
    radians = float(input('Radians: '))
    epsilon = float(input('Epsilon: '))

    print(calculate_cos(radians, epsilon))


if __name__ == '__main__':
    main()
