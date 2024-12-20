from matplotlib import pyplot as plt

# dynamic mappers
def mapLinePlot(x, y, chart_title, x_label, y_label):
    plt.plot(x, y)
    plt.title(chart_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# static mappers
# {1: {...}}: 1 = spots played & ... = {matches: payout}
kenoPayoutMapper = {
        1: {0: 0, 1: 2.5},
        2: {0: 0, 1: 1, 2: 5},
        3: {0: 0, 1: 0, 2: 2.5, 3: 25},
        4: {0: 0, 1: 0, 2: 1, 3: 4, 4: 100},
        5: {0: 0, 1: 0, 2: 0, 3: 2, 4: 20, 5: 450},
        6: {0: 0, 1: 0, 2: 0, 3: 1, 4: 7, 5: 50, 6: 1600},
        7: {0: 0, 1: 0, 2: 0, 3: 1, 4: 3, 5: 20, 6: 100, 7: 5000},
        8: {0: 0, 1: 0, 2: 0, 3: 0, 4: 2, 5: 10, 6: 50, 7: 1000, 8: 15000},
        9: {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 5, 6: 25, 7: 200, 8: 4000, 9: 40000},
        10: {0: 2, 1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 20, 7: 80, 8: 500, 9: 10000, 10: 100000},
        11: {0: 2, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 10, 7: 50, 8: 250, 9: 1500, 10: 15000, 11: 500000},
        12: {0: 4, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 5, 7: 25, 8: 150, 9: 1000, 10: 2500, 11: 25000, 12: 1000000},
    }

# coder [0 = "No Win", 1 = "One Digit Match", 2 = "Two Digit Contigous Match", 3 = "First Three Exact", 4 = "First 3 Any",
#  "     5 = "Last Three Exact", 6 = "Last Three Any", 7 = "All Four Exact", 8 = "All Four Any""]
numbersPayoutMapper = {
    0: 0,
    1: 4,
    2: 10,
    3: 500,
    4: 250,
    5: 500,
    6: 250,
    7: 2000,
    8: 5000
}

# true = matched pb & false = no match pb
powerballPayoutMapper = {
    "True": {
        0: 4,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 80000000
    },
    "False": {
        0: 0,
        1: 0,
        2: 0,
        3: 7,
        4: 100,
        5: 1000000
    }
}

# matches: payout
massCashPayoutMapper = {
    0: 0,
    1: 0,
    2: 0,
    3: 10,
    4: 250,
    5: 100000,
}