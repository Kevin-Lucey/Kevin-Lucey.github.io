import pandas as pd

class csv_to_html:
    def __init__(self, path:str):
        data = pd.read_csv(path)
        return data.to_html()
print(csv_to_html("NE10_OPSadjusted.csv"))

