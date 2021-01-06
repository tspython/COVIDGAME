import sys
import time
import random
import math
import pygame


from config import config

pygame.init()

arial = pygame.font.SysFont("Arial", 15)
arial_big = pygame.font.SysFont("Arial", 30)


class Text:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        textDraw = arial_big.render(self.text, True, self.color)
        win.blit(textDraw, (self.x, self.y))


class Entity:
    def __init__(self, x, y, sprite_path):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite_path)
        self.projectile = None

    def draw(self):
        win.blit(self.sprite, (self.x, self.y))

    def send_projectile(self):
        self.projectile = Entity(self.x + 64, self.y + 64, "sprites/germ.png")

    def update_projectile(self):
        if not self.projectile == None:
            if self.projectile.y < player.y:
                self.projectile.y += 2
            elif self.projectile.y > player.y:
                self.projectile.y -= 2
            if self.projectile.x < player.x:
                self.projectile.x += 2
            elif self.projectile.x > player.x:
                self.projectile.x -= 2

    def draw_projectile(self):
        self.projectile.draw()

    def sneeze_attack(self):
        global playerscore

        field_layer = pygame.Surface((800, 800), pygame.SRCALPHA)
        pygame.draw.circle(
            field_layer,
            pygame.Color(255, 0, 0, 100),
            ((enemy.x + 64), (enemy.y + 64)),
            300,
            width=230,
        )
        win.blit(field_layer, (0, 0))

        if (
            math.sqrt(
                ((enemy.x + 64) - (player.x + 64)) ** 2
                + ((player.y - 64) - (enemy.y - 64)) ** 2
            )
            < 300
        ):
            playerscore -= 0.04

class Mole(Entity):
    def __init__(self, x, y, sprite_path, symptom, ttl):
        super().__init__(x, y, sprite_path)
        self.enabled = True
        self.sprite_path = sprite_path
        self.symptom = symptom
        self.ttl = ttl
        self.hoverText = arial.render(str(symptom), True, (255, 0, 0))

    def draw(self):
        if self.enabled:
            win.blit(self.sprite, (self.x, self.y))
            win.blit(
                self.hoverText,
                (self.x + 64 - self.hoverText.get_size()[0] * 0.5, self.y - 12),
            )

    def is_in_hitbox(self, x, y):
        if self.x + 40 <= x <= self.x + 90:
            if self.y + 10 <= y <= self.y + 125:
                if self.enabled:
                    return True

        return False


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load("sprites/player.png")
        self.isJumping = False
        self.jumpY = 0
        self.stamina = 12

    def draw(self):
        win.blit(self.sprite, (self.x, self.y))

    def update(self):
        if self.isJumping:
            if abs(self.jumpY - self.y) > 200:
                self.isJumping = False
            else:
                self.y -= 5

        if int(get_elapsed_time()) % 1 == 0:
            if self.stamina < 12:
                self.stamina += 1


class Message:
    def __init__(self, message):
        self.message = message

    def draw(self):
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(0, 0, 800, 800))
        textDraw = arial_big.render(self.message, True, (255, 255, 255))
        win.blit(textDraw, (0, 385))


