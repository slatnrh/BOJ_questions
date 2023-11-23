# -를 기준으로 나누기(-뒤를 괄호로 하면 최대로 뺄 수 있기 때문)
question_lst = input().split('-')
answer_lst = []

for question in question_lst:
    sum = 0
    # -를 기준으로 나눈 후 +를 기준으로 나눠서 합 구하기
    tmp = question.split('+')
    for i in tmp:
        sum += int(i)
    answer_lst.append(sum)

# 첫째항은 숫자이기 때문에 이후에 모든 항을 빼서 최솟값 출력
rslt = answer_lst[0]
for answer in range(1, len(answer_lst)):
    rslt -= answer_lst[answer]

print(rslt)