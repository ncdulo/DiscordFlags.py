staff = 1
partner = 2
hypesquad = 4
bug_hunter = 8
unknown_4 = 1<<4
unknown_5 = 1<<5
hypesquad_bravery = 64
hypesquad_brilliance = 128
hypesquad_balance = 256
early_supporter = 1<<9
team_user = 1024
unknown_11 = 1<<11
system = 4096
unknown_13 = 1<<13
bug_hunter_2 = 1<<14
unknown_15 = 1<<15
unknown_16 = 1<<16
while True:
    flags=input("flags: ")
    if flags.isnumeric():
        print("Valid flags")
        flags = int(flags)
        if (flags & staff) == staff:
            print("Staff")
        if (flags & partner) == partner:
            print("Partner")
        if (flags & hypesquad) == hypesquad:
            print("Hypesquad Events")
        if (flags & bug_hunter) == bug_hunter:
            print("Bug hunter")
        if (flags & unknown_4) == unknown_4:
            print("unknown_4")
        if (flags & unknown_5) == unknown_5:
            print("unknown_5")
        if (flags & hypesquad_bravery) == hypesquad_bravery:
            print("Hypesquad bravery")
        if (flags & hypesquad_brilliance) == hypesquad_brilliance:
            print("Hypesquad brilliance")
        if (flags & hypesquad_balance) == hypesquad_balance:
            print("Hypesquad balance")
        if (flags & early_supporter) == early_supporter:
            print("Early nitro")
        if (flags & team_user) == team_user:
            print("Team user")
        if (flags & unknown_11) == unknown_11:
            print("unknown_11")
        if (flags & system) == system:
            print("System")
        if (flags & unknown_13) == unknown_13:
            print("unknown_13")
        if (flags & bug_hunter_2) == bug_hunter_2:
            print("Bug hunter lvl2")
        if (flags & unknown_15) == unknown_15:
            print("unknown_15")
        if (flags & unknown_16) == unknown_16:
            print("Verified Bot")