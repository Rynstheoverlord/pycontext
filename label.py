import pygame

class TextLabel:
	def __init__(self,surface,text,x = 100,y = 100,font_size = 30,font_style = None,text_color = (255,255,255)):
		self.surface = surface
		self.text = text
		self.x = x 
		self.y = y 
		self.font_size = font_size
		self.font_style = font_style
		self.text_color = text_color
		
		self.font = pygame.font.SysFont(self.font_style,self.font_size)

	def update(self):
		text = self.font.render(self.text,True,self.text_color)
		self.surface.blit(text,(self.x,self.y))

class ImageLabel:
	def __init__(self,surface,image_path,x = 100,y = 100,width = 100,height = 100,flip_x = False,flip_y = False,rotation = 0):
		self.surface = surface
		self.image_path = image_path
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.flip_x = flip_x
		self.flip_y = flip_y
		self.rotation = rotation
		self.image = pygame.transform.rotate(pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.image_path),(self.width,self.height)),self.flip_x,self.flip_y),self.rotation)


	def update(self):
		self.surface.blit(self.image,(self.x,self.y))
