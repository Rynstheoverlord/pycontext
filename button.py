import pygame

class TextButton:
	def __init__(self,surface,text = "",font_size = 30,button_color = pygame.Color('gray'),text_color = (0,0,0),x = 100,y = 100,width = 100,height = 50,command = None):
		self.x = x
		self.y = y 
		self.width = width 
		self.height = height 
		self.command = command 
		self.surface = surface
		self.button_color = button_color
		self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
		self.font_size = font_size
		self.font = pygame.font.SysFont(None,self.font_size)
		self.text = self.font.render(text,True,text_color)

	def update(self):
		pygame.draw.rect(self.surface,self.button_color,self.rect,2)
		self.surface.blit(self.text,(self.x + 10,self.y + 10))
		self.mousepos = pygame.mouse.get_pos()
		if self.rect.collidepoint(self.mousepos):
			if pygame.mouse.get_pressed()[0] == 1:
				if self.command != None:
					self.command()


class ImageButton:
	def __init__(self,surface,image,x = 100,y = 100,width = 50,height = 50,command = None):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.command = command
		self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
		self.image = pygame.transform.scale(image,(self.width,self.height))
		self.surface = surface

	def update(self):
		self.mousepos = pygame.mouse.get_pos()
		self.surface.blit(self.image,(self.x,self.y))
		if self.rect.collidepoint(self.mousepos):
			if pygame.mouse.get_pressed()[0] == 1:
				if self.command != None:
					self.command()

