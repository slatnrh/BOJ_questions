ohm = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

color1 = input()
color2 = input()
color3 = input()

# dictionary로 저장된 값들에서 1, 2번 색상은 숫자로 표현, 3번 색상은 10의 배수로 표현
print((ohm[color1]*10 + ohm[color2]) * 10**ohm[color3])