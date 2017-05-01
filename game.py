from board import *
from player import *

def main():
	t4t = T4Tplayer();
	cp  =	Cplayer();
	dp  = Dplayer();

	p1 = t4t
	p2 = dp

	simpleGame(p1,p2)


def simpleGame(p1,p2):
	iterations = 1
	print(p1.name + " vs. " + p2.name)

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

	print(p2.name,p2.logistics)
	p1.setRecord(p1d,"test")
	print(p2.name,p2.logistics)

main();