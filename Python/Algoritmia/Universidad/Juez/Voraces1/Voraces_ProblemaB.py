a, b, c = map(int, input().strip().split())
if a < 0 or b < 0 or c < 0 :
    print("ERROR")
elif a + b + c != 180:
    print("NO")
else:
    print("SI")