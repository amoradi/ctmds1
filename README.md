# Commodity Prices CLI

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
$ poetry run python3 -m cli daily-prices
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