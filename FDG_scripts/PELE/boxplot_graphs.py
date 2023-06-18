import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read csv files
comb_csv = pd.read_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS/KRAS_comb.csv')
x = comb_csv['all_BFE'].tolist()

new = comb_csv["molecule"].str.split("_", n = 2, expand = True)
comb_csv["S4"] = new[0]
comb_csv["S2"] = new[1]
comb_csv["S3"] = new[2]

s4_22 = comb_csv.loc[comb_csv['S4'] == "S4.22", "all_BFE"].tolist()
s4_24 = comb_csv.loc[comb_csv['S4'] == "S4.24", "all_BFE"].tolist()
s4_25 = comb_csv.loc[comb_csv['S4'] == "S4.25", "all_BFE"].tolist()
all_s4 = [s4_22, s4_24, s4_25]

s3_244 = comb_csv.loc[comb_csv['S3'] == "S3.244", "all_BFE"].tolist()
s3_317 = comb_csv.loc[comb_csv['S3'] == "S3.317", "all_BFE"].tolist()
s3_380 = comb_csv.loc[comb_csv['S3'] == "S3.380", "all_BFE"].tolist()
s3_507 = comb_csv.loc[comb_csv['S3'] == "S3.507", "all_BFE"].tolist()
s3_521 = comb_csv.loc[comb_csv['S3'] == "S3.521", "all_BFE"].tolist()
s3_556 = comb_csv.loc[comb_csv['S3'] == "S3.556", "all_BFE"].tolist()
s3_590 = comb_csv.loc[comb_csv['S3'] == "S3.590", "all_BFE"].tolist()
s3_602 = comb_csv.loc[comb_csv['S3'] == "S3.602", "all_BFE"].tolist()
s3_628 = comb_csv.loc[comb_csv['S3'] == "S3.628", "all_BFE"].tolist()
all_s3 = [s3_244, s3_317, s3_380, s3_507, s3_521, s3_556, s3_590, s3_602, s3_628]

s2_26 = comb_csv.loc[comb_csv['S2'] == "S2.26", "all_BFE"].tolist()
s2_88 = comb_csv.loc[comb_csv['S2'] == "S2.88", "all_BFE"].tolist()
s2_90 = comb_csv.loc[comb_csv['S2'] == "S2.90", "all_BFE"].tolist()
s2_149 = comb_csv.loc[comb_csv['S2'] == "S2.149", "all_BFE"].tolist()
s2_180 = comb_csv.loc[comb_csv['S2'] == "S2.180", "all_BFE"].tolist()
s2_307 = comb_csv.loc[comb_csv['S2'] == "S2.307", "all_BFE"].tolist()
s2_350 = comb_csv.loc[comb_csv['S2'] == "S2.350", "all_BFE"].tolist()
all_s2 = [s2_26, s2_88, s2_90, s2_149, s2_180, s2_307, s2_350]


# Boxplots of each subpocket fragment

fig = plt.figure(figsize =(10, 5))
plt.boxplot(all_s4)
plt.title(label = "Boxplot for S4 fragments in the combined ligands")
plt.xticks([1, 2, 3], ['S4_22', 'S4_24', 'S4_25'])
plt.savefig("s4_comb_boxplot.pdf")

fig = plt.figure(figsize =(10, 5))
plt.boxplot(all_s3)
plt.title(label = "Boxplot for S3 fragments in the combined ligands")
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9], ['S3_244', 'S3_317', 'S3_380', 'S3_507', 'S3_521', 'S3_556', 'S3_590', 'S3_602', 'S3_628'])
plt.savefig("s3_comb_boxplot.pdf")

fig = plt.figure(figsize =(10, 5))
plt.boxplot(all_s2)
plt.title(label = "Boxplot for S2 fragments in the combined ligands")
plt.xticks([1, 2, 3, 4, 5, 6, 7], ['S2_26', 'S2_88', 'S2_90', 'S2_149', 'S2_180', 'S2_307', 'S2_350'])
plt.savefig("s2_comb_boxplot.pdf")

# Histogram plots to see distribution of scores

plt.figure()
plt.hist(x, density = False, edgecolor = 'black')
sns.displot(x, kde=True)
plt.title(label = "Histogram of all_BFE scores for the combined ligands")
plt.xlabel("all_BFE")
plt.savefig("histogram_comb_plot.pdf", bbox_inches = 'tight')
