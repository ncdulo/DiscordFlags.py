staff = 1
partner = 1<<1
hypesquad = 1<<2
bug_hunter = 1<<3
unknown_4 = 1<<4
unknown_5 = 1<<5
hypesquad_bravery = 1<<6
hypesquad_brilliance = 1<<7
hypesquad_balance = 1<<8
early_supporter = 1<<9
team_user = 1<<10
unknown_11 = 1<<11
system = 1<<12
unknown_13 = 1<<13
bug_hunter_2 = 1<<14
unknown_15 = 1<<15
unknown_16 = 1<<16
unknown_17 = 1<<17
#all current flags defined here
def flagsfromint(flags):
    if flags.isnumeric():
        flags = int(flags)
        flaglist=[]
        if (flags & staff) == staff:
            flaglist.append("Staff")
        if (flags & partner) == partner:
            flaglist.append("Partner")
        if (flags & hypesquad) == hypesquad:
            flaglist.append("Hypesquad Events")
        if (flags & bug_hunter) == bug_hunter:
            flaglist.append("Bug hunter")
        if (flags & unknown_4) == unknown_4:
            flaglist.append("MFA_SMS")
        if (flags & unknown_5) == unknown_5:
            flaglist.append("PREMIUM_PROMO_DISMISSED")
        if (flags & hypesquad_bravery) == hypesquad_bravery:
            flaglist.append("Hypesquad bravery")
        if (flags & hypesquad_brilliance) == hypesquad_brilliance:
            flaglist.append("Hypesquad brilliance")
        if (flags & hypesquad_balance) == hypesquad_balance:
            flaglist.append("Hypesquad balance")
        if (flags & early_supporter) == early_supporter:
            flaglist.append("Early nitro")
        if (flags & team_user) == team_user:
            flaglist.append("Team user")
        if (flags & unknown_11) == unknown_11:
            flaglist.append("Unused")
        if (flags & system) == system:
            flaglist.append("System")
        if (flags & unknown_13) == unknown_13:
            flaglist.append("Unread urgent system message ")
        if (flags & bug_hunter_2) == bug_hunter_2:
            flaglist.append("Bug hunter lvl2")
        if (flags & unknown_15) == unknown_15:
            flaglist.append("UNDERAGE_DELETED")
        if (flags & unknown_16) == unknown_16:
            flaglist.append("Verified Bot")
        if (flags & unknown_17) == unknown_17:
            flaglist.append("Verified Developer")
        return flaglist
    else:
        return False
