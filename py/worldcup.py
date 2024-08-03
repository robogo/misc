from functools import cmp_to_key
import random

class Team:
    name = ""
    score = 0
    goals = 0
    net_wins = 0
    won = []

    def __init__(self, m):
        self.name = m

    def __str__(self):
        return self.name
    
    @staticmethod
    def get(d, n):
        if n not in d:
            d[n] = Team(n)
        return d[n]

def compare(x, y):
    if (x.score != y.score):
        return x.score - y.score
    if (x.goals != y.goals):
        return x.goals - y.goals
    if (x.net_wins != y.net_wins):
        return x.net_wins - y.net_wins
    if (y.name in x.won):
        return 1
    if (x.name in y.won):
        return -1
    return ord(y.name) - ord(x.name)

def rank(results):    
    teams = {}
    for m in results.split(" "):
        kv = m.split("=")
        t = [Team.get(teams, n) for n in kv[0].split(":")]
        g = [int(i) for i in kv[1].split(":")]
        t[0].goals += g[0]
        t[0].net_wins += g[0] - g[1]
        t[1].goals += g[1]
        t[1].net_wins += g[1] - g[0]
        if g[0] > g[1]:
            t[0].score += 2
            t[0].won.append(t[1].name)
        elif g[0] == g[1]:
            t[0].score += 1
            t[1].score += 1
        else:
            t[1].score += 2
            t[1].won.append(t[0].name)
    return sorted([t[1] for t in teams.items()], key=cmp_to_key(compare), reverse=True)

s = "ABCDE"
for i in range(0, 10):
    results = ""
    for x in range(0, len(s) - 1):
        for y in range(x + 1, len(s)):
            if len(results) > 0:
                results += " "
            results += s[x] + ":" + s[y]
            results += "="
            results += str(random.randint(0, 16)) + ":" + str(random.randint(0, 16))
    print(results)
    print("".join([t.name for t in rank(results)][:3]))
# results = "A:B=1:2 A:C=1:2 A:D=1:2 A:E=1:2 B:C=1:2 B:D=1:2 B:E=1:2 C:D=1:2 C:E=1:2 D:E=1:2"
