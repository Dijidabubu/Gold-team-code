def print_full_name(first, last):
    # Write your code here
    print("Hello " + first + " " + last + "! You just delved into python.")
    
if __name__ == '__main__':
    first_name = input("Input first name: ")
    last_name = input("Input last name: ")
    print_full_name(first_name, last_name)