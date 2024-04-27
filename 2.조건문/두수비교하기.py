import sys
input = sys.stdin.readline

v1 = int(input())

if 90 <= v1 and v1 <= 100:
    print("A")
elif 80 <= v1 and v1 <= 89:
    print("B")
elif 70 <= v1 and v1 <= 79:
    print("C")
elif 60 <= v1 and v1 <= 69:
    print("D")
else:
    print("F")