class Button:
    def __init__(self, x, y, w, h, color, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        pygame.draw.rect(win, self.color, self.get_rect())
        textDraw = arial.render(self.text, False, (255, 255, 255))
        win.blit(textDraw, (self.x, self.y + 0.5 * self.h - 7.5))

    def is_mouse_hovered():
        x, y = pygame.mouse.get_pos()

        if self.x < x < self.x + self.w:
            if self.y < y < self.y + self.h:
                return True

        return False


def stage_one_setup():
    global playerscore
    global player

    global context_one
    global context_two
    global context_three
    global context_four
    global context_five
    global context_six
    global context_seven
    global context_eight
    global context_nine

    global game_end1
    global game_end2

    global enemy
    global feet

    playerscore = config["initial_score"]
    player = Player(400, 400)

    context_one = Message(
        "    You are an ordinary person, living in Beaverton, Oregon."
    )
    context_two = Message("    You want to go up to the store, in a pandemic.")
    context_three = Message("    So you have to wear a mask and socially distance.")
    context_four = Message(
        "   You see a person coming towards you, they are too close."
    )
    context_five = Message("    So you must stay away from them.")
    context_six = Message("    A to walk left.")
    context_seven = Message("    D to walk right.")
    context_eight = Message("    Space to jump.")
    context_nine = Message("    Get to 20 points to not get infected.")

    game_end1 = Message("    You stayed too close to a sick person.")
    game_end2 = Message("    You obtained COVID and got pneumonia...")

    enemy = Entity(700, 400, "sprites/happy_person.png")
    enemy.send_projectile()
    feet = Text("Feet", 350, 600, (0, 0, 0))

    music = pygame.mixer.Sound("music\extremeaction.mp3")
    music.set_volume(0.2)
    pygame.mixer.Channel(0).play(music)

    global highoctane
    highoctane = pygame.mixer.Sound("music\highoctane.mp3")

    del music


def stage_two_setup():
    global startTime

    global context_one
    global context_two
    global context_three
    global context_four
    global context_five
    global context_six
    global context_seven
    global context_eight
    global context_nine
    global context_ten
    global context_eleven
    global context_twelve
    global context_thirteen
    global context_fourteen
    global context_fifteen
    global context_sixteen
    
    global time_reset

    global mole1
    global mole2
    global mole3
    global mole4
    global mole5
    global mole6
    global moles

    global symptoms

    global enemy
    global feet
    global player

    global timeLeft
    global previousTime

    try:
        del enemy
        del feet
        del player
    except:
        pass

    startTime = time.time()

    context_one = Message("   Good job, you managed to stay away from a sick person!")
    context_two = Message("    You're the manager at this store.")
    context_three = Message("     You need to send home sick people.")
    context_four = Message("      Let's play a game.")
    context_five = Message("    Do you know the game Whac-A-Mole?")
    context_six = Message("   It's like that.")
    context_seven = Message("    But the moles are people with virus symptoms.")
    context_eight = Message(" And you only send home people with COVID-19 symptoms.")
    context_nine = Message("    Let's play.")
    context_ten = Message("Click on people with COVID symptoms above their heads.")
    context_eleven = Message("   Ideally, you should stay six feet away from others.")
    context_twelve = Message("   Get a score of 60 or greater to finish.")
    context_thirteen = Message("   You have 90 seconds.")
    context_fourteen = Message("   Ready")
    context_fifteen = Message("   Set")
    context_sixteen = Message("   Go")

    symptoms = {
        "Headache": True,
        "Fever": True,
        "Cough": True,
        "Sore Throat": True,
        "Runny Nose": False,
        "Loss of Taste": True,
        "Nausea": True,
        "Chills": True,
        "Thirst": False,
        "Dry mouth": False,
        "Anxiety": False,
        "Hunger": False,
        "Dizziness": True,
        "Weight Loss": False,
    }

    global symptoms_list

    symptoms_list = list(symptoms.keys())

    pygame.mixer.Channel(1).set_volume(1)

    mole1 = Mole(
        136,
        436,
        "sprites/mole1.png",
        symptoms_list[random.randint(0, 13)],
        random.randint(0, 190),
    )
    mole2 = Mole(
        336,
        436,
        "sprites/mole2.png",
        symptoms_list[random.randint(0, 13)],
        random.randint(0, 190),
    )
    mole3 = Mole(
        536,
        436,
        "sprites/mole3.png",
        symptoms_list[random.randint(0, 13)],
        random.randint(0, 190),
    )
    mole4 = Mole(
        136,
        136,
        "sprites/mole4.png",
        symptoms_list[random.randint(0, 13)],
        random.randint(0, 190),
    )
    mole5 = Mole(
        336,
        136,
        "sprites/mole5.png",
        symptoms_list[random.randint(0, 13)],
        random.randint(0, 190),
    )
    mole6 = Mole(
        536,
        136,
        "sprites/mole6.png",
        symptoms_list[random.randint(0, 13)],
        random.randint(0, 190),
    )

    moles = [mole1, mole2, mole3, mole4, mole5, mole6]
        

    timeLeft = 90
    previousTime = int(get_elapsed_time())
    time_reset = False


def stage_one_logic():
    global playerscore, stage

    # If in-game, not in contextes
    if get_elapsed_time() > 40:

        # Gravity
        if player.y < 400:
            player.y += 2

        # Make enemy move to player
        if enemy.x < player.x:
            enemy.x += 3
        elif enemy.x > player.x:

            enemy.x -= 3

        # Make enemy fire germ
        if int(get_elapsed_time()) % 10 == 0:
            enemy.send_projectile()

        # Duh
        enemy.update_projectile()

        # Get distance between player center and enemy
        plrx, plry = player.x + 64, player.y + 64
        enmx, enmy = enemy.x + 64, enemy.y + 64
        difx = enmx - plrx
        dify = enmy - plry
        distance_between = math.sqrt(difx ** 2 + dify ** 2)

        # Defend against zero division
        if distance_between == 0:
            distance_between = 1

        # If in range
        if distance_between < 30:
            playerscore -= 0.1 / distance_between
            render_score((255, 0, 0))
        else:  # Make it so that the player can't take enemy damage and germ damage
            if enemy.projectile.y in range(
                player.y + 64 - 20, player.y + 64 + 20
            ) and enemy.projectile.x in range(player.x + 64 - 20, player.x + 64 + 20):
                enemy.send_projectile()
                playerscore -= 2
                render_score((255, 0, 0))
            else:
                playerscore += 0.005
                render_score((0, 255, 0))

        # Enemy teleportation
        if player.y < 300:
            if int(get_elapsed_time()) % 5 == 0:
                enemy.x = player.x

        # Teleport back to left
        if player.x > 800:
            player.x = -100

        # Teleport back to right
        if player.x < -100:
            player.x = 800

        # Duh
        player.update()

        # Enemy sneeze attack every 15 seconds
        if int(get_elapsed_time()) % 15 == 0:
            enemy.sneeze_attack()

        # Transition if high enough score
        if playerscore >= 20:
            stage = 2
            set_up()


def stage_two_logic():
    global previousTime, timeLeft
    
    for i in range(len(moles)):
        moles[i].ttl -= 1
        if moles[i].ttl < 0:
            moles[i].enabled = False
        if moles[i].ttl < -200:
            moles[i] = Mole(
                moles[i].x,
                moles[i].y,
                moles[i].sprite_path,
                symptoms_list[random.randint(0, 13)],
                random.randint(100, 190)
            )
            
            
    if int(get_elapsed_time()) > 60:
        if int(get_elapsed_time()) % 1 == 0:
            if not int(get_elapsed_time()) == previousTime:
                timeLeft -= 1
                previousTime = int(get_elapsed_time())
               
    
    if not pygame.mixer.Channel(0).get_busy():
        pygame.mixer.Channel(0).play(highoctane)

def stage_one_handle_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        if keys[pygame.K_LSHIFT]:
            if player.stamina > 0:
                player.x -= 4
            if int(get_elapsed_time()) % 1 == 0:
                player.stamina -= 2
        player.x -= 4

    if keys[pygame.K_d]:
        if keys[pygame.K_LSHIFT]:
            if player.stamina > 0:
                player.x += 4
            if int(get_elapsed_time()) % 1 == 0:
                player.stamina -= 2
        player.x += 4

    if keys[pygame.K_SPACE]:
        if player.y >= 400:
            player.isJumping = True
            player.jumpY = player.y

            pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds\jump.mp3"))


def stage_two_handle_input():
    global playerscore
    global moles

    if pygame.mouse.get_pressed()[0]:
        mousex, mousey = pygame.mouse.get_pos()
        for i in range(len(moles)):
            if moles[i].is_in_hitbox(mousex, mousey):
                moles[i].enabled = False

                if symptoms[moles[i].symptom]:
                    playerscore += 2
                    moles[i] = Mole(
                        moles[i].x,
                        moles[i].y,
                        moles[i].sprite_path,
                        symptoms_list[random.randint(0, 13)],
                        0
                    )
                    
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(r"sounds\ping.mp3"))
                else:
                    playerscore -= 4
                    
                    moles[i] = Mole(
                        moles[i].x,
                        moles[i].y,
                        moles[i].sprite_path,
                        symptoms_list[random.randint(0, 13)],
                        0
                    )
                    
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(r"sounds\uhoh.mp3"))


