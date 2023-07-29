import time

# define the ASCII representation of each digit
digits = {
    '0': ["  ###  ", " #   # ", "#     #", "#     #", "#     #", " #   # ", "  ###  "],
    '1': ["   #   ", "  ##   ", " # #   ", "   #   ", "   #   ", "   #   ", " ##### "],
    '2': ["  ###  ", " #   # ", "    #  ", "   #   ", "  #    ", " #     ", " ##### "],
    '3': [" ##### ", "      #", "      #", "  ###  ", "      #", "      #", " ##### "],
    '4': ["     # ", "    ## ", "   # # ", "  #  # ", " #   # ", "#######", "     # "],
    '5': [" ##### ", " #     ", " #     ", " ##### ", "      #", " #    #", "  #### "],
    '6': ["  #### ", " #     ", " #     ", " ##### ", " #    #", " #    #", "  #### "],
    '7': [" ##### ", "     # ", "    #  ", "   #   ", "  #    ", " #     ", " #     "],
    '8': ["  ###  ", " #   # ", " #   # ", "  ###  ", " #   # ", " #   # ", "  ###  "],
    '9': ["  ###  ", " #   # ", " #   # ", "  #### ", "      #", "     # ", "  ###  "]
}

while True:
    # get the current time
    current_time = time.strftime("%H:%M:%S", time.gmtime())

    # split the time into hours, minutes, and seconds
    hours, minutes, seconds = current_time.split(":")

    # create an empty list to store the ASCII representation of the time
    time_ascii = []

    # generate the ASCII representation of each digit
    for digit in [hours[0], hours[1], minutes[0], minutes[1], seconds[0], seconds[1]]:
        digit_ascii = digits[digit]
        time_ascii.append(digit_ascii)

    # print the ASCII representation of the time
    for i in range(7):
        for j in range(6):
            print("  ".join([row[j] for row in time_ascii]), end="  ")
            print()

    # wait for 1 second before updating the clock
    time.sleep(1)
