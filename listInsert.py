a = [3, 1, 0, 2, 4]
source_a = len(a)

for i in range(len(a)):
    for j in range(len(a)):
        if i == a[j]:
            a.insert(i, a[j])
a = a[: source_a]
print(a)

#insert(인덱스, 값) - 인덱스 위치에 값을 하나 추가