def stage_one_draw():
    if get_elapsed_time() < 5:
        context_one.draw()
    if 5 < get_elapsed_time() < 10:
        context_two.draw()
    if 10 < get_elapsed_time() < 15:
        context_three.draw()
    if 15 < get_elapsed_time() < 20:
        context_four.draw()
    if 20 < get_elapsed_time() < 25:
        context_five.draw()
    if 25 < get_elapsed_time() < 30:
        context_six.draw()
    if 30 < get_elapsed_time() < 32:
        context_seven.draw()
    if 32 < get_elapsed_time() < 36:
        context_eight.draw()
    if 36 < get_elapsed_time() < 40:
        context_nine.draw()

    if get_elapsed_time() > 40:
        player.draw()
        enemy.draw()
        enemy.draw_projectile()

        pygame.draw.line(win, (0, 0, 0), (0, 520), (800, 520))

        for i in range(0, 800, 30):
            pygame.draw.line(win, (30, 30, 30), (i, 520), (i, 550))

        feet.draw()

        field_layer = pygame.Surface((800, 800), pygame.SRCALPHA)

        pygame.draw.circle(
            field_layer,
            pygame.Color(255, 0, 0, 200),
            ((enemy.x + 64), (enemy.y + 64)),
            60,
            width=3,
        )

        pygame.draw.circle(
            field_layer,
            pygame.Color(255, 0, 0, 100),
            ((enemy.x + 64), (enemy.y + 64)),
            63,
            width=3,
        )

        pygame.draw.circle(
            field_layer,
            pygame.Color(255, 0, 0, 50),
            ((enemy.x + 64), (enemy.y + 64)),
            66,
            width=3,
        )

        pygame.draw.circle(
            field_layer,
            pygame.Color(255, 0, 0, 25),
            ((enemy.x + 64), (enemy.y + 64)),
            69,
            width=3,
        )

        win.blit(field_layer, (0, 0))


