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

scale = w / 2560

current_font_index = 0

star_image = pg.image.load('star.png')
star_image = pg.transform.scale(star_image, (int(star_image.get_width()*scale), int(star_image.get_height()*scale)))
star_image_rect = star_image.get_rect()
star_image_rect.topright = (w-20, 20)

star_filled_image = pg.image.load('star_filled.png')
star_filled_image = pg.transform.scale(star_filled_image, (int(star_filled_image.get_width()*scale), int(star_filled_image.get_height()*scale)))
star_filled_image_rect = star_filled_image.get_rect()
star_filled_image_rect.topright = (w-20, 20)

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
                if fonts[current_font_index] in saved_fonts:
                    saved_fonts.remove(fonts[current_font_index])
                else:
                    saved_fonts.append(fonts[current_font_index])
                with open(file_name, 'w') as f:
                    json.dump(saved_fonts, f)
                    
                    
    screen.fill((15, 15, 15))
    
    font = pg.font.SysFont(fonts[current_font_index], int(50*scale))
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
    
    font = pg.font.SysFont('arial', int(50*scale))
    text = f'{current_font_index+1}/{len(fonts)}'
    rendered_text = font.render(text, True, (240, 240, 240))
    rect = rendered_text.get_rect()
    rect.topleft = (20, 20)
    screen.blit(rendered_text, rect)
    
    font = pg.font.SysFont('arial', int(30*scale))
    text = f'press space to save font'
    rendered_text = font.render(text, True, (240, 240, 240))
    rect = rendered_text.get_rect()
    rect.bottomright = (w-20, h-20)
    screen.blit(rendered_text, rect)
    
    if fonts[current_font_index] in saved_fonts:
        screen.blit(star_filled_image, star_filled_image_rect)
    else:
        screen.blit(star_image, star_image_rect)
    
    
    
    pg.display.update()
pg.quit()
                    
        