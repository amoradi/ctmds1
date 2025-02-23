from typing import Optional

import numpy as np
import typer

from ctmds1.generate_random_prices import generate_random_prices


def validate_non_negative(value: int) -> int:
    if value < 0:
        raise typer.BadParameter("Number must be non-negative")
    return value


def main(
    num: int = typer.Argument(
        ..., help="Number of random prices to generate", callback=validate_non_negative
    ),
) -> Optional[np.ndarray]:
    result = generate_random_prices(num)
    print(np.array2string(result, separator="\n")[1:-1])
    return result


if __name__ == "__main__":
    typer.run(main)
