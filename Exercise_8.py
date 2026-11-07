e_number = int(input())
e_cost = int(min(50, e_number)) * 1984
if (e_number > 50):
    e_cost += min(50, e_number - 50) * 2050
if (e_number > 100):
    e_cost += 1