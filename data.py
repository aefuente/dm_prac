import pandas as pd

class data(object):
    def __init__(self, train_csv, test_csv, columns):
        self.train_x = pd.read_csv(train_csv, skipinitialspace=True,skiprows=1)
        self.test_x = pd.read_csv(test_csv, skipinitialspace=True, skiprows=1)
        self.train_x.columns = columns
        self.test_x.columns = columns
        self.train_y = None
        self.test_y = None


