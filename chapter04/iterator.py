# For loop
# x => is iterator
# array => is iterable


# Iterationing array
for x in [1,2,3]:
    print(x)


# Iterationing in string
for x in "Python for Geeks":
    print(x, end="")


# Iteration on a dictonary

week_day={
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

for k in week_day:
    print(k,week_day[k])