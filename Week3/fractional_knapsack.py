# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
        
    while (capacity > 0):
        pos = position(values, weights)

        if (capacity > weights[pos]):
            value = value + values[pos]
            capacity = capacity - weights[pos]
            values[pos] = 0
        else:
            value = value + capacity * (values[pos]/weights[pos])
            capacity = 0
    return value

def position(values, weights):
    #print(values)
    #print(weights)
    vdw = []
    for i in range(len(weights)):
        vdw.append(values[i]/weights[i])
    #print(vdw.index(max(vdw)))
    return vdw.index(max(vdw))

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
