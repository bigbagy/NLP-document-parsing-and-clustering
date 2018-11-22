from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
def pca(vec_df,n):

	scaled_df = StandardScaler().fit_transform(vec_df)
	pca = PCA(n_components=n) # reduce dimension to n
	pca_df = pca.fit_transform(scaled_df)

	return (pca_df)

