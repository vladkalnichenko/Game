from PyQt5 import QtCore, QtGui, QtWidgets

import os,random
card= ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'B♠', 'D♠', 'K♠',
	   'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'B♥', 'D♥', 'K♥',
	   'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'B♦', 'D♦', 'K♦',
	   'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'B♣', 'D♣', 'K♣']

class Card(QtWidgets.QLabel):

	def __init__(self,rank,suit):
		#----------------Backend_data---------------------
		self.suit = suit
		self.rank = rank
		self.set_value()
		# ----------------State-------------------------
		self.active=False
		self.visible = False

		#----------------Visual_parameters----------------
		#self.__img_back = os.path.join(r"C:\Users\user\Desktop\ооп\Programs\Pyramide\Cards_100_150\purple_back")
		QtWidgets.QLabel.__init__(self)
		self.setGeometry(QtCore.QRect(0, 0, 100, 150))
		self.setObjectName(self.rank + self.suit)
		#self.__img = os.path.join(r"C:\Users\user\Desktop\ооп\Programs\Pyramide\Cards_100_150", self.rank +
		#						  self.suit)
		self.setPixmap_()

		#-----------RELATIONSHIPS-----------------
		self.parents=[]
		self.childs=[]


	def set_value(self):
		if self.rank == 'A':
			self.value = 1
		elif self.rank == '2':
			self.value =2
		elif self.rank == '3':
			self.value =3
		elif self.rank == '4':
			self.value =4
		elif self.rank == '5':
			self.value =5
		elif self.rank == '6':
			self.value =6
		elif self.rank == '7':
			self.value =7
		elif self.rank == '8':
			self.value =8
		elif self.rank == '9':
			self.value =9
		elif self.rank == '10':
			self.value =10
		elif self.rank == 'B':
			self.value =11
		elif self.rank == 'D':
			self.value =12
		elif self.rank=='K':
			self.value=13

	def getVal(self):
		return self.value


	def setPixmap_(self):
		if self.visible :
			#self.setPixmap(QtGui.QPixmap(self.__img))
			self.setStyleSheet(
				"QLabel{{background-image: url({});border-radius:60px;overflow:hidden;background-color: transparent !important }}".format(
					'./pack/' + self.rank + self.suit + '.png'))
		else :
			self.setStyleSheet(
				"QLabel{{background-image: url({});border-radius:60px;overflow:hidden;background-color: transparent !important }}".format(
					'./pack/back.png'))
			#self.setPixmap(QtGui.QPixmap(self.__img_back))

	def change_visible(self):
		if self.visible :
			self.visible = False
			self.setPixmap_()
		else :
			self.visible = True
			self.setPixmap_()

	def is_visible(self):
		return True if self.visible else False

	def change_active_state(self):
		if self.active :
			self.active = False

		else :
			self.active = True

	def __str__(self):
		return self.rank + self.suit

	def __add__(self, other):
		return self.value + other.value


class DeckCard(QtWidgets.QLabel):
	#signalChangeDeckCard = QtCore.pyqtSignal()
	def __init__(self,cards):

		# ----------------Visual_parameters----------------
		QtWidgets.QLabel.__init__(self)
		self.setGeometry(QtCore.QRect(0, 0, 100, 150))
		self.setObjectName("DeckCard")
		#self.__img = os.path.join(r"C:\Users\user\Desktop\ооп\Programs\Pyramide\Cards_100_150\purple_back")
		#self.setPixmap(QtGui.QPixmap(self.__img))
		self.setStyleSheet(
			"QLabel{{background-image: url({});border-radius:60px;overflow:hidden;background-color: transparent !important }}".format(
				'./pack/back.png'))
		self.ScaledContents = True



		#list of cards in Deck
		self.cards=cards
		#number of cards in Deck
		self.num_cards=len(self.cards)
		#deque representation
		#self.cardsDeque = collections.deque(self.cards)

		# we see it near the Deck on the board
		self.activeCard = self.cards[0]
		self.currentIndex=0

	def get_deckCard(self):
		return self.activeCard


	def if_removed(self):
		self.currentIndex-=1

	def currentIndexChange(self,change_to_Null_index=0):
		if change_to_Null_index == 1 :
			self.currentIndex=0
		else :
			self.currentIndex=self.currentIndex+1

	def getNextDeckCard(self):
		try :
			self.currentIndexChange()
			return self.cards[self.currentIndex]
		except IndexError:
			self.currentIndexChange(1)
			return self.cards[self.currentIndex]

	def changeActiveCard(self):
		self.activeCard=self.getNextDeckCard()

	def using_card_from_the_deck(self):
		self.cards.remove(self.activeCard)
		self.if_removed()


