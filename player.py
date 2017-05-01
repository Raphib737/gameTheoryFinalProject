import random

class Player():
	name = "User Input"

	def __init__(self):
		self.moves = [];
		self.wins = 0;
		self.losses = 0;
		self.ties = 0;
		self.logistics = {};

	def strategy(self,opponent):
		i = ""
		while( i != "C" and i != "D"):
			i = input("Enter C (cooperate) or D(defect)");
		moves.append(i);
		return i;

	def addMove(self,move):
		self.moves.append(move)

	def setRecord(self,decision,opponentName):
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



	def __str__(self):
		s = "-------------------\n"
		s += self.name + " strategy record\n" 
		s += "Games played: " + str(self.wins + self.losses + self.ties) + " Win Rate: "+ str(self.wins/(self.wins+self.losses+self.ties * 1.0)*100) +"\n"
		s +="Won: " + str(self.wins) + "\t\tLost: " + str(self.losses) + "\t\tTied: "+ str(self.ties) + "\n\n"

		for opponentName in self.logistics.keys():
			l = self.logistics[opponentName]
			s += "against " + opponentName+ " : \n";
			s += "\tGames Played: " + str(l['games']) + "  Win Rate: " + str(l["wins"] * 100.00/ l['games']) + "\n"
			s += "\twins(" + str(l["wins"]) + ") losses(" + str(l['loss']) + ") ties(" + str(l['ties']) +")\n\n"

		return s


class Cplayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "Cooperative"

	def strategy(self,opponent):
		self.moves.append("C")
		return "C"

class Dplayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "Defective"

	def strategy(self,opponent):
		self.moves.append("D");
		return "D";

class T4Tplayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "Tit for Tat"

	def strategy(self,opponent):
		if len(self.moves) == 0:
			self.moves.append("C");
			return "C"
		if opponent.moves[-1] == "D":
			self.moves.append("D");
			return "D"
		else:
			self.moves.append("C");
			return "C"

class reversedT4Tplayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "reversed Tit for Tat"

	def strategy(self,opponent):
		if len(self.moves) == 0:
			self.moves.append("D");
			return "D"
		if opponent.moves[-1] == "D":
			self.moves.append("C");
			return "C"
		else:
			self.moves.append("D");
			return "D"

class Randomplayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "Random"

	def strategy(self,opponent):
		decision = ""
		dec = random.randint(1,10000000);
		dec = dec%2
		if(dec % 2 == 1):
			decision = "C";
		else:
			decision =  "D";

		self.addMove(decision)
		return decision




class halfplayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "Half and Half"

	def strategy(self,opponent):
		decision = ""
		dec = random.randint(0,100);
		if(dec >= 50):
			decision = "C"
		else:
			decision = "D"

		self.addMove(decision)
		return decision



class smartHalfPlayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "Re Op and 50 per decision"

	def strategy(self,opponent):
		decision = ""
		dec = random.randint(0,100);
		if(len(opponent.moves) == 0):
			if(dec >= 50):
				self.addMove("C")
				return "C"
			else:
				self.addMove("D")
				return "D"

		oppMove = opponent.moves[-1];
		if(dec >= 50):
			decision = oppMove
		else:
			if(oppMove == "C"):
				decision = "D"
			else:
				decision = "C"

		self.addMove(decision)
		return decision

class majorityPlayer(Player):
	def __init__(self):
		Player.__init__(self)
		self.name = "majority"

	def strategy(self,opponent):
		decision = ""

		if(len(opponent.moves) == 0):
			decision = "C"
			self.addMove(decision)
			return decision

		count = 0 
		for move in opponent.moves:
			if move == "C":
				count += 1;
			else:
				count -= 1

		if count >= 0:
			decision = "C"
		else:
			decision = "D"

		self.addMove(decision)
		return decision



