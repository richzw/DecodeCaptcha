
>>> import sklearn.svm
>>> clf = sklearn.svm.SVC()
>>> data = [(1,1), (1,0), (0,1), (0,0)]
>>> targets = [0,1,1,0]
>>> clf.fit(data, targets)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0,
  kernel='rbf', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False)
>>> clf.predict((0,0))[0]
0
