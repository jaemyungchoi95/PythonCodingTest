
# ascii code
# 컴퓨터를 통해서 문자를 저장하고 싶은데
# 컴퓨터는 오로지 숫자밖에 저장할 수 없으니
#
# 문자를 나타내기로 약속한 숫자들을 정해놓은 것이고
# 그 숫자(코드)들을 바로 ASCII 코드라고 한다.

# a -> 97 ord
#
# 97 -> a chr

'a-z'
# [0] -> 'a'
# [1] -> 'b'
# [25] -> 'z'

#
# print(ord('a') - 97)
# print(ord('b') - 97)

# print('a')

# chr() 은 인수로 숫자를 넣으면 그 숫자가 어떤 문자를 의미하는지 역 연산을 해주는 함수이다.
# 1번째 인덱스에 무슨 알파벳을 넣은건지를 알고 싶어.
#  -> chr()