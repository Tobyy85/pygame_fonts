import pygame as pg

class Text():
    auto_scale: float = None
    instances = []
    @staticmethod
    def change_auto_scale(scale: float):
        Text.auto_scale = scale
    
    def __init__(self, font: pg.font, text: str, color: tuple | str, x_pos: int, y_pos: int, surface: pg.surface.Surface, part: str = 'center', id: str = None):
        if len(color) != 3:
            raise TypeError(f'color takes 3 arguments ({len(color)} given)')
        if isinstance(color, str):
            c =  color.strip('#')
            color = tuple(int(c[i:i+2], 16) for i in (0, 2, 4))
        if isinstance(font, tuple):
            for c in color:
                if not isinstance(c, int):
                    raise TypeError('color values must be int')
                if not (0 <= c <= 255):
                    raise ValueError('color values must be between 0 and 255')
        if isinstance(font, tuple):
            self.original_font = font
            if Text.auto_scale is not None:
                font = (font[0], int(font[1] * Text.auto_scale/100))
            font = pg.font.SysFont(font[0], font[1])
        if isinstance(surface, pg.surface.Surface):
            self.surface = surface
        else:
            raise TypeError('surface must be pygame.surface.Surface')
        self.original_x = x_pos
        self.original_y = y_pos
        self.font = font
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.part = part
        self.color = color
        self.id = id
        self.text_ = self.font.render(str(self.text), True, self.color)
        self.rect = self.text_.get_rect()
        self.set_part(self.part)
        Text.instances.append(self)


    def set_part(self, part : str):
        if part == 'center':
            self.rect.center = (self.x_pos, self.y_pos)
        elif part == 'topleft':
            self.rect.topleft = (self.x_pos, self.y_pos)
        elif part == 'bottomright':
            self.rect.bottomright = (self.x_pos, self.y_pos)
        elif part == 'topright':
            self.rect.topright = (self.x_pos, self.y_pos)
        elif part == 'bottomleft':
            self.rect.bottomleft = (self.x_pos, self.y_pos)
        elif part == 'midtop':
            self.rect.midtop = (self.x_pos, self.y_pos)
        elif part == 'midbottom':
            self.rect.midbottom = (self.x_pos, self.y_pos)
        elif part == 'midleft':
            self.rect.midleft = (self.x_pos, self.y_pos)
        elif part == 'midright':
            self.rect.midright = (self.x_pos, self.y_pos)
        else:
            self.rect.center = (self.x_pos, self.y_pos)
            raise ValueError('Enter valid part')
        
        
    def flip(self, flip_x: bool, flip_y: bool):
        self.text_ = pg.transform.flip(self.text_, flip_x, flip_y)
        self.rect = self.text_.get_rect()
        self.set_part(self.part)


    def draw(self):
        self.surface.blit(self.text_, self.rect)
        
    
    def scale(self, precent, original: bool = True):
        if original:
            self.font = pg.font.SysFont(self.original_font[0], int(self.original_font[1]/100 * precent))
        else:
            self.font = pg.font.SysFont(self.original_font[0], int(self.font.size(self.text)[1]/100 * precent))
        self.text_ = self.font.render(str(self.text), True, self.color)
        self.rect = self.text_.get_rect()
        self.set_part(self.part)
        
        

    def change_text(self, text: str):
        self.text = text
        self.text_ = self.font.render(str(self.text), True, self.color)
        self.rect = self.text_.get_rect()
        self.set_part(self.part)
        
        
