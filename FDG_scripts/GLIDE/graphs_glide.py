import pandas as pd
import glob
import os
from statistics import mean
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from scipy import stats
import numpy as np

file_csv = '/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/7RPZ_prep_unique_output_S2_prep_pv_sorted.csv'
df = pd.read_csv(file_csv, sep=",")

df.replace("", "NaN", inplace=True)
df.dropna(how='all', axis=1, inplace=True)

df.to_csv('/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/7RPZ_prep_unique_output_S2_prep_pv_sorted_without_null.csv', index = None, header=True, sep=',', encoding='utf-8-sig')

df = pd.read_csv(file_csv, sep=",")

# To remove the last line of the file which corresponds to the protein
file_path = '/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/7RPZ_prep_unique_output_S2_prep_pv_sorted_without_null.csv'
os.system('sed -i "$ d" {0}'.format(file_path))


# mapping ligbuilder names with the glide titles

df_ligbuilder = pd.read_csv("/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/ligbuilder_S2/INDEX", names = ["Path", "Chemical_Formula", "Molecular_Weight", "LogP", "Binding_Score", "Structure_Score", "Synthesize_Score", "Chemical_Score"], delimiter = "\t")

names = []
for i,row in df_ligbuilder.iterrows():
    names.append(os.path.basename(row["Path"]).replace(".mol2", ""))
df_ligbuilder["Names"] = names


mapping = {}
for files in glob.glob("/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/ligbuilder_S2/*.mol2"):
    ligbuilder_name = os.path.basename(files).replace(".mol2", "")

    lines = [line for line in open(files, "r")]

    for i,line in enumerate(lines):
        if "<TRIPOS>MOLECULE" in line:
            glide_name = lines[i+1].replace("\n", "")
            ligbuilder_score = float(df_ligbuilder[df_ligbuilder["Names"] == ligbuilder_name]["Binding_Score"])
            mapping[glide_name] = (ligbuilder_name, ligbuilder_score)

df_glide = pd.read_csv('/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/7RPZ_prep_unique_output_S2_prep_pv_sorted_without_null.csv', sep=',')

adjust_scores = []
scoring_dict = {}
for i,row in df_glide.iterrows():
    glide_name = row["Title"]
    glide_names = glide_name.split(",")
    adjust_values = []

    for name in glide_names:
        if name == "No" or name == "No_0":
            continue
        adjust_values.append(mapping[name][1])
    adjust_value = max(adjust_values)

    if glide_name not in scoring_dict.keys():
        scoring_dict[glide_name] =([row["XP GScore"]], adjust_value)
    else:
        scoring_dict[glide_name][0].append(row["XP GScore"])

scoring_dict = {key:(value[0][0],value[1]) for key,value in scoring_dict.items()}

x = []
y = []
z = []

for value in scoring_dict.values():
    x.append(value[0])
    y.append(value[1])

for key in scoring_dict.keys():
    z.append(key)

correlation = pearsonr(x, y)
print(correlation)

# Scatterplot for the correlation between glide and LigBuilder
plt.figure()
fig, ax = plt.subplots(figsize=(10, 5))
sns.regplot(x = x, y = y, label = "$R^2$ = %.3f"%correlation[0], ci = None)
plt.xlabel("Glide gScore")
plt.ylabel("LigBuilder Adjust Score")
plt.legend()
plt.savefig("correlation_plot.pdf")

# Identifying outliers
data = {'x':x, 'y':y, 'glide':z}
x_1 = pd.DataFrame(data, columns = ['x', 'y', 'glide'])
f = open('df_scatter','w')
print(x_1.to_string(), file=f)

'''Glide (x) outliers'''
# IQR for glide (x)
Q1 = np.percentile(x_1["x"], 25,method = 'midpoint')
Q3 = np.percentile(x_1["x"], 75, method = 'midpoint')
IQR = Q3 - Q1

# Upper bound for glide (x)
upper = Q3 + 1.5 * IQR
upper_array = np.array(x_1["x"] >= upper)
upper_outliers_x = x_1["x"][upper_array]

# Lower bound for glide (x)
lower = Q1 - 1.5 * IQR
lower_array = np.array(x_1["x"] <= lower)
lower_outliers_x = x_1["x"][lower_array]

'''LigBuilder (y) outliers'''
# IQR for LigBuilder (y)
Q1 = np.percentile(x_1["y"], 25,method = 'midpoint')
Q3 = np.percentile(x_1["y"], 75, method = 'midpoint')
IQR = Q3 - Q1

# Upper bound for LigBuilder (y)
upper = Q3 + 1.5 * IQR
upper_array = np.array(x_1["y"] >= upper)
upper_outliers_y = x_1["y"][upper_array]

# Lower bound for LigBuilder (y)
lower = Q1 - 1.5 * IQR
lower_array = np.array(x_1["y"] <= lower)
lower_outliers_y = x_1["y"][lower_array]

print(upper_outliers_x)
print(lower_outliers_x)
print(upper_outliers_y)
print(lower_outliers_y)

'''Remove the outliers from the dataframe'''
x_2 = x_1.drop(x_1.index[75])
x_3 = x_2.drop(x_2.index[103])

f = open('df_scatter_dropped','w')
print(x_3.to_string(), file=f)

# Scatterplot without outliers
correlation_1 = pearsonr(x_3["x"], x_3["y"])
print(correlation_1)

plt.figure()
fig, ax = plt.subplots(figsize=(10, 5))
sns.regplot(x = x_3["x"], y = x_3["y"], label = "$R^2$ = %.3f"%correlation_1[0], ci = None)
plt.xlabel("Glide gScore")
plt.ylabel("LigBuilder Adjust Score")
plt.legend()
plt.savefig("correlation_plot_clean.pdf")


# Histogram plots to see distribution of scores
plt.figure()
plt.hist(x, density = False, edgecolor = 'black')
sns.displot(x, kde=True)
plt.axvline(x = -12.270, color = 'red', label = 'mirati gscore')
plt.title(label = "Histogram of the glide scores for the S2 subpocket ligands")
plt.xlabel("Glide gScore")
plt.savefig("histogram_glide_plot.pdf", bbox_inches = 'tight')

plt.figure()
plt.hist(y, density = False, edgecolor = 'black')
sns.displot(y, kde=True)
plt.title(label = "Histogram of the LigBuilder Adjust Score for the S2 subpocket ligands")
plt.xlabel("LigBuilder Adjust Score")
plt.savefig("histogram_ligbuilder_plot.pdf", bbox_inches = 'tight')

