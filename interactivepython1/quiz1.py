def check(p,q):
    print not (p or not q)

def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"

def f(x):
    print -5 * x ** 5 + 69 * x ** 2 - 47

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    return present_value * (1 + rate_per_period) ** periods

check(True, True)
check(True, False)
check(False, True)
check(False, False)

print do_stuff()

print (123 // 10) % 10
print ((123 - 123 % 10) % 100) / 10
print (123 % 10) / 10

f(0)
f(1)
f(2)

print future_value(1000, .02, 365, 3)

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

import math

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)