def create_cards():
	random.shuffle(card)

	list_of_cards = []  # все наши карточки тут
	for symbols in range(len(card)):
		card_tmp = Card(card[symbols][:-1], card[symbols][-1])
		list_of_cards.append(card_tmp)

	deck_cards = (list_of_cards[0:24])  # карты что в деке
	list_1 = (list_of_cards[24:25])
	list_2 = (list_of_cards[25:27])
	list_3 = (list_of_cards[27:30])
	list_4 = (list_of_cards[30:34])
	list_5 = (list_of_cards[34:39])
	list_6 = (list_of_cards[39:45])
	list_7 = (list_of_cards[45:52])

	playing_layers = []  # карты что на поле разложенные по слоям (список в списке)
	for l in (list_7, list_6, list_5, list_4, list_3, list_2, list_1):
		playing_layers.append(l)



	def createrelationships(pyramide_layers):
		pyramideLayers = pyramide_layers.copy()
		pyramideLayers.reverse()
		num_layers = len(pyramide_layers)
		for n_layer in range(num_layers - 1):
			for n_card in range(len(pyramideLayers[n_layer])):
				child1 = pyramideLayers[n_layer + 1][n_card]
				child2 = pyramideLayers[n_layer + 1][n_card + 1]
				pyramideLayers[n_layer][n_card].childs.append(child1)
				pyramideLayers[n_layer][n_card].childs.append(child2)
				child1.parents.append(pyramideLayers[n_layer][n_card])
				child2.parents.append(pyramideLayers[n_layer][n_card])
		pyramideLayers.reverse()
		return pyramide_layers

	playing_layers=createrelationships(playing_layers)

	return deck_cards, playing_layers

