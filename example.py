import discordflags as df


if __name__ == '__main__':
    print('Press Control-C to exit.')
    while True:
        try:
            x = input("User flags value: ")
        # Exit cleanly when the user presses 'Control-D' or 'Control-C'
        except (EOFError, KeyboardInterrupt):
            print('\nExiting.')
            exit()
        if df.flagsfromint(x):
            for y in df.flagsfromint(x):
                print(y)
        else:
            print("Invalid flag value passed.")
