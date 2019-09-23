def function(num):
    if num == 0:
        return 0
    else:
        return function(num - 1)


print(function(2))
