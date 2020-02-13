import sys
import pandas
import os
import time

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../hybrid_intrusion_detection_classifier")
from dataSet import DataSet

class DecisionTreeClassifier(object):
	#conjunto de dados de treino
	data_set = None
	#conjunto de dados de teste
	test_data_set = None
	
	decision_tree = None
	predictions = None
	
	#iteracao do processo de cross-validation
	iteration = 0

	training_time = 0
	test_time = 0
	class_name = ""
	#pasta para serem salvos os arquivos de resultados, variavel pode ser setada no arquivo main.py
	result_path = ""

	def __init__(self):
		print ("aa")

	def run(self):
		training_time_start = time.time()
		print("RUN DECISION TREE classifier")
		self.decision_tree.setDataSet(self.data_set)
		self.decision_tree.setTestDataSet(self.test_data_set)
		
		#funcao para gerar o modelo e treina-lo
		self.decision_tree.generateModel()

		self.training_time = time.time() - training_time_start

		test_time_start = time.time()
		#funcao para realizar a classificacao dos exemplos
		self.predictions = self.decision_tree.predictClasses()
		self.test_time = time.time() - test_time_start
		self.saveResults()

	#salva os resultados das classificacoes na pasta definida no arquivo main.py
	def saveResults(self):
		for i in range(0,len(self.predictions)):
			self.test_data_set.set_value(i, self.class_name,self.predictions[i])

		DataSet.saveResults(self.result_path, self.iteration, self.test_data_set)	

	def setDataSet(self, data_set):
		self.data_set = data_set

	def getDataSet(self):
		return self.data_set

	def setTestDataSet(self, test_data_set):
		self.test_data_set = test_data_set

	def getTestDataSet(self):
		return self.test_data_set

	def setDecisionTree(self, decision_tree):
		self.decision_tree = decision_tree

	def getDecisionTree(self):
		return self.decision_tree

	def setIteration(self, iteration):
		self.iteration = iteration

	def setResultPath(self, result_path):
            self.result_path = result_path

	def getTrainingTime(self):
		return self.training_time

	def getTestTime(self):
		return self.test_time

	def setClass_name(self, class_name):
		self.class_name = class_name