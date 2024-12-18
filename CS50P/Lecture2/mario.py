def main():
    square_size = input("What size? ")
    print_square(int(square_size))

def print_square(size):
    # for each row in square
    for i in range(size):

        # for each brick in row
        for j in range(size):

            # print brick
            print("#", end="")

        #new row
        print()

main()
