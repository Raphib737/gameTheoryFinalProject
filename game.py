from board import *
from player import *

def main():
	t4t = T4Tplayer();
	cp  =	Cplayer();
	dp  = Dplayer();
	rp = Randomplayer();
	hp = halfplayer();
	shp = smartHalfPlayer();

	roundRobinGame([t4t,cp,dp,rp,hp,shp]);

def roundRobinGame(listOfPlayers):
	for p1Index in range(len(listOfPlayers)):
		for p2Index in range(p1Index+1,len(listOfPlayers)):
			listOfPlayers[p1Index].moves = []
			listOfPlayers[p2Index].moves = []
			simpleGame(listOfPlayers[p1Index],listOfPlayers[p2Index])

	listOfPlayers.sort(key=lambda x: x.wins, reverse=True)
	for x in listOfPlayers:
		print(x)

def simpleGame(p1,p2):
	iterations = 20000
	# print(p1.name + " vs. " + p2.name)

	for x in range(iterations):
		p1Move = p1.strategy(p2);
		p2Move = p2.strategy(p1);

		(p1Score,p2Score) = b1[p1Move+p2Move];
		p1.addScore(p1Score);
		p2.addScore(p2Score);

		setRecords(p1,p2,p1Score,p2Score);

def setRecords(p1,p2,p1Score,p2Score):
	p1d = "",
	p2d = "";

	if (p1Score > p2Score):
		p1d = "W"
		p2d = "L"
	elif(p2Score > p1Score):
		p1d = "L"
		p2d = "W"
	else:
		p1d = "T"
		p2d = "T"

	p1.setRecord(p1d,p2.name)
	p2.setRecord(p2d,p1.name)

main();