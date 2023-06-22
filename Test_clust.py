import pytimeops as pto
import matplotlib.pyplot as plt

Dataset =  pto.read_file('Data/Fig1H-K_SI1G-I.csv', 100)
#A = cluster_each_group('Fig1H-K_SI1G-I.csv', 2, 'silhouette')
A = Dataset.cluster_each_group(['sugar','concentration'],'silhouette', grn_idx = 0)
#print(B[0][1][:])
r = 0
c = 0
fig, axs = plt.subplots(3,4)
for j in range(12):
    B  = A.iloc[j]['centroid']
    for i in range(A.iloc[0]['Number']):
        print(j)
        axs[r,c].plot(B[0][i][:])
        axs[r,c].set_title(A.iloc[j]['group'])
    c = c + 1
    if c == 4:
        c = 0
        r = r + 1


plt.show()