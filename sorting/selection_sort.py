"""Selection sort
"""
def bubble_sort(arr, left_pt=0, ascending=True):
    if left_pt == len(arr) - 1:
        return

    if ascending:
        th = float('inf')
    else:
        th = float('-inf')

    min_i = None
    for i in range(left_pt, len(arr)):
        if ascending:
            update = arr[i] < th
        else:
            update = arr[i] > th
        
        if update:
            th = arr[i]
            min_i = i

    if min_i is not None:
        tmp = arr[left_pt]
        arr[left_pt] = arr[min_i]
        arr[min_i] = tmp
        left_pt += 1

    bubble_sort(arr, left_pt, ascending)


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
        bubble_sort(t)
        print('Out:',t)

    print('DESCENDING')
    for t in test_data:
        print('----------')
        print('In :', t)
        bubble_sort(t, ascending=False)
        print('Out:', t)


if __name__ == '__main__':
    main()