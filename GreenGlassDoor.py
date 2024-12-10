import pygame, simpleGE

class Door(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("DoorClosed.png")
        self.setSize(140,232)
        self.position = (320, 140)      
              
              
class Instructions(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.response = "Quit"
        self.background.fill((183,255,203))
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
            "This is the Green Glass Door.",
            "Only some words can go through it.",
            "Type your guesses into the input box,",
            "and press ENTER to see if they go through.",
            "Figure out why only some words fit. ",
            "Type 10 correct guesses in a row to win!",
            "Good luck!",
            ""]
        self.directions.center = (320,370)
        self.directions.size = (360, 175)
        self.directions.clearBack = True
        self.directions.font = pygame.font.Font(None, 26)
        self.directions.fgColor = ((0,0,0))
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (72.5,370)
        self.btnPlay.size = (80,30)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (567.5,370)
        self.btnQuit.size = (80,30)
        
        self.door = Door(self)
        
        self.sprites = [self.door,
                        self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        ]
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        
        
class Game(simpleGE.Scene):
    def __init__(self):
            super().__init__()
            
            self.background.fill((183,255,203))
            
            self.response = "Play"
            self.guess = ""
            self.correct = 0
            self.incorrect = 0
            self.winCondition = 0
            self.sndDoorClose = simpleGE.Sound("doorClose.flac")
            self.sndDoorOpen = simpleGE.Sound("doorOpen.flac")
           
            self.door = Door(self)
            self.door.position = (320, 180)
            
            self.txtInput = simpleGE.TxtInput()
            self.txtInput.size = (300, 50) 
            self.txtInput.center = (320, 400)
            self.txtInput.font = pygame.font.Font(None, 40)
            
            self.btnExit = simpleGE.Button()
            self.btnExit.text = "Exit"
            self.btnExit.center = (75,400)
            self.btnExit.size = (80,30)
            
            self.btnHint = simpleGE.Button()
            self.btnHint.text = "Hint"
            self.btnHint.center = (1000, -1000)
            self.btnHint.size = (80, 30)
                       
            self.lblCorrect = simpleGE.Label()
            self.lblCorrect.text = f"Correct: {self.correct}"
            self.lblCorrect.size = (150,30)
            self.lblCorrect.center = (75, 30)
            self.lblCorrect.clearBack = True
            self.lblCorrect.fgColor = (0,0,0)
            
            self.lblIncorrect = simpleGE.Label()
            self.lblIncorrect.text = "Incorrect: 0"
            self.lblIncorrect.size = (150,30)
            self.lblIncorrect.center = (535, 30)
            self.lblIncorrect.clearBack = True
            self.lblIncorrect.fgColor = (0,0,0)
            
            self.lblHint = simpleGE.Label()
            self.lblHint.text = "Green, Glass, and Door can all go through..."
            self.lblHint.size = (360,40)
            self.lblHint.center = (1000,-1000)
            self.lblHint.clearBack = True
            self.lblHint.fgColor = (0,0,0)
            self.lblHint.font = pygame.font.Font(None, 26)
            
            self.sprites = [self.door,
                            self.btnExit,
                            self.btnHint,
                            self.lblCorrect,
                            self.txtInput,
                            self.lblIncorrect,
                            self.lblHint,
                            ]
            
            
    def checkWord(self,guess):
        for i in range (len(guess)-1):
            if guess[i] == guess[i+1]:
                return True
            
                                 
    def processEvent(self, event):
        self.txtInput.readKeys(event)
        
        
    def doEvents(self, event):
        if event.type == pygame.KEYDOWN:
            self.guess = "Why do I have to write the code like this just to make the empty black box that appears from RETURN disappear? At least I fixed it..."
            if event.key == pygame.K_RETURN:
                self.guess = self.txtInput.text
                self.txtInput.text = ""
                
                if self.checkWord(self.guess) == True:
                    self.sndDoorOpen.play()
                    self.door.image = pygame.image.load("DoorOpen.png")
                    self.door.setSize(200,232)
                    self.correct += 1
                    self.winCondition += 1
                    self.lblCorrect.text = f"Correct: {self.correct}"
                    self.guess = ""
                    
                    
                else:
                    self.sndDoorClose.play()
                    self.door.image = pygame.image.load("DoorClosed.png")
                    self.door.setSize(140,232)
                    self.incorrect +=1
                    self.winCondition = 0
                    self.lblIncorrect.text = f"Incorrect: {self.incorrect}"
                    self.guess = ""
                    
        
                                          
                
    def process(self):
        if self.btnExit.clicked:
            self.response = "Exit"
            self.stop()
            
        if self.incorrect >= 20:
            self.btnHint.center = (550,400)
            
        if self.btnHint.clicked: 
            self.lblHint.center = (320,350)
            
        if self.winCondition >= 10:
            self.response = "Win"
            self.stop()
            
        if self.guess == "":
            self.txtInput.text = ""
        
        
        
class Win(simpleGE.Scene):
    def __init__(self):
            super().__init__()
            self.background.fill((183,255,203))
            
            self.sndWin = simpleGE.Sound("Win.wav")
                        
            self.door = Door(self)
            self.door.image = pygame.image.load("DoorOpen.png")
            self.door.setSize(200,232)
            self.door.position = (340, 120)
                       
            self.btnExit = simpleGE.Button()
            self.btnExit.text = "Exit"
            self.btnExit.center = (72.5,370)
            self.btnExit.size = (80,30)
            
            self.btnQuit = simpleGE.Button()
            self.btnQuit.text = "Quit"
            self.btnQuit.center = (567.5,370)
            self.btnQuit.size = (80,30)
            
            self.winImage = simpleGE.Sprite(self)
            self.winImage.setImage("youWin.png")
            self.winImage.setSize(280,212)
            self.winImage.position = (320, 360)
            
            self.sprites = [self.winImage,
                            self.door,
                            self.btnExit,
                            self.btnQuit,
                            ]
    def process(self):
        
        self.sndWin.play()
            
        if self.btnExit.clicked:
            self.response = "Exit"
            self.stop()
            
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()

        
def main():
    
    keepGoing = True
    
    while keepGoing:
        
        instructions = Instructions()
        instructions.start()
        
        if instructions.response == "Quit":
            keepGoing = False
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            
            if game.response == "Exit":
                game.stop()
                continue
            
            if game.response == "Win":
                 win = Win()
                 win.start()
                 
                 if win.response == "Exit":
                     win.stop()
                     continue
                    
                 if win.response == "Quit":
                     keepGoing = False
                    
                  
if __name__ == "__main__":
    main()
    
    

        