from datetime import datetime
from typing import Optional

import numpy as np
import typer

from utils.constants import CountryCode, countryCodeMeanPrices
from utils.generate_normal_distribution import generate_normal_distribution
from utils.generate_random_prices import generate_random_prices
from utils.generate_times import generate_times
from utils.is_dst_transition_day import is_dst_transition_day
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


@app.command()
def daily_prices(
    for_date: datetime = typer.Argument(..., help="Date of prices in (YYYY-MM-DD)"),
    country_code: CountryCode = typer.Argument(
        ...,
        help=f"Country code ({', '.join(code.value for code in CountryCode)})",
    ),
    granularity: str = typer.Option(default="h", help="h: hourly hh: half hourly"),
):
    hour_size = 24

    match is_dst_transition_day(for_date.strftime("%Y-%m-%d"), country_code.value):
        case "short":
            hourSize = 23
        case "long":
            hourSize = 25

    is_hh = granularity == "hh"
    size = hour_size * 2 if is_hh else hour_size
    daily_prices = generate_normal_distribution(
        countryCodeMeanPrices[country_code], size
    )

    times = generate_times(hour_size, True if is_hh else False)

    times_and_prices = np.array(list(zip(times, daily_prices)))

    print("daily prices", times_and_prices)


if __name__ == "__main__":
    app()
