import sys
input = sys.stdin.readline

# 키패드 표현
keyboard = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

p, w = map(int, input().split())
text = input()

time = 0
# 이전 입력 문자 선언
past_j = ''

# for i: 문자열에서 각 한 문자씩 저장
for i in range(len(text)):
    # 공백 입력 시
    if text[i] == ' ':
            # 입력 시간 +
            time += p
            past_j = ''
    for j in range(len(keyboard)):
        for k in range(len(keyboard[j])):
            # 문자 == 키패드일 시
            if text[i] == keyboard[j][k]:
                # 이전 입력 문자와 동일할 시
                if j == past_j:
                    # 기다려야 하는 시간 +
                    time += w
                time += (1 + k) * p
                # 이전 입력 문자 저장
                past_j = j
print(time)