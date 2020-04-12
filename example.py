import flags
while True:
    x = input("User flags value: ")
    if flags.flagsfromint(x):
        for y in flags.flagsfromint(x):
        print(y)
    else:
        print("Invalid flag value passed.")
