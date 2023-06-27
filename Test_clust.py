import pytimeops as pto
import matplotlib.pyplot as plt

Dataset =  pto.read_file('Data/Fig1H-K_SI1G-I.csv', 100)
#A = cluster_each_group('Fig1H-K_SI1G-I.csv', 2, 'silhouette')
A = Dataset.cluster_each_group(['sugar', 'concentration'], 'silhouette', grn_idx = 0)
#print(B[0][1][:])
r = 0
c = 0
fig, axs = plt.subplots(2, 2)
#fig.subplots_adjust(bottom=0.85)
for j in range(17,21):
    B  = A.iloc[j]['centroid']

    for i in range(A.iloc[j]['Number']):

        axs[r, c].plot(B[0][i][:], label=f'Cluster {i+1}')
        axs[r, c].set_title(A.iloc[j]['group'])
        axs[r, c].legend(loc='upper right')
        
    c = c + 1
    if c == 2:
        axs[r, c-2].set_ylabel('Spikes/sec')
        c = 0
        r = r + 1
axs[1, 0].set_xlabel('Bin')
axs[1, 1].set_xlabel('Bin')
plt.show()