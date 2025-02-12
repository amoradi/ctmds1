import sys
import numpy as np

ERR_NOT_INTEGER = "Error: Please provide a valid integer"
ERR_NO_ARGUMENT = "Error: Please provide a number argument"

def generate_random_prices(num, print_output=False):
    """
    Generate random prices between 0 and 100 with 2 decimal places
    
    Args:
        num (int): Number of prices to generate
        print_output (bool): Whether to print the results
    
    Returns:
        numpy.ndarray: Array of random prices
    """
    prices = np.round(np.random.uniform(0, 100, size=num), 2)
    
    if print_output:
        np.savetxt(sys.stdout, prices, fmt='%.2f')
    
    return prices

def main():
    try:
        if not sys.argv[1].isdigit():
            print(ERR_NOT_INTEGER)
            return None
        
        num = int(sys.argv[1])
            
        # By default, print when running from command line
        return generate_random_prices(num, print_output=True)
            
    except IndexError:
        print(ERR_NO_ARGUMENT)
        return None

if __name__ == '__main__':
    main()
    