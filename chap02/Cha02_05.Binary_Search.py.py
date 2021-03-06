def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    mid_index = (end_index + start_index) // 2

    # Base Case _ 1
    if start_index > end_index:
        return None

    # Base Case _ 2
    elif some_list[mid_index] == element:
        return mid_index

    # Recursive Case
    # 찾는 값이 중간값 보다 큰 경우 - 오른쪽 탐색
    elif element > some_list[mid_index]:
        return binary_search(element, some_list, mid_index + 1, end_index)

    # 찾는 값이 중간값 보다 작은 경우 - 왼쪽 탐색
    elif element < some_list[mid_index]:
        return binary_search(element, some_list, 0, mid_index - 1)

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))