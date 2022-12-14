# -*- coding: utf-8 -*-
"""Met.Desicion Tree_1207030007_Bianca Khalfianisa

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yiwnzoTTR-KuYwhuxenA8Q-Z1zbBenQk
"""

from sklearn.neighbors import NearestCentroid

# Database: Gerbang logika AND
# x = Data, Y = Target
x = [[0,0], [0,1], [1,0], [1,1], [0,2], [2,0], [1,2], [2,1], [0,3], [3,0]]
y = [0,2,0,3,1,0,4,2,0,1]

#Training and Classify 
clf = NearestCentroid()
clf = clf.fit(x, y)

#Prediksi
print ("Logika AND Metode K. Nearest Neighbors (KN)")
print ("Logika = Prediksi")
print ("0 0 =", clf.predict([[0,0]]))
print ("0 1 =", clf.predict([[0,1]]))
print ("1 0 =", clf.predict([[1,0]]))
print ("1 1 =", clf.predict([[1,1]]))
print ("0 2 =", clf.predict([[0,2]]))
print ("2 0 =", clf.predict([[2,0]]))
print ("1 2 =", clf.predict([[1,2]]))
print ("2 1 =", clf.predict([[2,1]]))
print ("0 3 =", clf.predict([[0,3]]))
print ("3 0 =", clf.predict([[3,0]]))