import random
import time
from math import *


N = 3
trainSize = 16
testSize = 10
lr = 0.001
epochs = 200000
Errmax = 0.00001
CBiasNeuron = 1

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

def fn2(a, b, c, d, e):
    if (a and b or not c and d or not e):
        return 1
    return 0

def getSelection2(count):
    res = []  
    for a in range (2):
        for b in range (2):
            for c in range (2):
                for d in range (2):
                    for e in range (2):
                        res.append([a, b, c, d, e, fn2(a,b,c,d,e)])

    mas = random.sample(res, count)
    X = []
    Y = []
    for i in range (count):
        t = mas[i]
        X.append(t[: -1])
        Y.append(t[-1]) 
    return X, Y

def multi(x, W):
    sum = CBiasNeuron * W[0]
    for i in range(len(x)):
        sum += (x[i] * W[i + 1])
    return sum

def sigmoid(x):
    return 1 / (1 + exp(-x))

def train(training_inputs, training_outputs, epochs, lr):

    weights = []
    for i in range (len(training_inputs[0]) + 1):
        weights.append(random.random()*2 - 1)

   
    j = 0
    errsum = Errmax * 2

    while j < epochs and errsum > Errmax:

        for i in  range (len(training_inputs)):

            outputsPredict = sigmoid(multi(training_inputs[i], weights))

            delta = training_outputs[i] - outputsPredict

            errsum += delta ** 2 / 2

            weights[0] += lr * CBiasNeuron * delta

            for g in range(len(training_inputs[i])):
                weights[g + 1] += lr * training_inputs[i][g] * delta
            
        j += 1

    return weights

def printPredict(inputs, outputs, weights):
    
    print("-----------------------")
    for i in range(len(inputs)):
        predict_outputs = sigmoid(multi(inputs[i], weights))
        print(inputs[i], outputs[i], predict_outputs)

training_inputs, training_outputs  = getSelection2(trainSize)

weights = train(training_inputs, training_outputs, epochs, lr)

test_inputs, test_outputs  = getSelection2(testSize)

printPredict(test_inputs, test_outputs, weights)