class PyramideScene(QtWidgets.QGraphicsScene):
	EndGameSignal = QtCore.pyqtSignal()
	def __init__(self):
		QtWidgets.QGraphicsScene.__init__(self)
		#------------------------scene_parameters----------------------
		self.setBackgroundBrush(QtGui.QColor(92,117,97,alpha = 255))
		#self.setSceneRect(0, 150, 995, 650)
		self.setSceneRect(0, 0, 995, 650)

		self.addRect(self.sceneRect())
		self.end_game = os.path.join(r"pack\ground")
		self.__init_obj()
		self.game_over()

	def __init_obj(self):
		#------------------------adding_cards_to_the_field-------------
		self.deck_cards, self.pyramide_layers = create_cards()

		self.cards_to_the_deck()

		maniken_obj=DeckCard(self.deck_cards)
		self.maniken_card=self.addWidget(maniken_obj)
		self.maniken_card.setPos(30,30)

		for card in self.deck_cards:
			card.change_visible()

		self.put_Deck_cards()
		self.maniken_card.widget().get_deckCard().setVisible(True)

		self.current_card=0
		self.current_card_old_pos=0


	def restart(self):
		# restart scene
		self.clear()
		self.__init_obj()

	def opening_next_card(self,action_item):

		if not action_item.widget().parents:
			self.game_over()

		for parent in action_item.widget().parents:
			parent.childs.remove(action_item.widget())

			if not parent.childs:
				parent.change_visible()


	def game_over(self):
		self.addPixmap(QtGui.QPixmap(self.end_game))
		self.EndGameSignal.emit()


	def mousePressEvent(self, event):

		print(len(self.pyramide_layers[0]))
		print(len(self.maniken_card.widget().cards))
		for card in self.maniken_card.widget().cards:

			print(str(card),end=" ")
		print()

		if event.button() == QtCore.Qt.LeftButton:
			scenePos = event.scenePos()
			items = self.items(scenePos)
			if not items:
				return
			clked_item=items[0]

			if isinstance(clked_item,QtWidgets.QGraphicsProxyWidget):
				if isinstance(clked_item.widget(),Card) and clked_item.widget().is_visible():

					if self.current_card :

						print(self.current_card.widget().getVal(),clked_item.widget().getVal())

						if self.current_card.widget()+clked_item.widget() == 13 :
							if self.current_card.widget() == self.maniken_card.widget().get_deckCard():

								self.opening_next_card(clked_item)

								self.maniken_card.widget().using_card_from_the_deck()

								self.removeItem(self.current_card)

								self.removeItem(clked_item)
								print("okB")
								self.maniken_card.widget().changeActiveCard()
								print(self.maniken_card.widget().get_deckCard())

								self.maniken_card.widget().get_deckCard().setVisible(True)
								print("okF")
								self.current_card = 0
								return

							if clked_item.widget() == self.maniken_card.widget().get_deckCard():

								self.opening_next_card(self.current_card)

								self.maniken_card.widget().using_card_from_the_deck()
								self.removeItem(clked_item)

								self.removeItem(self.current_card)
								print("okB")
								print(self.maniken_card.widget().get_deckCard())
								self.maniken_card.widget().changeActiveCard()
								self.maniken_card.widget().get_deckCard().setVisible(True)

								print("okF")
								self.current_card = 0
								return

							self.opening_next_card(self.current_card)

							self.opening_next_card(clked_item)

							self.removeItem(clked_item)
							self.removeItem(self.current_card)



						else:
							self.current_card.setPos(self.current_card_old_pos)
							self.current_card=0


					else :
						# if we have a king
						if clked_item.widget().getVal()==13:
							if clked_item.widget()==self.maniken_card.widget().get_deckCard():

								self.maniken_card.widget().using_card_from_the_deck()

								self.removeItem(clked_item)
								self.maniken_card.widget().changeActiveCard()
								self.maniken_card.widget().get_deckCard().setVisible(True)
								return

							else :

								self.opening_next_card(clked_item)
								self.removeItem(clked_item)

						self.current_card=clked_item
						self.activate_card(clked_item)

				elif isinstance(clked_item.widget(),DeckCard) :
					if self.current_card:
						self.current_card.setPos(self.current_card_old_pos)
					self.maniken_card.widget().get_deckCard().setVisible(False)
					self.maniken_card.widget().changeActiveCard()
					self.maniken_card.widget().get_deckCard().setVisible(True)
					self.current_card = 0

					#self.deckCard = self.addWidget(self.maniken_card.widget().get_deckCard())
					#self.deckCard.setPos(135, 200)
					print(len(self.maniken_card.widget().cards))
					print(self.maniken_card.widget().cards)

				else :
					return


	def put_Deck_cards(self):
		for card in self.maniken_card.widget().cards:

			card_=self.addWidget(card)
			card_.setPos(135,30)
			card.setVisible(False)


	def activate_card(self,card):
		card_pos=card.pos()
		self.current_card_old_pos=card_pos
		card.setPos(card_pos.x(),card_pos.y())

	def cards_to_the_deck(self):

		layers =self.pyramide_layers
		#widgets_layers=[[],[],[],[],[],[],[]]
		# make the firs layer visible
		for card in layers[0]:
			card.change_visible()
		# starter point to put card in the field
		starter_x=635
		for layer in range(len(layers),-1,-1) :
			layer_length=7-layer
			for card in range(layer_length) :

				card_in_the_field=self.addWidget(layers[layer][card])
				card_in_the_field.setPos(starter_x-(layer_length-card)*100,(layer_length+1)*80-150)
				#card_in_the_field.parents=[]
				#card_in_the_field.childs=[]
				#widgets_layers[layer].append(card_in_the_field)

			starter_x+=50


class Game(QtWidgets.QWidget):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setObjectName('MainWidget')
		self.setStyleSheet('''#MainWidget {
		                background-color: #279;
		            }''')

		# parameters QWIndowWIdget
		#self.setFixedSize(1050,800 )
		self.setFixedSize(1050,800)
		self.Initialization()


	def Initialization(self):
		layout = QtWidgets.QGridLayout()
		self.setLayout(layout)
		self.PyramideView = QtWidgets.QGraphicsView()
		layout.addWidget(self.PyramideView)
		self.PyramideScene = PyramideScene()
		self.PyramideView.setScene(self.PyramideScene)

		self.PyramideView.setFixedSize(1000, 655)

		self.PyramideScene.EndGameSignal.connect(self.handler_EndGameSignal)

	@QtCore.pyqtSlot()
	def handler_EndGameSignal(self):

		res = QtWidgets.QMessageBox.question(self, "Game Over", "Restart ? ",
											 QtWidgets.QMessageBox.Yes |
											 QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
		if res == QtWidgets.QMessageBox.Yes:
			self.PyramideScene.restart()
		else:
			self.close()

def main():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Pyramide = Game()
	Pyramide.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
