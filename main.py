# pyinstaller main.py -F --onefile --noupx --noconsole --icon="assets/img/TimeMachinesUpgradeImg.ico" -n="Idle Time Clickers"
# Made By: Neuxs

import pygame
import sys
import threading

pygame.mixer.init()
ClickerButtonClick = pygame.mixer.Sound("assets/sounds/ClickerButtonClick.mp3")
ButtonClick = pygame.mixer.Sound("assets/sounds/ButtonClick.mp3")
ButtonError = pygame.mixer.Sound("assets/sounds/ButtonError.mp3")
ButtonError.set_volume(0.05)

WindowIcon = pygame.image.load("assets/img/TimeMachinesUpgradeImg.png")
HelpIcon = pygame.image.load("assets/img/HelpIcon.png")
HelpIcon = pygame.transform.scale(HelpIcon, (48, 48))
ShopIcon = pygame.image.load("assets/img/ShopIcon.png")
ShopIcon = pygame.transform.scale(ShopIcon, (42, 46))
GameBackground = pygame.image.load("assets/img/GameBackground.png")
ShopBackground = pygame.image.load("assets/img/ShopBackground.png")
ClickerButtonPressed = pygame.image.load("assets/img/ClickerButtonPressed.png")
ClickerButtonPressed = pygame.transform.scale(ClickerButtonPressed, (132, 72))
ClickerButtonUnpressed = pygame.image.load("assets/img/ClickerButtonUnpressed.png")
ClickerButtonUnpressed = pygame.transform.scale(ClickerButtonUnpressed, (132, 72))
BackArrow = pygame.image.load("assets/img/BackArrow.png")
BackArrow = pygame.transform.scale(BackArrow, (64, 64))
StrongerComputersUpgradeImg = pygame.image.load("assets/img/StrongerComputersUpgradeImg.png")
StrongerComputersUpgradeImg = pygame.transform.scale(StrongerComputersUpgradeImg, (52, 80))
ScientistsUpgradeImg = pygame.image.load("assets/img/ScientistsUpgradeImg.png")
ScientistsUpgradeImg = pygame.transform.scale(ScientistsUpgradeImg, (60, 100))
ComplicatedEquationsUpgradeImg = pygame.image.load("assets/img/ComplicatedEquationsUpgradeImg.png")
ComplicatedEquationsUpgradeImg = pygame.transform.scale(ComplicatedEquationsUpgradeImg, (80, 32))
TimeMachinesUpgradeImg = pygame.image.load("assets/img/TimeMachinesUpgradeImg.png")
TimeMachinesUpgradeImg = pygame.transform.scale(TimeMachinesUpgradeImg, (76, 72))

WindowX, WindowY = (800, 600)
WinCenterX, WinCenterY = (WindowX / 2, WindowY / 2)
screen = pygame.display.set_mode((WindowX, WindowY))
pygame.display.set_icon(WindowIcon)
pygame.display.set_caption('Idle Time Clickers')
ScoreTextX, ScoreTextY = (10, 10)
ShopScoreTextX, ShopScoreTextY = (40, WindowY - 72)
Score_Val = 0
HelpMenuRun, ShopMenuRun, GameMenuRun = (False, False, True)
ClickerPerClick = 1
StrongerComputersUpgradeCost = 25
ScientistsCost = 1000
PassiveClicks = 0
ComplicatedEquationsCost = 2500
ComplicatedEquationsAddClick = 10
TimeMachinesCost = 20000
TimeMachinesAddPassive = 1000
ran = True

WHITE = (255, 255, 255)

pygame.font.init()
RetroGamingFont = pygame.font.Font('assets/fonts/Retro Gaming.ttf', 32)
RetroGamingFontShop = pygame.font.Font('assets/fonts/Retro Gaming.ttf', 16)

def addPassiveIncome():
    global ran

    def addPassiveIncome2():
        global Score_Val, PassiveClicks
        if PassiveClicks > 0:
            Score_Val += PassiveClicks

    addPassiveIncome2()

    if ran == True:
        threading.Timer(1.0, addPassiveIncome).start()

addPassiveIncome()

