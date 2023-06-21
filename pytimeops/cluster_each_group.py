import pandas as pd
import sys
sys.path.append('/Users/elnazazizi/Desktop/Schmidt/Software/Bumblebee taste data & papers/turbo-parakeet/')
import pytimeops as pto
from sklearn.cluster import KMeans



def cluster_each_group(filename, feature, method):
    """
    This function gets the dataset and the feature that you want
    to group based on that, applies clustering on each group
    and returns centroids of clusters.
    """
    df = pd.read_csv(filename)
    # Initialize an empty DataFrame to store the centroids
    centroids_df = pd.DataFrame(columns=['group', 'Number', 'centroid'])
    df_selected_columns = df.iloc[:, [feature] + list(range(5, 10))]
    grouped = df_selected_columns.groupby(df_selected_columns.columns[0])
    for group_name, group_df in grouped:
        #print(f"Processing group: {group_name}")
        group_data = group_df.iloc[:, -5:].values
        # Apply K-means clustering
        result = pto.apply_clustering(group_data, 10, method)
        # Create a new DataFrame to store the group name and centroid
        group_centroids_df = pd.DataFrame({'group': [group_name], 'Number':[result[0]], 
                                           'centroid': [result[1:]]})
        centroids_df = centroids_df.append(group_centroids_df, ignore_index=True)
        # Append the group centroids to the main centroids DataFrame
        #group_centroids = pto.apply_clustering(group_data.iloc[:, -5:].values, 3)
        #print(group_centroids)
        #group_centroids = 10
    return centroids_df


A = cluster_each_group('Fig1H-K_SI1G-I.csv', 2, 'calinski_harabasz_score')
print(A)
