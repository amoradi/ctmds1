# Commodity Prices CLI

A command-line tool for generating simulated commodity/energy prices for European electricity markets. Built as a demonstration of clean Python CLI development practices with proper testing, type safety, and performance considerations.

## What It Does

- **Random price generation** - Generates arbitrary quantities of random prices using NumPy's vectorized operations
- **Daily price simulation** - Produces realistic daily price curves for European markets (DE, FR, GB, NL) using normal distributions centered on country-specific mean prices
- **Granularity options** - Supports both hourly (24 intervals) and half-hourly (48 intervals) price data
- **DST-aware** - Correctly handles daylight saving time transitions, generating 23-hour or 25-hour day profiles as appropriate

## Tech Stack

- **Python 3.13+** with full type annotations
- **Typer** for CLI interface
- **NumPy** for efficient numerical operations
- **pytz** for timezone/DST calculations
- **Poetry** for dependency management
- **Ruff** for linting and formatting
- **Pyright** for static type checking
- **pytest + coverage** for testing

## Notable Implementation Details

- Uses NumPy vectorization over Python loops for price generation (benchmarks included showing ~10-100x performance improvement at scale)
- Country-specific mean prices based on real European wholesale electricity market averages
- DST detection uses pytz to calculate actual day length rather than hardcoding transition dates

## Setup

```bash
$ pip3 install poetry
```


## CLI Commands

```bash
$ # help
$ poetry run python3 -m cli --help
$
$ # random-prices
$ poetry run python3 -m cli random-prices <number-of-prices>
$
$ # daily prices
$ poetry run python3 -m cli daily-prices <date> <country-code> --granularity h or hh
```

## Dev Commands

```bash
$ make lint
$ make format
$ make pyright
$ make test
$ make coverage
$ make coverage-html
$ make benchmark
$ make check # run ~all
```