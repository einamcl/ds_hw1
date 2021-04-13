import math
def sum(values):
    cur_sum = 0
    for val in values:
        cur_sum += val
    return cur_sum

def mean(values):
    cur_sum = 0
    for val in values:
        cur_sum += val
    return cur_sum / len(values)

def med(values):
    if values%2 == 1:  # odd number
            return values[math.ceil(len(values)/2)]
    else: #even number
        return (values[(len(values)/2)]+values[(len(values)/2)+1])/2


def population_statistics(feature_description, data, treatment, target, threshold, is_above,
                          statistic_functions):
    """"
   :argument: "hum, t1, cnt, season, is_holiday"
   :parameter: None
   :return:
   """