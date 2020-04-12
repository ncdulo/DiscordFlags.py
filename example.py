import flags


if __name__ == '__main__':
    print('Press Control-C to exit.')
    while True:
        x = input("User flags value: ")
        if flags.flagsfromint(x):
            for y in flags.flagsfromint(x):
                print(y)
        else:
            print("Invalid flag value passed.")
