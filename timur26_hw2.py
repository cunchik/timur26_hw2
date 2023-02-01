def lange(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)


def ist_quadratisch(x1, y1, x2, y2, x3, y3):
    erste = lange(x1, y1, x2, y2)
    zweite = lange(x1, y1, x3, y3)
    dritte = lange(x2, y2, x3, y3)
    l1 = [erste, zweite, dritte]
    l1.sort()
    dsf = erste + zweite+ dritte
    print(dsf)
    with open('area.txt', 'w') as is_area:
        is_area.write(f'{dsf}')
    if round(l1[0] ** 2 + l1[1] ** 2) == round(l1[2] ** 2):
        with open('truefalse.txt', 'w') as is_area:
            is_area.write('True')
        return True
    else:
        with open('truefalse.txt', 'w') as is_area:
            is_area.write('False')
        return False

print(ist_quadratisch(2,2,2,2,2,2))

#2
fin = open('input.txt', encoding='utf8')
d = {}
for line in fin:
    words = line.strip().split()
    for word in words:
        d[word] = d.get(word, 0) + 1
for i in sorted(d.items(), key=lambda x: (x[0])):
    if i[1] == max(d.values()):
        print(i[0])
        break


#3
def sort_times(n, times):
  sorted_times = sorted(times, key=lambda x: (x[0], x[1], x[2]))
  return sorted_times

n = 5
times = [(23, 59, 59), (0, 0, 0), (12, 34, 56), (9, 30, 0), (3, 45, 17)]
result = sort_times(n, times)
print(result)


