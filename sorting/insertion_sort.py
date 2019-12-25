"""Insertion sort
"""
def insertion_sort(arr, ascending=True):
    if not arr: return arr
    if len(arr) == 1:
        return
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if ascending:
                compare = arr[j] > arr[j+1]
            else:
                compare = arr[j] < arr[j+1]
            if  compare:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp

def main():
    test_data = [
        [3,4,7,3,76,9,3],
        [1],
        [1,2,3,4],
        [4,3,2,1],
    ]

    print('ASCENDING')
    for t in test_data:
        print('----------')
        print('In :', t)
        insertion_sort(t)
        print('Out:',t)

    print('DESCENDING')
    for t in test_data:
        print('----------')
        print('In :', t)
        insertion_sort(t, ascending=False)
        print('Out:', t)


if __name__ == '__main__':
    main()