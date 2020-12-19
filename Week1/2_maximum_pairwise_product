def maximum_pairwise_product(m):
    if (m[0] >= m[1]):
        max1 = m[0]
        max2 = m[1]
    else:
        max1 = m[1]
        max2 = m[0]
    #print(max1, max2)

    if len(m) == 2:
        return(max1 * max2)
    
    for a in range(2,len(m)):
        if m[a] >= max1:
            max2 = max1
            max1 = m[a]
        elif max1 > m[a] > max2:
            max2 = m[a]
    #print(max1, max2)
    return(max1 * max2)


if __name__ == '__main__':
    n = int(input())
    l = [int(x) for x in input().split()]
    print(maximum_pairwise_product(l))