def ShopMenu():
    pygame.init()
    global ShopMenuRun, GameMenuRun
    ShopMenuRun = True
    GameMenuRun = False

    def drawScore(x, y):
        ShopScoreText = RetroGamingFont.render("Clicks: " + str(Score_Val), True, WHITE)
        screen.blit(ShopScoreText, (x, y))

    class StrongerComputersUpgrade:
        def __init__(self, x, y, scale):
            self.rect = StrongerComputersUpgradeImg.get_rect()
            self.rect.topleft = (x, y)
            self.scale = scale
            self.pressed = False

        def draw(self, TextX, TextY, TextX2, TextY2, TextX3, TextY3):
            SCUText = RetroGamingFontShop.render("Stronger Computers", True, WHITE)
            screen.blit(SCUText, (TextX, TextY))
            SCUText2 = RetroGamingFontShop.render("+ 1 per Click", True, WHITE)
            screen.blit(SCUText2, (TextX2, TextY2))
            SCUText3 = RetroGamingFontShop.render("Cost: " + str(StrongerComputersUpgradeCost), True, WHITE)
            screen.blit(SCUText3, (TextX3, TextY3))
            screen.blit(StrongerComputersUpgradeImg, (self.rect.x, self.rect.y))
            self.check_click()

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed = True
                else:
                    if self.pressed == True:
                        global ClickerPerClick, StrongerComputersUpgradeCost, Score_Val
                        if Score_Val < StrongerComputersUpgradeCost:
                            pygame.mixer.Sound.play(ButtonError)
                        else:
                            pygame.mixer.Sound.play(ButtonClick)
                            ClickerPerClick += 1
                            Score_Val -= StrongerComputersUpgradeCost
                            StrongerComputersUpgradeCost *= 2
                        self.pressed = False

    class ScientistsUpgrade:
        def __init__(self, x, y, scale):
            self.rect = ScientistsUpgradeImg.get_rect()
            self.rect.topleft = (x, y)
            self.scale = scale
            self.pressed = False

        def draw(self, TextX, TextY, TextX2, TextY2, TextX3, TextY3):
            SCUText = RetroGamingFontShop.render("Scientists", True, WHITE)
            screen.blit(SCUText, (TextX, TextY))
            SCUText2 = RetroGamingFontShop.render("+ 5 Passive Income", True, WHITE)
            screen.blit(SCUText2, (TextX2, TextY2))
            SCUText3 = RetroGamingFontShop.render("Cost: " + str(ScientistsCost), True, WHITE)
            screen.blit(SCUText3, (TextX3, TextY3))
            screen.blit(ScientistsUpgradeImg, (self.rect.x, self.rect.y))
            self.check_click()

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed = True
                else:
                    if self.pressed == True:
                        global PassiveClicks, ScientistsCost, Score_Val
                        if Score_Val < ScientistsCost:
                            pygame.mixer.Sound.play(ButtonError)
                        else:
                            pygame.mixer.Sound.play(ButtonClick)
                            PassiveClicks += 5
                            Score_Val -= ScientistsCost
                            ScientistsCost /= 0.25
                            addPassiveIncome()
                        self.pressed = False

    class ComplicatedEquationsUpgrade:
        def __init__(self, x, y, scale):
            self.rect = ComplicatedEquationsUpgradeImg.get_rect()
            self.rect.topleft = (x, y)
            self.scale = scale
            self.pressed = False

        def draw(self, TextX, TextY, TextX2, TextY2, TextX3, TextY3):
            SCUText = RetroGamingFontShop.render("Complicated Equations", True, WHITE)
            screen.blit(SCUText, (TextX, TextY))
            SCUText2 = RetroGamingFontShop.render("+ " + str(ComplicatedEquationsAddClick) + " per Click", True, WHITE)
            screen.blit(SCUText2, (TextX2, TextY2))
            SCUText3 = RetroGamingFontShop.render("Cost: " + str(ComplicatedEquationsCost), True, WHITE)
            screen.blit(SCUText3, (TextX3, TextY3))
            screen.blit(ComplicatedEquationsUpgradeImg, (self.rect.x, self.rect.y))
            self.check_click()

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed = True
                else:
                    if self.pressed == True:
                        global ClickerPerClick, ComplicatedEquationsCost, Score_Val, ComplicatedEquationsAddClick
                        if Score_Val < ComplicatedEquationsCost:
                            pygame.mixer.Sound.play(ButtonError)
                        else:
                            pygame.mixer.Sound.play(ButtonClick)
                            ClickerPerClick += ComplicatedEquationsAddClick
                            Score_Val -= ComplicatedEquationsCost
                            ComplicatedEquationsCost /= 0.25
                            ComplicatedEquationsAddClick /= 0.8
                        self.pressed = False

    class TimeMachinesUpgrade:
        def __init__(self, x, y, scale):
            self.rect = TimeMachinesUpgradeImg.get_rect()
            self.rect.topleft = (x, y)
            self.scale = scale
            self.pressed = False

        def draw(self, TextX, TextY, TextX2, TextY2, TextX3, TextY3):
            SCUText = RetroGamingFontShop.render("Time Machines", True, WHITE)
            screen.blit(SCUText, (TextX, TextY))
            SCUText2 = RetroGamingFontShop.render("+ " + str(TimeMachinesAddPassive) + " Passive Income", True, WHITE)
            screen.blit(SCUText2, (TextX2, TextY2))
            SCUText3 = RetroGamingFontShop.render("Cost: " + str(TimeMachinesCost), True, WHITE)
            screen.blit(SCUText3, (TextX3, TextY3))
            screen.blit(TimeMachinesUpgradeImg, (self.rect.x, self.rect.y))
            self.check_click()

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed = True
                else:
                    if self.pressed == True:
                        global PassiveClicks, TimeMachinesCost, Score_Val, TimeMachinesAddPassive
                        if Score_Val < TimeMachinesCost:
                            pygame.mixer.Sound.play(ButtonError)
                        else:
                            pygame.mixer.Sound.play(ButtonClick)
                            PassiveClicks += TimeMachinesAddPassive
                            Score_Val -= TimeMachinesCost
                            TimeMachinesCost /= 0.5
                            TimeMachinesAddPassive /= 0.8
                            addPassiveIncome()
                        self.pressed = False

    class BackArrowIcon:
        def __init__(self, x, y, scale):
            self.rect = BackArrow.get_rect()
            self.rect.topleft = (x, y)
            self.scale = scale
            self.pressed = False

        def draw(self):
            screen.blit(BackArrow, (self.rect.x, self.rect.y))
            self.check_click()

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed = True
                else:
                    if self.pressed == True:
                        pygame.mixer.Sound.play(ButtonClick)
                        Game()
                        self.pressed = False

    BackArrowButton = BackArrowIcon(40, 40, (64, 64))
    StrongerComputersUpgradeButton = StrongerComputersUpgrade(WindowX / 5, WindowY / 5, (52, 80))
    ScientistsUpgradeButton = ScientistsUpgrade(WindowX / 3, WindowY / 2, (60, 100))
    ComplicatedEquationsUpgradeButton = ComplicatedEquationsUpgrade(WindowX / 2, WindowY / 5 + 30, (80, 32))
    TimeMachinesUpgradeButton = TimeMachinesUpgrade(WindowX - 200, WindowY / 2 + 20, (76, 72))
    running = True

    while running and GameMenuRun == False and HelpMenuRun == False:
        screen.blit(ShopBackground,(0,0))
        drawScore(ShopScoreTextX, ShopScoreTextY)
        BackArrowButton.draw()
        StrongerComputersUpgradeButton.draw(WindowX / 5 - 65, WindowY / 5 + 80, WindowX / 5 - 40, WindowY / 5 + 98, WindowX / 5 - 15, WindowY / 5 + 116)
        ScientistsUpgradeButton.draw(WindowX / 3 - 20, WindowY / 2 + 100, WindowX / 3 - 65, WindowY / 2 + 118, WindowX / 3 - 20, WindowY / 2 + 136)
        ComplicatedEquationsUpgradeButton.draw(WindowX / 2 - 65, WindowY / 5 + 80, WindowX / 2 - 28, WindowY / 5 + 98, WindowX / 2 - 15, WindowY / 5 + 116)
        TimeMachinesUpgradeButton.draw(WindowX - 200 - 30, WindowY / 2 + 100, WindowX - 200 - 75, WindowY / 2 + 118, WindowX - 200 - 20, WindowY / 2 + 136)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for i in range(10000):
                    global PassiveClicksToggle
                    PassiveClicksToggle = False
                    pygame.quit()
                    sys.exit()
                    running = False

