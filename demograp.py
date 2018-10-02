import pandas as pd
from matplotlib import pyplot as plt
sample_data=pd.read_csv("odidata.csv")
print("{}    {} ".format(sample_data.Truns,sample_data.StrikeRate))
