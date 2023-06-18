import pandas as pd


#table s2
table_s2 = pd.read_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_S2/table_S2.csv')

table_s2["Title"] = table_s2["Title"].str.replace(',','_')

table_s2.to_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_S2/table_S2_prep.csv')

#table s3
table_s3 = pd.read_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_S3/table_S3.csv')

table_s3["Title"] = table_s3["Title"].str.replace(',','_')

table_s3.to_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_S3/table_S3_prep.csv')


#table s4
table_s4 = pd.read_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_S4/table_S4.csv')

table_s4["Title"] = table_s4["Title"].str.replace(',','_')

table_s4.to_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS_2/KRAS_S4/table_S4_prep.csv')
