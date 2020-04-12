import discordflags as df


if __name__ == '__main__':
    print('Press Control-C to exit.')
    while True:
        x = input("User flags value: ")
        if df.flagsfromint(x):
            for y in df.flagsfromint(x):
                print(y)
        else:
            print("Invalid flag value passed.")
