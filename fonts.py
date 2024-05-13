import pygame as pg
import json
from datetime import datetime
import screeninfo
import string

monitor = screeninfo.get_monitors()[0]
pg.init()
w, h = monitor.width, monitor.height
screen = pg.display.set_mode((w, h))
pg.font.init()
fonts = pg.font.get_fonts()
saved_fonts = []

current_font_index = 0

file_name = f'saved/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json'

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                current_font_index -= 1
                if current_font_index < 0:
                    current_font_index = len(fonts) - 1
                    
            if event.key == pg.K_RIGHT:
                current_font_index += 1
                if current_font_index >= len(fonts):
                    current_font_index = 0
                    
            if event.key in [pg.K_SPACE, pg.K_RETURN]:
                saved_fonts.append(fonts[current_font_index])
                with open(file_name, 'w') as f:
                    json.dump(saved_fonts, f)
                    
                    
    screen.fill((15, 15, 15))
    
    font = pg.font.SysFont(fonts[current_font_index], 50)
    text = f'{string.ascii_lowercase} {string.ascii_uppercase}'
    rendered_text = font.render(text, True, (240, 240, 240))
    rect = rendered_text.get_rect()
    rect.center = (w//2, h//2)
    screen.blit(rendered_text, rect)
    
    bottom_pos = rect.bottom
    
    text = f'{string.digits} {string.punctuation}'
    rendered_text = font.render(text, True, (240, 240, 240))
    rect = rendered_text.get_rect()
    rect.center = (w//2, bottom_pos + 10 + rect.height//2)
    screen.blit(rendered_text, rect)
    
    font = pg.font.SysFont('arial', 50)
    text = f'{current_font_index+1}/{len(fonts)}'
    rendered_text = font.render(text, True, (240, 240, 240))
    rect = rendered_text.get_rect()
    rect.topleft = (10, 10)
    screen.blit(rendered_text, rect)
    
    
    
    pg.display.update()
pg.quit()
                    
        