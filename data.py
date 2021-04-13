import pandas as pd



# df = pd.read_csv("C:/Users/einam/Desktop/school/intro_ds/hw1/london.csv")
# data1 = df.to_dict(orient="list")
# print(data1)
# features_we_need = ["hum", "t1", "cnt", "season", "is_holiday"]

def load_data(path, features):
    """
    # receives path to file, requested features from file. Returns dictionaries with keys by given features
    #:argument:
    #:parameter: "hum, t1, cnt, season, is_holiday", path to file
    #:return: data list containing all relevent keys by features.
    """
    df = pd.read_csv(path)
    raw_data = df.to_dict(orient=list)
    data_1 = {}
    for feature in features:
        data_1[feature] = raw_data.get(feature)
    return data_1


def filter_by_features(data, feature, values):
    """
    receives
    list, requested
    features, list
    of
    values.Returns
    dictionaries
    with keys by given features
    :argument: "hum, t1, cnt, season, is_holiday"
    :parameter: None
    :return: 2
    data
    lists
    data1
    contains
    all
    relevant
    keys
    by
    features, data2
    contains
    the
    rest.
"""
    good_features = data.copy()
    bad_features = data.copy()
    for val in values:
        if val in bad_features[feature]:
            bad_features[feature].remove(val)
    good_features[feature].remove(bad_features[feature])
    return good_features, bad_features


def print_details(data, features, statistic_functions):

        print(statistic_functions.sum) print(statistic_functions.mean, ) statistic_functions.mead \n)

        print(statistic_functions(data[feature]))