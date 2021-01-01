import pygame
pygame.init()
win=pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")
clock=pygame.time.Clock()
walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')

bulletsound=pygame.mixer.Sound('music/bullet.mp3')
hitsound=pygame.mixer.Sound('music/hit.mp3')
music=pygame.mixer.music.load('music/music.mp3')
pygame.mixer.music.play(-1)
score=0

class player(object):
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.v=5
		self.isJump=False
		self.left=False
		self.jumpcount=10
		self.right=False
		self.walkcount=0
		self.standing=True
		self.hitbox=(self.x+17,self.y+11,29,52)
	def draw(self,win):
		if self.walkcount+1>=27:
			self.walkcount=0
		if not(self.standing):
			if self.left:
				win.blit(walkLeft[self.walkcount//3],(self.x,self.y))
				self.walkcount+=1
			elif self.right:
				win.blit(walkRight[self.walkcount//3],(self.x,self.y))
				self.walkcount+=1
		else:
			if self.right:
				win.blit(walkRight[0],(self.x,self.y))
			else:
				win.blit(walkLeft[0],(self.x,self.y))
		self.hitbox=(self.x+17,self.y+11,29,52)
		#pygame.draw.rect(win,(255,0,0),self.hitbox,2)
	def hit(self):
		self.isJump=False
		self.jumpcount=10
		self.x=60
		self.y=410
		self.walkcount=0
		font1=pygame.font.SysFont('ComicSans',100)
		text=font1.render("-5",1,(255,0,0))
		win.blit(text,(250-(text.get_width()/2),200))
		pygame.display.update()
		i=0
		while i<100:
			pygame.time.delay(10)
			i+=1
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					i=301
					pygame.quit()
class projectile(object):
	def __init__(self,x,y,radius,color,facing):
		self.x=x
		self.y=y
		self.radius=radius
		self.color=color
		self.facing=facing
		self.v=8*facing
	def draw(self,win):
		pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
class enemy(object):
	walkRight = [pygame.image.load('images/R1E.png'), pygame.image.load('images/R2E.png'), pygame.image.load('images/R3E.png'), pygame.image.load('images/R4E.png'), pygame.image.load('images/R5E.png'), pygame.image.load('images/R6E.png'), pygame.image.load('images/R7E.png'), pygame.image.load('images/R8E.png'), pygame.image.load('images/R9E.png'), pygame.image.load('images/R10E.png'), pygame.image.load('images/R11E.png')]
	walkLeft = [pygame.image.load('images/L1E.png'), pygame.image.load('images/L2E.png'), pygame.image.load('images/L3E.png'), pygame.image.load('images/L4E.png'), pygame.image.load('images/L5E.png'), pygame.image.load('images/L6E.png'), pygame.image.load('images/L7E.png'), pygame.image.load('images/L8E.png'), pygame.image.load('images/L9E.png'), pygame.image.load('images/L10E.png'), pygame.image.load('images/L11E.png')]
	def __init__(self,x,y,width,height,end):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.end=end
		self.path=[self.x,self.end]
		self.walkcount=0
		self.v=3
		self.hitbox=(self.x+17,self.y+2,31,57)
		self.health=10
		self.visible=True
	def draw(self,win):
		self.move()
		if self.visible:
			if self.walkcount+1>=33:
				self.walkcount=0
			if self.v>0:
				win.blit(self.walkRight[self.walkcount//3],(self.x,self.y))
				self.walkcount+=1
			else:
				win.blit(self.walkLeft[self.walkcount//3],(self.x,self.y))
				self.walkcount+=1		
			pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
			pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,50-((5)*(10-self.health)),10))
			self.hitbox=(self.x+17,self.y+2,31,57)
			#pygame.draw.rect(win,(255,0,0),self.hitbox,2)
	def move(self):
		if self.v>0:
			if self.x + self.v < self.path[1]:
				self.x+=self.v
			else:
				self.v=self.v*(-1)
				self.x+=self.v
				self.walkcount=0
		else:
			if self.x-self.v>self.path[0]:
				self.x+=self.v
			else:
				self.v=self.v*(-1)
				self.x+=self.v
				self.walkcount=0
	def hit(self):
		if self.health>0:
			self.health-=1
		else:
			self.visible=False
		print("hit")
	
font=pygame.font.SysFont('comicsans',30,True,True)
man=player(300,410,64,64)
goblin=enemy(100,410,64,64,450)
run=True
shootloop=0
bullets=[]
def redrawGameWindow():
	win.blit(bg,(0,0))
	text=font.render('Score: '+str(score),1,(0,0,0))
	win.blit(text,(390,10))
	man.draw(win)
	goblin.draw(win)
	for bullet in bullets:
		bullet.draw(win)
	pygame.display.update()
while run:
	clock.tick(27)
	if goblin.visible==True:
		if man.hitbox[1]<goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1]+man.hitbox[3]>goblin.hitbox[1]:
				if man.hitbox[0]+man.hitbox[2]>goblin.hitbox[0] and man.hitbox[0]<goblin.hitbox[0]+goblin.hitbox[2]:
					man.hit()
					score-=5
	if shootloop>0:
		shootloop+=1
	if shootloop>3:
		shootloop=0
	for bullet in bullets:
		if bullet.y-bullet.radius<goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1]:
			if bullet.x+bullet.radius>goblin.hitbox[0] and bullet.x-bullet.radius<goblin.hitbox[0]+goblin.hitbox[2]:
				hitsound.play()
				goblin.hit()
				score+=1
				bullets.pop(bullets.index(bullet))
		if bullet.x<500 and bullet.x>0:
			bullet.x+=bullet.v
		else:
			bullets.pop(bullets.index(bullet))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_SPACE] and shootloop==0:
		bulletsound.play()
		if man.left:
			facing=-1
		else:
			facing=1
		if len(bullets)<5:
			bullets.append(projectile(int(man.x+man.width//2),int(man.y+man.height//2),6,(0,0,0),facing))
		shootloop=1
	if keys[pygame.K_LEFT] and man.x>man.v:
		man.x-=man.v
		man.left=True
		man.right=False 
		man.standing=False
	elif keys[pygame.K_RIGHT] and man.x<500-man.width-man.v:
		man.x+=man.v
		man.right=True
		man.left=False
		man.standing=False
	else:
		man.standing=True
		man.walkcount=0
	if not(man.isJump):
		if keys[pygame.K_UP]:
			man.isJump=True
	else:
		if man.jumpcount>=-10:
			neg=1
			if man.jumpcount<0:
				neg=-1
			man.y-=(man.jumpcount**2)*0.5*neg
			man.jumpcount-=1
		else:
			man.isJump=False
			man.jumpcount=10
	redrawGameWindow()
pygame.quit()
