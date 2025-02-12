# ctmds1

- Write a command line utility which takes an argument num and produces that many random numbers in the range 0 - 100.
  - The numbers should be suitable to represent a price (e.g 65.48)
- Structure your code and files in whatever way you think is right.
  - Please use snake_case for file and directory names - no spaces, no capital letters.
- Write one or more unit tests for your code
- Try to optimise your code - what's the fastest you can generate 100,000 random prices in that range?


-------

## Run 

```bash
$ python3 generate_random_prices.py <number-of-elements>
```

## Test

```bash
$ pytest generate_random_prices_test.py -v
```

## Benchmark

```bash
$ python3 benchmark.py
```