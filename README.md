# ctmds1


## Setup

```bash
$ pip3 install poetry
```


## Run 

```bash
$ poetry run python3 ctmds1/main.py <number-of-elements>
```

## Test

```bash
$ poetry run pytest 
```

## Benchmark

```bash
$ poetry run python3 benchmarks/bench_main.py
```

## Dev Tools

```bash
$ make lint
$ make format
$ make pyright
$ make test
$ make coverage
$ make check # run all
```