import numpy as np
import kmeansclustering as kmc
import itertools as it

data = np.array([7845, 778, 942, 143, 0.75,
                 7956, 810, 976, 146, 0.76,
                 8215, 825, 1002, 152, 0.78,
                 8542, 847, 1038, 157, 0.78,
                 8150, 100587, 807, 1015, 150,
                 0.72, 8386, 884, 101964, 1085,
                 138, 0.82, 8219, 827, 995,
                 158, 0.82, 7500, 745, 948,
                 135, 0.67, 9257, 901, 120967,
                 1154, 148, 0.72, 8553, 811,
                 1218, 175, 0.84])

k = kmc.KMeansClustering(data, 6)
result = k.execute()

for r in result:
    print("Value: {}, Centroid: {}".format(r.value, r.get_centroid().get_value()))
