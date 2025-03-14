from datetime import datetime
from typing import Optional

import numpy as np
import typer

from utils.constants import CountryCode, countryCodeMeanPrices
from utils.generate_normal_distribution import generate_normal_distribution
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


@app.command()
def daily_prices(
    for_date: datetime = typer.Argument(..., help="Date of prices in (YYYY-MM-DD)"),
    country_code: CountryCode = typer.Argument(
        ...,
        help=f"Country code ({', '.join(code.value for code in CountryCode)})",
    ),
    granularity: str = typer.Option(default="h", help="h: hourly hh: half hourly"),
):
    """
    TODO: annotate.

    In your output, ensure to label the hours, in some sensible way.
    E.g. 0000: 57.35; 0100: 56.98; 0200: 57.45; ...
    Add support for a --granularity option, with values h (for hourly - the default)
    or hh (for half-hourly, i.e. every 30 minutes)

    We're still keeping this intentionally abstract - but will soon make it more tangible
    with some commodity specific pricing details. For now, keep in mind the edge cases
    around the inputs. E.g. not all days have 24 hours in them! These countries all have
    Daylight Savings Time, which means every year has a "short day" (23 hours)
    and a "long day" (25 hours). In my experience, every year this little gotcha
    causes great losses or unrealised gains - and anxiety - for many trading companies
    due to various pieces of software not handling this correctly!
    """
    size = 48 if granularity == "hh" else 24
    daily_prices = generate_normal_distribution(
        countryCodeMeanPrices[country_code], size
    )

    print("daily prices", daily_prices)


if __name__ == "__main__":
    app()
