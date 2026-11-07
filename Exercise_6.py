a, b, c = map(float, input().split())
if (a + b > c and a + c > b and b + c > a):
    p = float((a + b + c) / 2)
    S = float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    print(f"{S:.1f}")
else:
    print("Khong phai 3 canh cua tam giac")