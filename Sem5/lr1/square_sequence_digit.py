'''
Task 1. https://repl.it/@zhukov/WindingRoughApi#main.py
'''

def lengthOfNumber(number):
    l = 0
    while number > 0:
        number //= 10
        l += 1
    return l

def squareSequenceDigit(n):
    num = 0
    length = 0
    while length < n:
        num += 1
        length += lengthOfNumber(num*num)
    l1 = length - n
    num1 = (num*num) // 10**l1 % 10
    return num1

if __name__ == "__main__":
    assert squareSequenceDigit(1) == 1, "предполагаемый результат: 1"

    assert squareSequenceDigit(2) == 4, "предполагаемый результат: 4"

    assert squareSequenceDigit(7) == 5, "предполагаемый результат: 5"
    
    assert squareSequenceDigit(8) == 3, "предполагаемый результат: 3"

    assert squareSequenceDigit(12) == 6, "предполагаемый результат: 6"

    assert squareSequenceDigit(17) == 0, "предполагаемый результат: 0"

    assert squareSequenceDigit(27) == 9, "предполагаемый результат: 9"
    
    print('Все тесты пройдены успешно')