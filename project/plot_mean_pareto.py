import matplotlib.pyplot as plt
import numpy as np

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

dv = plt.scatter(np.mean([.17,.18,.29]), np.mean([0.23,0.2,0.12]), marker='x', color=colors[0])
lr = plt.scatter(np.mean([0.24,0.62,0.47]), np.mean([0.62, 0.77, 0.68]), marker='x', color=colors[1])
smote = plt.scatter(np.mean([0.27, 0.64,0.53]), np.mean([0.54, 0.69, 0.61]), marker='x', color=colors[2]) 
adasyn = plt.scatter(np.mean([0.25, 0.53, 0.52]), np.mean([0.54, 0.62, 0.61]), marker='x', color=colors[3])
ros = plt.scatter(np.mean([0.21, 0.6, 0.53]), np.mean([0.54, 0.69, 0.61]), marker='x', color=colors[4])
border = plt.scatter(np.mean([0.2, 0.57, 0.5]), np.mean([0.46, 0.62, 0.68]), marker='x', color=colors[5])
smotenn = plt.scatter(np.mean([0.24,0.42, 0.4]), np.mean([0.69, 0.77, 0.82]), marker='x', color=colors[6])
smotetomek = plt.scatter(np.mean([0.22, 0.59, 0.48]), np.mean([0.46, 0.77, 0.57]), marker='+', color=colors[0])
cluster = plt.scatter(np.mean([0.08,0.05,0.28]), np.mean([0.92,0.85,0.79]), marker='+', color=colors[1])
conden = plt.scatter(np.mean([0.45,0.41,0.41]), np.mean([0.69,0.69,0.46]), marker='+', color=colors[2])
edited = plt.scatter(np.mean([0.2,0.44,0.35]), np.mean([0.69,0.85,0.64]), marker='+', color=colors[3])
repeated = plt.scatter(np.mean([0.19,0.38,0.34]), np.mean([0.69,0.92,0.75]), marker='+', color=colors[4])
allknn = plt.scatter(np.mean([0.21,0.36,0.34]), np.mean([0.69,0.77,0.68]), marker='+', color=colors[5])
instance = plt.scatter(np.mean([0.12,0.22,0.34]), np.mean([0.77,0.85,0.68]), marker='+', color=colors[6])
nm1 = plt.scatter(np.mean([0.1,0.06,0.32]), np.mean([0.69,0.92,0.64]), marker='1', color=colors[0])
nm2 = plt.scatter(np.mean([0.08,0.05,0.27]), np.mean([0.92,0.92,0.75]), marker='1', color=colors[1])
nm3 = plt.scatter(np.mean([0.12,0.06,0.33]), np.mean([0.92,0.77,0.61]), marker='1', color=colors[2])
neighb = plt.scatter(np.mean([0.21,0.5,0.41]), np.mean([0.69,0.85,0.68]), marker='1', color=colors[3])
one = plt.scatter(np.mean([0.22,0.62,0.53]), np.mean([0.62,0.77,0.64]), marker='1', color=colors[4])
rus = plt.scatter(np.mean([0.19,0.35,0.44]), np.mean([0.69,0.85,0.57]), marker='1', color=colors[5])
tome = plt.scatter(np.mean([0.24,0.62,0.49]), np.mean([0.62,0.77,0.64]), marker='1', color=colors[6])


plt.legend((dv, lr, smote, adasyn, ros, border, smotenn, smotetomek, cluster, conden, edited, 
	repeated, allknn, instance, nm1, nm2, nm3, neighb, one, rus, tome),
           ('Dictionary Vote', 'Logistic Regression', 'LR + SMOTE', 'LR + ADASYN', 'LR + RandomOverSampler',
           	'LR + BordrlineMOTE', 'LR + SMOTENN', 'LR + SMOTETomek', 'LR + ClusterCentroids',
           	'LR + CondendNearestNeighbour', 'LR + EditedNearestNeighbours', 'LR + RepeatedEditedNearestNeighbours',
           	'LR + AllKNN', 'LR + InstanceHardnessThreshold', 'LR + NearMiss1', 'LR + NearMiss2', 'LR + NearMiss3',
           	'LR + NeighbourholdCleaningRule', 'LR + OneSidedSelection', 'LR + RandomUnderSampler', 'LR + TomeLinks'),
           scatterpoints=1,
           loc='lower left',
           ncol=4,
           fontsize=8)

plt.xlabel('Precision', fontsize=18)
plt.ylabel('Recall', fontsize=16)

plt.show()