def render_score(color):
    textDraw = arial_big.render("Score: " + str(int(playerscore)), True, color)
    win.blit(textDraw, (330, 0))
    
def render_time_left():
    textDraw = arial_big.render(str(timeLeft), True, (0,0,0))
    win.blit(textDraw, (370, 700))
    


def stage_two_draw():
    global playerscore, startTime, time_reset

    if get_elapsed_time() < 5:
        context_one.draw()
    if 5 < get_elapsed_time() < 10:
        context_eleven.draw()
    if 10 < get_elapsed_time() < 15:
        context_two.draw()
    if 15 < get_elapsed_time() < 20:
        context_three.draw()
    if 20 < get_elapsed_time() < 25:
        context_four.draw()
    if 25 < get_elapsed_time() < 30:
        context_five.draw()
    if 30 < get_elapsed_time() < 32:
        context_six.draw()
    if 32 < get_elapsed_time() < 36:
        context_seven.draw()
    if 36 < get_elapsed_time() < 40:
        context_eight.draw()
    if 40 < get_elapsed_time() < 45:
        context_nine.draw()
    if 45 < get_elapsed_time() < 50:
        context_twelve.draw()
    if 50 < get_elapsed_time() < 54:
        context_thirteen.draw()
    if 54 < get_elapsed_time() < 56:
        context_fourteen.draw()
    if 56 < get_elapsed_time() < 58:
        context_fifteen.draw()
    if 58 < get_elapsed_time() < 60:
        context_sixteen.draw()
  
    if 60 < get_elapsed_time():
        for mole in moles:
            mole.draw()

        render_score((0, 255, 0))
        
    render_time_left()
    
    if timeLeft <= 0:
        
    
        if playerscore < 60:
        
            if time_reset:
                pass
            else:
                startTime = time.time()
                time_reset = True
            
            if get_elapsed_time() <= 5:
                Message("    Oops, you guessed the symptoms wrong!").draw()
            if 5 <= get_elapsed_time() <= 10:
                Message("    I'll let you play again!").draw()
            if 10 <= get_elapsed_time():
                set_up()
                startTime = 0
                playerscore = 25
        else:
            if time_reset:
                pass
            else:
                startTime = time.time()
                time_reset = True
        
            if get_elapsed_time() < 5:
                Message("    You win!").draw()
            if 5 < get_elapsed_time() < 10:
                Message("    Covid Game").draw()
            if 10 < get_elapsed_time() < 15:
                Message("    A set of educational minigames").draw()
            if 15 < get_elapsed_time() < 20:
                Message(" That teaches social distancing and symptom recognition!").draw()
            if 20 < get_elapsed_time() < 40:
                Message("   Thanks for playing, and good night!").draw()
            if get_elapsed_time() > 40:
                sys.exit()
            
def set_up():
    if stage == 1:
        stage_one_setup()
    elif stage == 2:
        stage_two_setup()


def handle_input():
    # Basic events
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    # Stage specific
    if stage == 1:
        stage_one_handle_input()
    elif stage == 2:
        stage_two_handle_input()


def logic():
    # Stage specific
    if stage == 1:
        stage_one_logic()
    elif stage == 2:
        stage_two_logic()


def draw():
    # Stage specific
    if stage == 1:
        stage_one_draw()
    elif stage == 2:
        stage_two_draw()


def get_elapsed_time():
    return time.time() - startTime


def main():
    global stage
    global win
    global startTime

    stage = 1

    win = pygame.display.set_mode((config["width"], config["height"]))

    pygame.display.set_caption(config["caption"])

    clock = pygame.time.Clock()

    startTime = time.time()

    set_up()

    while True:
        win.fill(config["bg_color"])
        handle_input()
        logic()
        draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
