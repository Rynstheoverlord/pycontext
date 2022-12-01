import pygame

pygame.init()

class App:
	def __init__(self,size,title = "PyContext",color = (0,0,0)):
		self.size = size
		self.title = title
		self.color = color

	def init(self):
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption(self.title)
		return self.screen

	def background_color(self):
		self.screen.fill(self.color)

	def background_image(self,image_path):
		image = pygame.transform.scale(pygame.image.load(image_path),self.size)
		self.screen.blit(image,(0,0))


	def mainloop(self,update):
		self.update = update
		run = True
		while run: 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False


			self.background_color()
			self.update()
			pygame.display.update()

		pygame.quit()
		quit()
