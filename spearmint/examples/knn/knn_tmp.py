from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

def knn_test(n_neighbors):
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target,random_state=0)

    reg = KNeighborsClassifier(n_neighbors=n_neighbors[0])
    reg.fit(X_train, y_train)
    result = reg.score(X_test, y_test)

    print 'Result ={:.2f} '.format(result)
    return (-result)

def main(job_id, params):
    print 'job #%d' %job_id
    print params
    return knn_test(params['n_neighbors'])
