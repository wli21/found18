import matplotlib.pyplot as plt

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

dv = plt.scatter([.29], [0.12], marker='x', color=colors[0])
lr = plt.scatter([0.47], [0.68], marker='x', color=colors[1])
smote = plt.scatter([0.53], [0.61], marker='x', color=colors[2]) 
adasyn = plt.scatter([0.52], [0.61], marker='x', color=colors[3])
ros = plt.scatter([ 0.53], [0.61], marker='x', color=colors[4])
border = plt.scatter([0.5], [0.68], marker='x', color=colors[5])
smotenn = plt.scatter([0.4], [0.82], marker='x', color=colors[6])
smotetomek = plt.scatter([0.48], [0.57], marker='+', color=colors[0])
cluster = plt.scatter([0.28], [0.79], marker='+', color=colors[1])
conden = plt.scatter([0.41], [0.46], marker='+', color=colors[2])
edited = plt.scatter([0.35], [0.64], marker='+', color=colors[3])
repeated = plt.scatter([0.34], [0.75], marker='+', color=colors[4])
allknn = plt.scatter([0.34], [0.68], marker='+', color=colors[5])
instance = plt.scatter([0.34], [0.68], marker='+', color=colors[6])
nm1 = plt.scatter([0.32], [0.64], marker='1', color=colors[0])
nm2 = plt.scatter([0.27], [0.75], marker='1', color=colors[1])
nm3 = plt.scatter([0.33], [0.61], marker='1', color=colors[2])
neighb = plt.scatter([0.41], [0.68], marker='1', color=colors[3])
one = plt.scatter([0.53], [0.64], marker='1', color=colors[4])
rus = plt.scatter([0.44], [0.57], marker='1', color=colors[5])
tome = plt.scatter([0.49], [0.64], marker='1', color=colors[6])


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