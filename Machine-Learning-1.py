from sklearn import tree

# 1 = medium shirt
# 2 = Large shirt
# The first number's in features_of_shirts = inches

features_of_shirts = [38, 2], [44, 2], [38, 1], [44, 1]
shirts = [2, 2, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_of_shirts, shirts)
print(clf.predict([[44, 2]]))


# Output = 2
