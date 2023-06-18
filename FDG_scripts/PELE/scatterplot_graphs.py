import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Read all summary csv
df_s2_csv = pd.read_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS/KRAS_s2.csv')
df_s3_csv = pd.read_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS/KRAS_s3.csv')
df_s4_csv = pd.read_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS/KRAS_s4.csv')
df_comb_csv = pd.read_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS/KRAS_comb.csv')


'''Generate scatterplots for each subpocket'''

# Retrieve glide gscore and binding free energy columns
s2_x = df_s2_csv['glidegscore'].tolist()
s2_y = df_s2_csv['all_BFE'].tolist()

s3_x = df_s3_csv['glidegscore'].tolist()
s3_y = df_s3_csv['all_BFE'].tolist()

s4_x = df_s4_csv['glidegscore'].tolist()
s4_y = df_s4_csv['all_BFE'].tolist()

comb_x = df_comb_csv['glidegscore'].tolist()
comb_y = df_comb_csv['all_BFE'].tolist()

# Correlation values
s2_correlation = pearsonr(s2_x, s2_y)
s3_correlation = pearsonr(s3_x, s3_y)
s4_correlation = pearsonr(s4_x, s4_y)
comb_correlation = pearsonr(comb_x, comb_y)

# Horizontal line to represent mirati
mirati_X = pd.read_csv('/gpfs/projects/bsc72/bsc72876/PELE_KRAS/KRAS_x_pelemetrics.csv')
hor_X = mirati_X['all_BFE'].tolist()

# Design scatterplots
plt.figure()
fig, ax = plt.subplots(figsize=(10, 5))
sns.regplot(x = s2_x, y = s2_y, label = "$R^2$ = %.3f"%s2_correlation[0], ci = None)
plt.axhline(y = hor_X, color = 'g', linestyle = '-', label = 'mirati BFE x-ray')
plt.xlabel("glide gscore")
plt.ylabel("binding free energy")
plt.legend()
plt.savefig("S2_scatterplot.pdf")

plt.figure()
fig, ax = plt.subplots(figsize=(10, 5))
sns.regplot(x = s3_x, y = s3_y, label = "$R^2$ = %.3f"%s3_correlation[0], ci = None)
plt.axhline(y = hor_X, color = 'g', linestyle = '-', label = 'mirati BFE x-ray')
plt.xlabel("glide gscore")
plt.ylabel("binding free energy")
plt.legend()
plt.savefig("S3_scatterplot.pdf")

plt.figure()
fig, ax = plt.subplots(figsize=(10, 5))
sns.regplot(x = s4_x, y = s4_y, label = "$R^2$ = %.3f"%s4_correlation[0], ci = None)
plt.axhline(y = hor_X, color = 'g', linestyle = '-', label = 'mirati BFE x-ray')
plt.xlabel("glide gscore")
plt.ylabel("binding free energy")
plt.legend()
plt.savefig("S4_scatterplot.pdf")

plt.figure()
fig, ax = plt.subplots(figsize=(10, 5))
sns.regplot(x = comb_x, y = comb_y, label = "$R^2$ = %.3f"%comb_correlation[0], ci = None)
plt.axhline(y = hor_X, color = 'g', linestyle = '-', label = 'mirati BFE x-ray')
plt.xlabel("glide gscore")
plt.ylabel("binding free energy")
plt.legend()
plt.savefig("comb_scatterplot.pdf") 
