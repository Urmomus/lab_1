from math import cos


def calculate_cos(radians: float, epsilon: float):
    exact_sum = cos(radians)

    curr_sum = 1
    diff = abs(exact_sum - curr_sum)
    n = 0
    sign = 1
    numerator = 1
    denominator = 1


    while diff > epsilon:
        n += 1
        sign *= -1
        numerator *= radians ** 2
        denominator = denominator * (2 * n - 1) * (2 * n)
        summand = sign * (numerator / denominator)
        curr_sum += summand
        diff = abs(exact_sum - curr_sum)

    print(f'---\n'
          f'Calculated cosine: {curr_sum}\n'
          f'Exact cosine: {exact_sum}\n'
          f'Number of iterations (N): {n}\n')


def main():
    radians = float(input('Eadians: '))
    epsilon = float(input('Epsilon: '))

    if epsilon <= 0:
        raise ValueError('Epsilon has to be positive')

    calculate_cos(radians, epsilon)


if __name__ == '__main__':
    main()
