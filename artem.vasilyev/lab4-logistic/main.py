import numpy as np
import learning
import random

positiveLabel = learning.positiveLabel
negativeLabel = learning.negativeLabel

data = "../common/cancer/wdbc.data"

def main():
    X, Y = load_data()

    classifier, iters, error, (precision, recall, f1) = learning.learn(X, Y)

    print("Best C: {0}".format(iters))
    print("Test set error: {0}".format(error))
    print("Precision: {0}".format(precision))
    print("Recall: {0}".format(recall))
    print("F1 score: {0}".format(f1))


def load_data():
    xs, ys = [], []
    lines = []
    for line in open(data, "r"):
        lines.append(line)

    random.shuffle(lines)
    for line in lines:
        tokens = line.split(",")
        y = positiveLabel if tokens[1] == 'M' else negativeLabel
        x = np.array(list(map(float, tokens[2:])))
        xs.append(x)
        ys.append(y)

    return xs, ys


main()