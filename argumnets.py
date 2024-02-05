import argparse

def main():
    parser= argparse.ArgumentParser()
    
    parser.add_argument("string",help="Enter a string",type=str)
    parser.add_argument("int",help="Enter an integer",type=int)
    parser.add_argument("float",help="Enter a float",type=float)

    args = parser.parse_args()
    print(f"{args.string} {args.int} {args.float}")

if __name__ == "__main__":
    main()