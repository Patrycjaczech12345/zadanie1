def stan_zdrowia(nalogi, choroby, operacje):
    stan_zdrowia = nalogi + choroby + operacje
    if nalogi == "TAK":
        nalogi = 1

    else:
        nalogi = 0

    if choroby == "TAK":
        choroby = 1
    else:
        choroby = 0

    if operacje == "TAK":
        operacje = 1
    else:
        operacje = 0

    if stan_zdrowia == 3:
        return str("Można inwestować")
    elif stan_zdrowia < 3:
        return str("nie można inwestować")