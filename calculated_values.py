from typing import NamedTuple


class CalculatedValues(NamedTuple):
    exact_value: float
    final_value: float
    number_of_iterations: float


    def __repr__(self) -> str:
        return (
        f'---\n'
        f'{"Calculated cosine:":<30}{self.final_value:>20}\n'
        f'{"Exact cosine:":<30}{self.exact_value:>20}\n'
        f'{"Number of iterations (N):":<30}{self.number_of_iterations:>20}\n'
        )
