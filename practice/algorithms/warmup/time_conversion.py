import os


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    components = s.split(":")
    hh = int(components[0])
    mm = components[1]
    ss = components[2][:2]
    ap = components[2][-2:]

    if ap == "AM" and hh == 12:
        hh = 0
    elif ap == "PM" and hh != 12:
        hh += 12
    return f"{hh:02d}:{mm}:{ss}"


if __name__ == "__main__":
    f = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    f.write(result + "\n")

    f.close()
