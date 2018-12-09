import matplotlib.pyplot as plt

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

dv = plt.scatter([.18], [0.2], marker='x', color=colors[0])
lr = plt.scatter([0.62], [0.77], marker='x', color=colors[1])
smote = plt.scatter([0.64], [0.69], marker='x', color=colors[2]) 
adasyn = plt.scatter([0.53], [0.62], marker='x', color=colors[3])
ros = plt.scatter([0.6], [0.69], marker='x', color=colors[4])
border = plt.scatter([0.57], [0.62], marker='x', color=colors[5])
smotenn = plt.scatter([0.42], [0.77], marker='x', color=colors[6])
smotetomek = plt.scatter([0.59], [0.77], marker='+', color=colors[0])
cluster = plt.scatter([0.05], [0.85], marker='+', color=colors[1])
conden = plt.scatter([0.41], [0.69], marker='+', color=colors[2])
edited = plt.scatter([0.44], [0.85], marker='+', color=colors[3])
repeated = plt.scatter([0.38], [0.92], marker='+', color=colors[4])
allknn = plt.scatter([0.36], [0.77], marker='+', color=colors[5])
instance = plt.scatter([0.22], [0.85], marker='+', color=colors[6])
nm1 = plt.scatter([0.06], [0.92], marker='1', color=colors[0])
nm2 = plt.scatter([0.05], [0.92], marker='1', color=colors[1])
nm3 = plt.scatter([0.06], [0.77], marker='1', color=colors[2])
neighb = plt.scatter([0.5], [0.85], marker='1', color=colors[3])
one = plt.scatter([0.62], [0.77], marker='1', color=colors[4])
rus = plt.scatter([0.35], [0.85], marker='1', color=colors[5])
tome = plt.scatter([0.62], [0.77], marker='1', color=colors[6])


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