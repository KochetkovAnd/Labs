import random
import time
from math import *
import os
from time import sleep

N = 5 # Количество в функции 
trainSize = 30
testSize = 10
lr = 0.05
epochs = 200000
Errmax = 0.75
CBiasNeuron = 1
CInitWeight = 0

file1 = "weight.txt" # Название файла под сохранение весов
file2 = "train.txt" # Название файла под забор значений для тренировки
file3 = "predict.txt" # Название файла под сохраниние рузультатов


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
    def __init__(self):
        self.weights = []   
        for i in range (N + 1):
            self.weights.append((random.random()*2 - 1)* CInitWeight)

    def train(self, trainInputs, trainOutputs, lr, epoсhsMax, errMin):
        epoсhs, err = 0, errMin * 2 

        while epoсhs < epoсhsMax and err > errMin:
            err = 0
            epoсhs += 1
            for i in range(len(trainInputs)):

                predictOutput = sigmoid(multi(trainInputs[i], self.weights))

                delta = trainOutputs[i] - predictOutput
                err += delta ** 2 / 2

                self.weights[0] += lr * CBiasNeuron * delta
                for j in range(len(trainInputs[i])):
                    self.weights[j + 1] += lr * trainInputs[i][j] * delta

        return epoсhs, err

    def trainFromFile(self, filename, lr, epoсhsMax, errMin):

        f = open(filename, 'r')
        inputs = []
        outputs = []
        for line in f:
            if line[-1: ] == '\n':
                line = line[: -1]
                line = line.split(' ')
                temp = []
                for i in range(N):
                    temp.append(int(line[1]))
                inputs.append(temp)
                outputs.append(int(line[N]))
        f.close()

        return self.train(inputs, outputs, lr, epoсhsMax, errMin)   

    def predict(self, inputs, filename):

        predictOutputs = []

        for i in range(len(inputs)):
            predictOutputs.append(sigmoid(multi(inputs[i], self.weights)))

        f = open(filename, 'w')
        for i in range(len(predictOutputs)):
            f.write(str(predictOutputs[i]) +"\n")

        return predictOutputs

    def saveWeight(self, filename):

        f = open(filename, 'w')
        for i in range (len(self.weights)):
            s ="weight" + str(i) + " = " +  str(self.weights[i]) + "\n" 
            f.write(s)
        f.close()

key = True

perceptron =  Perceptron()
while key:
    print("Выполнил: Кочетков А В гр 6315  функция: a and b or not c and d or not e ")
    print("Для создания (пересоздания) перцептрона                введите 1")
    print("Для тренировки с помощью данных из выборки             введите 2")
    print("Для тренировки с помощью данных из файла train.txt     введите 3")
    print("Для получения предсказания из выборки                  введите 4")
    print("Для сохранения весов в файл weight.txt                 введите 5")
    print("Для выхода                                             введите 6")

    command = input("Введите комманду:")

    if command == "1":
        perceptron = Perceptron()
        print("Перцептрон создан (пересоздан)")
        sleep(2)
    elif command == "2":
        training_inputs, training_outputs  = getSelection(trainSize)

        startTime = time.time()
        epohs, err = perceptron.train(training_inputs, training_outputs, lr, epochs, Errmax)
        trainTime = time.time() - startTime
        
        print("============================================================================================")
        print("                                 PERCEPTRON обучен                                          ")
        print("Эпоха:", epohs) 
        print("Ошибка:", err) 
        print("Время обучения:", trainTime)
        print("============================================================================================")
        sleep(2)

    elif command == "3":

        startTime = time.time()
        epohs, err = perceptron.trainFromFile(file2, lr, epochs, Errmax)
        trainTime = time.time() - startTime
        
        print("============================================================================================")
        print("                                 PERCEPTRON обучен                                          ")
        print("Эпоха:", epohs) 
        print("Ошибка:", err) 
        print("Время обучения:", trainTime)
        print("============================================================================================")
        sleep(2)

    elif command == "4":
        test_inputs, test_outputs  = getSelection(testSize)
        predict_outputs = perceptron.predict(test_inputs, file3)
        print("Задача              ОТВЕТ              ВЕРНЫЙ ОТВЕТ")
        for i in range(len(test_inputs)):
            print(test_inputs[i][0], test_inputs[i][1], test_inputs[i][2], test_inputs[i][3], test_inputs[i][4],"          %.6f          " % (predict_outputs[i]), test_outputs[i])
        sleep(2)

    elif command == "5":
        perceptron.saveWeight(file1)
        sleep(2)
    
    elif command == "6":
        key = False
        sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear')

    
