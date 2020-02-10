def max_product(left_cards, right_cards):
    max_num = 1
    for left in left_cards:
        for right in right_cards:
            max_num = max(max_num, left * right)

    return max_num


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))