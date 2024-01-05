import pandas

class DataWriter:
    info: dict

    def __init__(self):
        df1 = None
    @staticmethod
    def writeParams(info):
        df = pandas.DataFrame(info)
        df.to_csv("myInfo.csv", index=False)

