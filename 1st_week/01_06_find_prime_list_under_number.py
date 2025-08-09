input = 20

# 소수는 자기 자신과 1 외에는 아무것도 나눌 수 없다.
def find_prime_list_under_number(number):
    prime_list = []

    # 2 ~ 20찾아서 이것들이 소수인가? 소수라면 prime_list 에 넣어라!
    for n in range(2, number + 1): # 2~n 까지의 숫자들이 n에 들어가는 것을 반복한다
        for i in range(2, n): # 2 부터 n - 1 까지를 i 에 들어가는 것을 반복한다
            if n % i == 0: # ddd
                break
        else:
            prime_list.append(n)

    return []

result = find_prime_list_under_number(input)
print(result)