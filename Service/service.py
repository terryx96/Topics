import pandas as pd

class Service():

    courses = pd.DataFrame()
    students = pd.DataFrame()

    def import_data(self):
        df = pd.read_csv() # Will need to be a GUI function after flask implementation
        self.courses = df.iloc[:,0:7]
        self.students = df.iloc[:,7:]