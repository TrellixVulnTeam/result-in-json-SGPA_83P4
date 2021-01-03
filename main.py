import pandas
import json

credit = [3, 3, 3, 3, 3, 3, 2, 2, 2]
g2p = {"O": 10, "A": 9, "B": 8, "C": 7, "D": 6, "F": 0, "AB": 0}
res = dict()


class Student(object):
    def __init__(self, hno, grade):
        self.hno = hno
        self.grade = grade

    def calc(self):
        p = 0
        for k in range(0, len(self.grade)):
            p += g2p[self.grade[k]] * credit[k]
        p = p / 24
        res.update({self.hno:{"sgpa": p, "grade": self.grade}})


df = pandas.read_csv('res.csv',
                     names=['Ht.no', 'Subcode', 'Subname', 'Grade', 'Credits'])
rno = df['Ht.no'].to_list()
gra = df['Grade'].to_list()
i = 1
while i < len(rno):
    a = []
    tmp = rno[i]
    j = i
    while j < len(rno) and tmp == rno[j]:
        a.append(gra[j])
        j += 1
    i = j
    s = Student(tmp, a)
    s.calc()
with open("res.json", "w") as outfile:
    json.dump(res, outfile)
