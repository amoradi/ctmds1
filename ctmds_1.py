import argparse
import random

def generate_random_prices(num):
    for _ in range(num):
        # Generate random price between 0 and 100 with 2 decimal places
        price = round(random.uniform(0, 100), 2)
        print(price)

def main():
    parser = argparse.ArgumentParser(description='Generate random prices between 0 and 100')
    parser.add_argument('num', type=int, help='Number of prices to generate')
    args = parser.parse_args()

    if args.num <= 0:
        print("Please enter a positive number")
        return

    generate_random_prices(args.num)

if __name__ == '__main__':
    main()
    