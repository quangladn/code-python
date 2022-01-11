import pygame, sys, math, random, time

a = 640

pixel = 20
square = int(a / pixel)
speed_snake = 10

bg_color1 = (156,210,54)
bg_color2 = (147,203,57)
red = (255,0,0)
snake_color = (96,150,22)
black = (0,0,0)

class Snake:

	def __init__(self):
		self.color = snake_color
		self.head_X = random.randrange(0 ,a ,pixel )
		self.head_Y = random.randrange(0, a ,pixel )
		self.bodies = []
		self.body_color = 22
		self.state = "STOP"

	def move_head(self):
		if self.state == "up":
			self.head_Y -= pixel

		elif self.state == "down":
			self.head_Y += pixel
		
		elif self.state == "right":
			self.head_X += pixel

		elif self.state == "left":
			self.head_X -= pixel

	def move_body(self):
		if len(self.bodies) > 0:
			for i in range(len(self.bodies)-1,-1,-1):
				if i == 0:
					self.bodies[0].posX = self.head_X
					self.bodies[0].posY = self.head_Y
				else:
					self.bodies[i].posX = self.bodies[i-1].posX
					self.bodies[i].posY = self.bodies[i-1].posY

	def add_body(self):
		# self.body_color += 100
		body_S = Body_snake((96,150,self.body_color),self.head_X,self.head_Y)
		self.bodies.append(body_S)

	def die(self):
		self.head_X = random.randrange(0,a,pixel)
		self.head_Y = random.randrange(0,a,pixel)
		self.bodies = []
		self.state = "STOP"
		
	def draw(self,screen):
		pygame.draw.rect(screen, self.color, (self.head_X,self.head_Y,pixel,pixel))
		if len(self.bodies) > 0:
			for body_S in self.bodies:
				body_S.draw(screen)

class Body_snake:

	def __init__(self,color,posX,posY):
		self.color = color
		self.posX = posX
		self.posY = posY

	def draw(self,screen):
		pygame.draw.rect(screen, self.color, (self.posX,self.posY,pixel,pixel))

class Apple:
	def __init__(self):
		self.color = red
		self.spawn()

	def spawn(self):
		self.posX = random.randrange(0 , a, pixel)
		self.posY = random.randrange(0 , a, pixel)

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.posX,self.posY,pixel,pixel))

class Back_round:
	def draw(self,screen):
		screen.fill(bg_color1)
		counter = 0
		for row in range(square):
			for col in range(square):
				if counter % 2 == 0:
					pygame.draw.rect(screen, bg_color2,(col*pixel ,row*pixel ,pixel ,pixel ))
				if col != square -1:
					counter += 1

class Collision:

	def beween_snake_and_apple(self,snack,apple):
		distance = math.sqrt( math.pow((snack.head_X - apple.posX),2) + math.pow((snack.head_Y - apple.posY),2) )
		return distance < pixel

	def beween_snake_and_wall(self,snake):
		if snake.head_X < 0 or snake.head_X > a - pixel or snake.head_Y < 0 or snake.head_Y > a - pixel:
			return True
		return False

	def beween_snake_and_body(self,snake):
		for body_S in snake.bodies:
			distance = math.sqrt( math.pow((snake.head_X - body_S.posX),2) + math.pow((snake.head_Y - body_S.posY),2) )
			return distance < pixel
			return True
		return False

class Score:

	def __init__(self):
		self.points = 0
		self.font = pygame.font.SysFont('monospace',30,False)

	def increase(self):
		self.points += 1

	def reset(self):
		self.points = 0

	def show(self,screen):
		lbl = self.font.render('Score' + str(self.points),1,black)
		screen.blit(lbl,(5,5))
		
def main():
	pygame.init()
	screen = pygame.display.set_mode((a,a))
	pygame.display.set_caption('snack by quang')
	
	snake = Snake()	
	apple = Apple()
	bg = Back_round()
	collision = Collision()
	score = Score()

	while True:
		bg.draw(screen)
		snake.draw(screen)
		apple.draw(screen)
		score.show(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					if snake.state != "down":
						snake.state = "up"
				if event.key == pygame.K_DOWN:
					if snake.state != "up":
						snake.state = "down"
				if event.key == pygame.K_RIGHT:
					if snake.state != "left":
						snake.state = "right"
				if event.key == pygame.K_LEFT:
					if snake.state != "right":
						snake.state = "left"

				if event.key == pygame.K_SPACE:
					snake.state = "STOP"



		if collision.beween_snake_and_apple(snake,apple):
			apple.spawn()
			snake.add_body()
			score.increase()
		if snake.state != "STOP":
			snake.move_body()
			snake.move_head()
		
		if collision.beween_snake_and_wall(snake):
			snake.die()
			apple.spawn()
			score.reset()

		if collision.beween_snake_and_body(snake):
			snake.die()
			apple.spawn()
			score.reset()

		pygame.time.delay(120)

		pygame.display.update()
	pygame.quit()

main()