def Game():
    pygame.init()
    global HelpMenuRun, ShopMenuRun, GameMenuRun
    HelpMenuRun = False
    ShopMenuRun = False
    GameMenuRun = True

    class Shop:
        def __init__(self, x, y, scale):
            self.rect = ShopIcon.get_rect()
            self.rect.topleft = (x, y)
            self.scale = scale
            self.pressed = False

        def draw(self):
            screen.blit(ShopIcon, (self.rect.x, self.rect.y))
            self.check_click()

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed = True
                else:
                    if self.pressed == True:
                        pygame.mixer.Sound.play(ButtonClick)
                        global ShopMenuRun, GameMenuRun
                        ShopMenuRun = False
                        GameMenuRun = False
                        ShopMenu()
                        self.pressed = False

    def drawScore(x, y):
        ScoreText = RetroGamingFont.render("Clicks: " + str(Score_Val), True, WHITE)
        screen.blit(ScoreText, (x, y))

    class ClickButton:
        def __init__(self, x, y, scale):
            self.rect = ClickerButtonPressed.get_rect()
            self.rect.topleft = (x, y)
            self.scale = scale
            self.pressed = False

        def draw(self):
            if self.pressed == True:
                screen.blit(ClickerButtonPressed, (self.rect.x, self.rect.y))
            else:
                screen.blit(ClickerButtonUnpressed, (self.rect.x, self.rect.y))

            self.check_click()

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed = True
                else:
                    if self.pressed == True:
                        pygame.mixer.Sound.play(ClickerButtonClick)
                        global Score_Val, ClickerPerClick
                        Score_Val += ClickerPerClick
                        self.pressed = False
            else:
                self.pressed = False

    ClickerButton = ClickButton(WinCenterX - 66, WindowY - 122, (264, 144))
    ShopButton = Shop(WindowX - 52, 20, (42, 46))
    pygame.display.flip()
    running = True

    while running == True and HelpMenuRun == False and ShopMenuRun == False:
        screen.blit(GameBackground,(0,0))
        ClickerButton.draw()
        ShopButton.draw()
        drawScore(ScoreTextX, ScoreTextY)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for i in range(10000):
                    global PassiveClicksToggle
                    PassiveClicksToggle = False
                    pygame.quit()
                    sys.exit()
                    running = False

Game()