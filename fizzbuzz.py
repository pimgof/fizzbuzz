import argparse

###
num = 100
###


def fizzbuzz(n = None):
    if n == None: n = num

    for i in range(n+1):
        s = ""

        if (i % 3 == 0): s += "fizz"
        if (i % 5 == 0): s += "buzz"

        if (not(i % 3 == 0) and not(i % 5 == 0)): s += str(i)

        print(s)



def checkArgs():
    global num

    parser = argparse.ArgumentParser(description = "Add number to which the algorithm should run. Default = 100.")
    parser.add_argument("-n", "--number", help = "Add number to which the algorithm should run. Default = 100.", required = False)
    
    arguments = parser.parse_args()
    
    if arguments.number:
        print("Number manually set to {}".format(arguments.number))

        # Check if given argument is integer
        if (str(arguments.number).isnumeric()): num = int(arguments.number)
        else: print("! Argument is not a positive integer, using default instead !")



def main():
    checkArgs()
    fizzbuzz()



if __name__ == "__main__":
    main()