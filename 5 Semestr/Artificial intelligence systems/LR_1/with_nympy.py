import numpy as np
import random
import time

N = 3
trainSize = 8
testSize = 6
lr = 0.5
epochs = 200000
Errmax = 0.0001

def fn(a, b, c):
    if (not a and not b or c):
        return 1
    return 0

def getSelection(count):
    res = []  
    for a in range (2):
        for b in range (2):
            for c in range (2):
                res.append([a, b, c, fn(a, b, c)])

    mas = random.sample(res, count)
    X = []
    Y = []
    for i in range (count):
        t = mas[i]
        X.append(t[: -1])
        Y.append(t[-1]) 
    return X, Y

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def train(training_inputs, training_outputs, epochs, lr):

    synaptic_weight = 2 * np.random.random((N, 1)) - 1
    
    i = 0
    errsum = Errmax * 2

    while i < epochs and errsum > Errmax:
        outputs = sigmoid(np.dot(training_inputs, synaptic_weight))
        err = training_outputs - outputs        
        delta = np.dot(training_inputs.T, err * (outputs * (1 - outputs)) * lr)
        synaptic_weight += delta

        errsum = err.sum()
        i += 1

    return synaptic_weight

def printPredict(inputs, outputs, weights):
    predict_outputs = sigmoid(np.dot(inputs, weights))
    print("Полученные веса")
    print(weights)
    print("Предсказанные результаты")
    print(predict_outputs)
    print("Реальные результаты")
    print(outputs)



training_inputs, training_outputs  = getSelection(trainSize)
training_inputs = np.array(training_inputs)
training_outputs = np.array([training_outputs]).T

start_time = time.time()
weights = train(training_inputs, training_outputs, epochs, lr)
print("Время обучения:", time.time() - start_time)

test_inputs, test_outputs  = getSelection(testSize)
test_inputs = np.array(test_inputs)
test_outputs = np.array([test_outputs]).T

printPredict(test_inputs, test_outputs, weights)