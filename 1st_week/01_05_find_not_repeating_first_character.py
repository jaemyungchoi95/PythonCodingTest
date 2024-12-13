# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.
# (원 문제 링크 : https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/)
# "abadabac" # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!

def find_not_repeating_first_character(string):
    # 반복되지 않는 첫번째 알파벳
    # 반복되는지 아닌지를 판단해야 한다.
    # alphabet_occurrence_array 의 원리를 활용해야 한다. 아래는 로직을 구현하는 순서
    # string 에서 알파벳의 빈도수를 찾는다.
    # O(N)
    occurrence_array = find_alphabet_occurrence_array(string)
    # 그리고 빈도수가 1인 알파벳들 중에서 string에서 뭐가 먼저 나왔는지를 찾아본다.
    not_repeating_charactor_array = []
    for index in range(len(occurrence_array)):
        alphabet_occurrence = occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_charactor_array.append(chr(index + ord('a')))

    for char in string:
        if char in not_repeating_charactor_array:
            return char
    return "_"

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))