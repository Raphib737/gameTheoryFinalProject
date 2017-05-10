from board import *
from player import *
import numpy as np
import matplotlib.pyplot as plt

def main():
	t4t = T4Tplayer();
	cp  =	Cplayer();
	dp  = Dplayer();
	rp = Randomplayer();
	hp = halfplayer();
	shp = smartHalfPlayer();
	rt4t = reversedT4Tplayer();
	mp = majorityPlayer();
	minP = minorityPlayer();

	players = [cp,t4t,rp,hp,shp,rt4t,dp,mp,minP]

	roundRobinGame(players)
	for player in players:
		print(player)

	keys = list(set(players[0].logistics.keys()) | set(players[1].logistics.keys()))
	data = [[]]
	
	xLabels = []
	currIndex = 0
	
	#yAxis = 'wins'
	#yAxis = "ties"
	yAxis = 'loss'

	
	
	for key in keys:
		for player in players:
			if player.name not in xLabels:
				xLabels.append(player.name);
			if key == player.name:
				data[currIndex].append(0);
			else:
				data[currIndex].append(player.logistics[key][yAxis])
		data.append([]);
		currIndex +=1

	del data[-1]

	N = len(players)

	ind = np.arange(N)
	width = .25

	color = ['#0abab5',"#f4e8d9","#dfa855","#1e1e1e","#e70000","#965660",
					 "#bd3b0c","#dae7c2","#fce3ed","#cd8c95","#baffc9"]

	plots = []
	count = 0
	for index in range(len(data)):
		npd = np.array(data[index])

		tempList = data[:index]
		bot = [sum(i) for i in zip(*tempList)]

		if index != 0:
			p = plt.bar(ind,npd,width,color = color[index],bottom=bot)
		else:
			p = plt.bar(ind,npd,width,color = color[index])
		plots.append(p)
		count+=1
		
	plt.ylabel(yAxis)
	plt.title(yAxis + " per Strategy | Games("+ str(players[0].wins + players[0].losses + players[0].ties) + ")" )
	plt.xticks(ind+.1,xLabels,rotation=90);
	plt.legend(keys, loc='upper center', fancybox=True,ncol=2)
	plt.gcf().subplots_adjust(bottom=0.20)

	plt.savefig(yAxis+ " per Strategy")
	plt.show()



def roundRobinGame(listOfPlayers):
	for p1Index in range(len(listOfPlayers)):
		for p2Index in range(p1Index+1,len(listOfPlayers)):
			listOfPlayers[p1Index].moves = []
			listOfPlayers[p2Index].moves = []
			for x in range(100):
				simpleGame(listOfPlayers[p1Index],listOfPlayers[p2Index])

	listOfPlayers.sort(key=lambda x: x.wins, reverse=True)
	# for x in listOfPlayers:
	# 	print(x)

def simpleGame(p1,p2):
	iterations = 50
	# print(p1.name + " vs. " + p2.name)
	p1Score = 0
	p2Score = 0

	for x in range(iterations):
		p1Move = p1.strategy(p2);
		p2Move = p2.strategy(p1);

		(p1S,p2S) = b2[p1Move+p2Move];
		p1Score += p1S
		p2Score += p2S

	setRecords(p1,p2,p1Score,p2Score);

def setRecords(p1,p2,p1Score,p2Score):
	p1d = "",
	p2d = "";

	if(p1Score < p2Score):
		p1d = "W"
		p2d = "L"
	elif(p2Score < p1Score):
		p1d = "L"
		p2d = "W"
	else:
		p1d = "T"
		p2d = "T"

	p1.setRecord(p1d,p2.name)
	p2.setRecord(p2d,p1.name)

main();