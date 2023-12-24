N = int(input())
# 첫번째 문자 저장
word = list(input())
word_len = len(word)
             
for i in range(N - 1):
    # 두번째부터 마지막까지 문자 한개씩 저장
    other_words = list(input())
    for j in range(word_len):
        # 다르면 ?로 변환
        if word[j] != other_words[j]:
            word[j] = '?'

# 문자열 합치려고 join함수 사용
print(''.join(word))