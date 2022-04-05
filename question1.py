import copy

def RangeIterator(main_lst, lis, max_sum):
    # if not lis:
    #     yield main_lst

    if len(lis) == 1:
        if lis[0] < max_sum:
            main_lst.append(lis[0])
            yield main_lst

    else:
        temp = copy.deepcopy(main_lst)
        yield from RangeIterator(main_lst, lis[:1], max_sum)
        main_lst = copy.deepcopy(temp)
        yield from RangeIterator(main_lst, lis[1:], max_sum)
        main_lst = copy.deepcopy(temp)
        if lis[0] < max_sum:
            main_lst.append(lis[0])
            yield from RangeIterator(main_lst, lis[1:], max_sum-lis[0])


def bounded_subset(lis, max_sum):
    lis.sort()
    if not lis:
        yield []
    elif max_sum >= 0:
        yield []
        yield from RangeIterator([], lis, max_sum)


if __name__ == '__main__':
    #simple cases - empty group
    print("Expected: [], Got")
    print("Got:")
    for i in bounded_subset([] , 0):             #expected: []
        print(i, end=' ')
    print(" ")

    #simple cases - size 1
    print("Expected: [], Got:")
    for i in bounded_subset([1] , 0):            #expected: []
        print(i, end=' ')
    print(" ")

    print("Expected: [], [1], Got:")
    for i in bounded_subset([1] , 3):            #expected: [], [1]
        print(i, end=' ')
    print(" ")


    #Simple cases - size 2
    print("Expected: [], [1], [2], [1,2], Got:")
    for i in bounded_subset([1, 2] , 7):
        print(i, end=' ')
    print(" ")

    # Simple cases - size 2
    print("Expected: [], [1], [2], Got:")
    for i in bounded_subset([1, 2], 3):
        print(i, end=' ')
    print(" ")

    print("Expected: [] [1] [2] [3] [4] [2, 3] [2, 4] [1, 2] [1, 3] [1, 4] [1, 2, 3], Got:")
    for i in bounded_subset([1, 2, 3, 4] , 7):
        print(i, end=' ')
    print(" ")
    for i in bounded_subset([1, 4, 6, 2] , 8):
        print(i, end=' ')