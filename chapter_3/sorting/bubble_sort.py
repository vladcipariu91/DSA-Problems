"""
Sam records when they wake up every morning. Assuming Sam always wakes up in the same hour, use bubble sort to sort by
earliest to latest.
"""
wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]


def bubble_sort_1(l):
    l_len = len(l)
    for i in range(l_len):
        for j in range(0, l_len - i - 1):
            if l[j] > l[j + 1]:
                aux = l[j]
                l[j] = l[j + 1]
                l[j + 1] = aux


bubble_sort_1(wakeup_times)
print("Pass" if (wakeup_times[0] == 3) else "Fail")

"""
Sam doesn't always go to sleep in the same hour. Given the following times Sam has gone to sleep, 
sort the times from latest to earliest.
"""

sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]


def bubble_sort_2(l):
    l_len = len(l)
    for i in range(l_len):
        for j in range(0, l_len - i - 1):
            if l[j][0] < l[j + 1][0] or (l[j][0] == l[j + 1][0] and l[j][1] < l[j + 1][1]):
                aux = l[j]
                l[j] = l[j + 1]
                l[j + 1] = aux


bubble_sort_2(sleep_times)
print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")
