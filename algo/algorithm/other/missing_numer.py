'''
Run Pytest: pytest missing_numer.py
'''
def solution(numbers: list):
    for i in range(len(numbers)-1):
        if numbers[i] + 1 != numbers[i+1]:
            return numbers[i] + 1


def test1():
    assert solution([1, 2, 3, 4, 5, 6, 8]) == 8

