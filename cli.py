from typing import Optional

import numpy as np
import typer

from utils.generate_random_prices import generate_random_prices
from utils.validation import validate_non_negative

app = typer.Typer()

@app.command()
def random_prices(
    num: int = typer.Argument(
        ..., help="Number of random prices to generate", callback=validate_non_negative
    ),
) -> Optional[np.ndarray]:
    result = generate_random_prices(num)
    print(np.array2string(result, separator="\n")[1:-1])
    return result


# @app.command()
# def daily_prices()
#     # todo

if __name__ == "__main__":
    app()
