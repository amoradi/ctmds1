import random
import sys

def generate_random_prices(num):
    for _ in range(num):
        price = round(random.uniform(0, 100), 2)
        print(price)

def main():
    try:
        if not sys.argv[1].isdigit():
            print("Error: Please provide a valid integer")
            return
        
        num = int(sys.argv[1])
        if num <= 0:
            print("Error: Please enter a positive number")
            return
            
        generate_random_prices(num)
            
    except IndexError:
        print("Error: Please provide a number argument")
        return

if __name__ == '__main__':
    main()
