import random
import time
from math import *

N = 3
trainSize = 30
testSize = 10
lr = 0.05
epochs = 200000
Errmax = 0.75
CBiasNeuron = 1
CInitWeight = 0
filename = "weight.txt"

def fn(a, b, c, d, e):
    if (a and b or not c and d or not e):
        return 1
    return 0

def getSelection(count):
    res = []  
    for a in range (2):
        for b in range (2):
            for c in range (2):
                for d in range (2):
                    for e in range (2):
                        res.append([a, b, c, d, e, fn(a,b,c,d,e)])
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

class Perceptron:
    def __init__(self, trainInputs, trainOutputs):
        self.trainInputs = trainInputs
        self.trainOutputs = trainOutputs

        self.weights = []   
        for i in range (len(trainInputs[0]) + 1):
            self.weights.append((random.random()*2 - 1)* CInitWeight)

    def train(self, lr, epoсhsMax, errMin):
        epoсhs, err = 0, errMin * 2 

        while epoсhs < epoсhsMax and err > errMin:
            err = 0
            epoсhs += 1
            for i in range(len(self.trainInputs)):

                predictOutput = sigmoid(multi(self.trainInputs[i], self.weights))

                delta = self.trainOutputs[i] - predictOutput
                err += delta ** 2 / 2

                self.weights[0] += lr * CBiasNeuron * delta
                for j in range(len(self.trainInputs[i])):
                    self.weights[j + 1] += lr * self.trainInputs[i][j] * delta

        return epoсhs, err

    def predict(self, inputs):

        predictOutputs = []

        for i in range(len(inputs)):
            predictOutputs.append(sigmoid(multi(inputs[i], self.weights)))

        return predictOutputs

    def saveWeight(self, filename):

        f = open(filename, 'w')
        for i in range (len(self.weights)):
            s ="weight" + str(i) + " = " +  str(self.weights[i]) + "\n" 
            f.write(s)
        f.close()



training_inputs, training_outputs  = getSelection(trainSize)

perceptron = Perceptron(training_inputs, training_outputs)


startTime = time.time()
epohs, err = perceptron.train(lr,epochs, Errmax)
trainTime = time.time() - startTime
print("Выполнил: Кочетков А В гр 6315  функция: a and b or not c and d or not e ")
print("============================================================================================")
print("                                        PERCEPTRON                                          ")
print("Эпоха:", epohs) 
print("Ошибка:", err) 
print("Время обучения:", trainTime)
print("============================================================================================")

test_inputs, test_outputs  = getSelection(testSize)

predict_outputs = perceptron.predict(test_inputs)
print("Задача              ОТВЕТ              ВЕРНЫЙ ОТВЕТ")
for i in range(len(test_inputs)):
    print(test_inputs[i][0], test_inputs[i][1], test_inputs[i][2], test_inputs[i][3], test_inputs[i][4],"          %.6f          " % (predict_outputs[i]), test_outputs[i])

perceptron.saveWeight(filename)


    
