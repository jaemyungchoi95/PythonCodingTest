# 두번째 문제 : 최빈값 찾기 (프로그래머스 : https://school.programmers.co.kr/learn/courses/30/lessons/120812)
# Q. Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오
# "hello my name is dingcodingco"

# 1. a, b, c 처럼 문자가 해당 문자열에 얼마나 있는지 파악하고, 그 개수가 가장 크다면 반환해줘야 하는 값을 그 알파벳으로 변환한다.
# a -> hello my name is dingcodingco -> 0 max_occurence = 0 max_alphabet = a
# b -> hello my name is dingcodingco -> 0 max_occurence = 0 max_alphabet = b
# c -> hello my name is dingcodingco -> 2 max_occurence = 2 max_alphabet = c
#
# def find_max_occurred_alphabet(string):
#     alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
#                       "t", "u", "v", "x", "y", "z"]
#     max_occurrence = 0
#     max_alphabet = alphabet_array[0]
#
#     for alphabet in alphabet_array:
#         occurrence = 0
#         for char in string:
#             if char == alphabet:
#                 occurrence += 1
#
#         if occurrence > max_occurrence:
#             max_alphabet = alphabet
#             max_occurrence = occurrence
#
#     return max_alphabet

# 2. [0 * 26] 각 알파벳의 빈도수를 저장한 배열을 만든다.
# 그리고 문자열을 돌면서 해당 문자가 알파벳이라면, 알파벳은 인덱스화 시켜서 알파벳의 빈도수를 업데이트 한다.
# a -> 0번째 인덱스 값을 올리고, z가 나왔다면 가장 마지막인 25번째 인덱스의 값을 추가해라.
#
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha(): # 알파벳인지 아닌지 검사
            continue
        arr_index = ord(char) - ord('a') # 해당 문자를 인덱스로 치환한다. a -> 0 , b -> 1
        alphabet_occurrence_array[arr_index] += 1 # 빈도수 배열에 인덱스로 찾아가서 해당 값을 추가해준다.

    print("alphabet_occurrence_array is ", alphabet_occurrence_array)

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)): # 0, 1, ...25
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
    print("max_alphabet_index is ", max_alphabet_index)

    return chr(max_alphabet_index + ord('a'))

    # 8 -> i 인덱스 -> 아스키코드 형태로 만들고 -> 알파벳
    # 0 -> a
    # 0 -> 97 -> a
    # chr(0 + ord('a')) -> a

    # chr(97) == 'a'
    # chr(0 + ord('a')) == 'a'
    # chr(0 + 97) == 'a'
    # chr(1 + 97) == 'b'

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))