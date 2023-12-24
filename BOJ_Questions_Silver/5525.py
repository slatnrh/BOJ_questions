import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

ans, i, cnt = 0, 0, 0

while i < (M-1):
    # IOI 체크 후
    if S[i:i+3] == 'IOI':
        # 두 칸 뒤에도 IOI 체크
        i += 2
        # IOI의 갯수 저장
        cnt += 1

        if cnt == N:
            # 원하는 IOIOI를 찾으면 출력값 +1
            ans += 1
            # 맨 앞 IOI를 지워주기 위해 cnt -1
            cnt -= 1
    # IOI 체크 중 이상 있으면 초기화
    else:
        i += 1
        cnt = 0

print(ans)