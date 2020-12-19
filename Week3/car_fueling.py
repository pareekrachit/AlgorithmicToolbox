import sys

def compute_min_refills(distance, tank, stops):
    # write your code here
    numRefills = 0
    lastRefill = 0
    currentPos = 0
    while (currentPos < len(stops)-1):
        if (stops[currentPos+1] - stops[lastRefill] <= tank):
            currentPos = currentPos+1
        elif (stops[currentPos+1] - stops[currentPos] > tank):
            return -1
        else:
            lastRefill = currentPos
            numRefills = numRefills+1
            currentPos = currentPos+1
    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    stops.append(d)
    stops.insert(0,0)
    print(compute_min_refills(d, m, stops))