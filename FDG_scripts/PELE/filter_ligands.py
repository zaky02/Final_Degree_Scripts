import pandas as pd


# read csv files 
s4_csv = pd.read_csv("/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_s4.csv")
s3_csv = pd.read_csv("/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_s3.csv")
s2_csv = pd.read_csv("/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_s2.csv")


# filter ligands by threshold
x_csv = pd.read_csv("/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_x.csv")
threshold = float(x_csv["all_BFE"])
print(threshold) #-90.8071

s4_csv_filtered = s4_csv.loc[s4_csv["all_BFE"] < -90.8071]
s4_csv_filtered.to_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_s4_filtered.csv')

s3_csv_filtered = s3_csv.loc[s3_csv["all_BFE"] < -90.8071]
s3_csv_filtered.to_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_s3_filtered.csv')

s2_csv_filtered = s2_csv.loc[s2_csv["all_BFE"] < -90.8071]
s2_csv_filtered.to_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_s2_filtered.csv')
