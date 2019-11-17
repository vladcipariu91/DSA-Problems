"""
Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of
platforms required so that no train has to wait for the other(s) to leave.

You will be given arrival and departure times in the form of a list.

Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be written as 930. Similarly, 13:45 would be given as 1345
"""


def min_platform(arrival, departure):
    if len(arrival) != len(departure):
        return None

    platforms = [[]]
    index = 0
    while index < len(arrival):
        train = Train(arrival[index], departure[index])
        should_add_new_platform = True
        for p_index, p in enumerate(platforms):
            if len(p) == 0:
                p.append(train)
                should_add_new_platform = False
                break
            else:
                existing_train = p[0]
                if existing_train.departure <= train.arrival:
                    should_add_new_platform = False
                    p[0] = train
                    break

        if should_add_new_platform:
            platform = [train]
            platforms.append(platform)

        index += 1

    return len(platforms)


class Train:
    def __init__(self, arrival, departure):
        self.arrival = arrival
        self.departure = departure


arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
print(min_platform(arrival, departure))
