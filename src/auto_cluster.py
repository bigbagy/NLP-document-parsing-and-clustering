from sklearn.cluster import KMeans
import numpy as np


def find_optimum_k(df):	

###################################################################
#first we need to find the optimum k value, using elbow method:

#if we plot model-error vs k, the plot is elbow-shaped

#when k is too small, the model is underfit, increasing k will give large error reduction, the slope is large

#when k becomes too large, the model is overfit, increasing k will fit to random noise, and give minor error reduction, the slope is small

#optimum k is found when slope is smaller than a certain threshold


	optimum_k=1	#initialize optimum_k
	kmeans = KMeans(n_clusters=1, random_state=0).fit(df)	#initialize model using k=1
	max_error=kmeans.inertia_	#initialize k=1 clustering error (using kmeans.inertia_)
	old_error=max_error	#initialize k=1 error
	slope=1		#rate of error reduction with increasing k

	kmax=df.shape[0]	#max cluster number is total no. of documents	

	k=2	#start iteration using k=2
	while k<kmax and slope>0.1:	# stop if slope<10%, or k reach kmax
		kmeans = KMeans(n_clusters=k, random_state=0).fit(df)	#fit model using k
		new_error=kmeans.inertia_
		slope = (old_error - new_error) / max_error	# % improved
		old_error=new_error	#update for next iteration
		k+=1	#update for next iteration


	return (k)

###################################################################
#fit model using optimum k

def kmeans(df,k):	
	kmeans = KMeans(n_clusters=k, random_state=0).fit(df)	#fit model using k
	print (kmeans.labels_)

	cluster_label=kmeans.predict(df)

	print (cluster_label)

#	print ( kmeans.cluster_centers_)
	return (cluster_label)


