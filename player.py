class Player:
	name = "User Input Strategy"
	score = 0;
	moves = [];
	wins = 0;
	losses = 0;
	ties = 0;
	logistics = {};

	def _init__(self):
		self.moves = [];
		self.score = 0;
		self.wins = 0;
		self.losses = 0;
		self.ties = 0;
		self.logistics = {"wins":0,"loss":0,"ties":0,"games":0};


	def strategy(self,opponent):
		i = ""
		while( i != "C" and i != "D"):
			i = input("Enter C (cooperate) or D(defect)");
		moves.append(i);
		return i;

	def addScore(self,score):
		self.score += score;

	def addMove(self,move):
		self.moves.append(move)

	def setRecord(self,decision,opponentName):
		print(self)
		if(opponentName not in self.logistics.keys()):
			self.logistics[opponentName] = {"wins":0,"loss":0,"ties":0,"games":0}

		if(decision == "T"):
			self.logistics[opponentName]["ties"] += 1;
			self.ties += 1 ;
		elif(decision == "W"):
			self.logistics[opponentName]["wins"] += 1;
			self.wins += 1;
		else:
			self.logistics[opponentName]["loss"] += 1;
			self.losses += 1;
		self.logistics[opponentName]["games"] += 1

		print(self)


	def __str__(self):
		s = "-------------------\n"
		s += self.name + " record\n" 
		s += "Games played: " + str(self.wins + self.losses) + "\n"
		s +="Won: " + str(self.wins) + "\t\tLost: " + str(self.losses) + "\t\tTied: "+ str(self.ties) + "\n\n"

		for opponentName in self.logistics.keys():
			l = self.logistics[opponentName]
			s += "against " + opponentName+ " : \n";
			s += "\tGames Played: " + str(l['games']) + "  Win Rate: " + str(l["wins"] * 1.0/ l['games']) + "\n"
			s += "\twins(" + str(l["wins"]) + ") losses(" + str(l['loss']) + ") ties(" + str(l['ties']) +")\n\n"
		s += '-------------------\n'

		return s


class Cplayer(Player):
	name = "Cooperative Strategy"

	def strategy(self,opponent):
		self.moves.append("C")
		return "C"

class Dplayer(Player):
	name = "Defective Strategy"
	def strategy(self,opponent):
		self.moves.append("D");
		return "D";

class T4Tplayer(Player):
	name = "Tit For Tat Strategy"

	def strategy(self,opponent):
		if len(self.moves) == 0 or opponent.moves[-1] == "D":
			self.moves.append("C");
			return "C"
		self.moves.append("D");
		return "D"


