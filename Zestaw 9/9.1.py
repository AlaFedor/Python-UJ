import sys
import pygame
import random

pygame.init()
font = pygame.font.Font(None, 40)

NEW_BOX_EVENT = pygame.USEREVENT + 1 
pygame.time.set_timer(NEW_BOX_EVENT, 1000)

# COLORS
black = (0, 0, 0)
gray = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

RUNNING = 1
OVER = 0
game_state = RUNNING

POINTS = 0
TOTAL = 0

# INITIALIZE THE GAME
pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('padający śnieg')

# CLOCK
FPS = 60
clock = pygame.time.Clock()

boxes = []

def create_new_box():
    box_width = 50
    box_height = 60
    
    random_x = random.randint(0, width - box_width)
    new_rect = pygame.Rect(random_x, 0, box_width, box_height)

    return {
        'rect': new_rect,
        'speed': [0, random.randint(1, 3)],
        'visible': True
    }


# MAIN GAME LOOP
while True:
    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # QUIT Event
            pygame.quit()   # deaktywacja pygame
            sys.exit(0)

        elif event.type == NEW_BOX_EVENT:
            if game_state == RUNNING:
                boxes.append(create_new_box())
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == RUNNING:
                for box_data in boxes:
                    if box_data['visible'] and box_data['rect'].collidepoint(event.pos):
                        box_data['visible'] = False
                        print("event down dict {}".format(event.__dict__))
                        POINTS = POINTS + 1
                        break
            elif game_state == OVER:
                game_state = RUNNING
                boxes = []


    # INPUT
    new_boxes = []
    
    for box_data in boxes:
        if box_data['visible']:
            box_data['rect'] = box_data['rect'].move(box_data['speed'])
            
            if box_data['rect'].bottom > height:
                print("gra skonczona, sniezka dotknęła ziemi")
                game_state = OVER
                TOTAL = POINTS
                POINTS = 0 
                break
            else:
                new_boxes.append(box_data)
                
    boxes = new_boxes

    # DRAWING
    screen.fill(black)   # na nowo rysujemy pusty czarny ekran
    if game_state == RUNNING:
        text = font.render(f"kliknij w śnieżke i nie pozwól jej dotknąć ziemi   PUNKTY:{POINTS}", True, white)
        text_rect = text.get_rect(center=(width//2,height//20))
        screen.blit(text, text_rect)

        for box_data in boxes:
            if box_data['visible']:
                pygame.draw.rect(screen, white, box_data['rect'])
    else:
        text = font.render(f"twój wynik to {TOTAL} punktów, kliknij żeby zagrać ponownie", True, white)
        text_rect = text.get_rect(center=(width//2,height//2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    # Ograniczamy pętlę while do max FPS przebiegów na sekundę.
    # Bez tej instrukcji pętla biegnie zgodnie z wydajnością CPU.
    clock.tick(FPS)   # na początku lub na końcu pętli while