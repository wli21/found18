import matplotlib.pyplot as plt

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

dv = plt.scatter([.17], [0.23], marker='x', color=colors[0])
lr = plt.scatter([0.24], [0.62], marker='x', color=colors[1])
smote = plt.scatter([0.27], [0.54], marker='x', color=colors[2]) 
adasyn = plt.scatter([0.25], [0.54], marker='x', color=colors[3])
ros = plt.scatter([0.21], [0.54], marker='x', color=colors[4])
border = plt.scatter([0.2], [0.46], marker='x', color=colors[5])
smotenn = plt.scatter([0.24], [0.69], marker='x', color=colors[6])
smotetomek = plt.scatter([0.22], [0.46], marker='+', color=colors[0])
cluster = plt.scatter([0.08], [0.92], marker='+', color=colors[1])
conden = plt.scatter([0.45], [0.69], marker='+', color=colors[2])
edited = plt.scatter([0.2], [0.69], marker='+', color=colors[3])
repeated = plt.scatter([0.19], [0.69], marker='+', color=colors[4])
allknn = plt.scatter([0.21], [0.69], marker='+', color=colors[5])
instance = plt.scatter([0.12], [0.77], marker='+', color=colors[6])
nm1 = plt.scatter([0.1], [0.69], marker='1', color=colors[0])
nm2 = plt.scatter([0.08], [0.92], marker='1', color=colors[1])
nm3 = plt.scatter([0.12], [0.92], marker='1', color=colors[2])
neighb = plt.scatter([0.21], [0.69], marker='1', color=colors[3])
one = plt.scatter([0.22], [0.62], marker='1', color=colors[4])
rus = plt.scatter([0.19], [0.69], marker='1', color=colors[5])
tome = plt.scatter([0.24], [0.62], marker='1', color=colors[6])


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