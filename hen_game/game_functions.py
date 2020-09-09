import sys
import pygame
from basket import Basket
from hen import Hen
from time import sleep
import random
from egg_golden import Egg_G
from egg_white import Egg_W
from poop import Poop
import game_control as gc
import copy
from stats import GameStats 

#def start_game():

def check_events(basket,basket_h,play_btn,stats):
	
	for event in pygame.event.get():
		'''respond to keypresses and mouse moves'''
		#print(event.type)
		if event.type == pygame.QUIT:
	    	# without this the window does not get closed even after clicking the close button
			
			sys.exit()	
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, basket,basket_h)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, basket,basket_h)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(mouse_x,mouse_y,play_btn,stats)

def check_play_button(mouse_x,mouse_y,play_btn,stats):
	"""Start a new game when the player clicks Play."""
	button_clicked = play_btn.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		#Hide the mouse cursor
		pygame.mouse.set_visible(False)		
		stats.game_active = True
		stats.game_start_msg = True

		


def update_screen(cg_settings, screen,sb, basket_h,basket, hens, eggs_w,eggs_g, poops,stats,play_btn):
	"""Update images on screen and flip to new screen."""
	# Redraw the screen during each pass through the loop.
	screen.blit(cg_settings.background,[0,0])
	
	basket.blitme()
	basket_h.blitme()
	pygame.draw.line(screen, (100, 100, 255), (0, 190), (1200, 190))
	pygame.draw.line(screen, (100, 100, 255), (0, 191), (1200, 191))
	pygame.draw.line(screen, (100, 100, 255), (0, 192), (1200, 192))
	pygame.draw.line(screen, (100, 100, 255), (0, 193), (1200, 193))
	pygame.draw.line(screen, (100, 100, 255), (0, 194), (1200, 194))
	if(stats.game_active):	
		for hen in hens:
			hen.blitme()
		hen_number = random.randint(0,cg_settings.num_hens-1)
		if(stats.game_start_msg):
			stats.game_start_msg = False
			show_msg(screen,poops,eggs_w,eggs_g,"Starting game in ")
		#if(gc.hen_prev!=10):
			#hens[gc.hen_prev].image=pygame.image.load("images/hen.png")
		#pygame.display.update()
		hen_prev=3
			#print("changed")
		if gc.time_spent>gc.time_upper:
			do_something(hen_number,poops,eggs_w,eggs_g,screen,cg_settings,hens[random.randint(0,cg_settings.num_hens-1)])
			gc.time_spent=0
			gc.hen_prev = hen_number
			#print("is " ,hen_prev)
		# Make the most recently drawn screen visible.
		eggs_g.draw(screen)
		eggs_w.draw(screen)
		poops.draw(screen)
		gc.time_spent+=1
		sb.show_score()

	#play button
	if(not stats.game_active):
		pygame.mouse.set_visible(True)		
		play_btn.draw_button()
	pygame.display.flip()
	#if gc.egg_active:
		#gc.egg_active=False
		#sleep(5)
	

def check_keydown_events(event, basket,basket_h):
	"""Respond to keypresses"""
	if event.key == pygame.K_RIGHT:
		basket_h.moving_right=True
		basket.moving_right=True
	elif event.key == pygame.K_LEFT:
		basket_h.moving_left=True	
		basket.moving_left=True	
	elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
		sys.exit()	
	

def check_keyup_events(event, basket, basket_h):
	if event.key == pygame.K_RIGHT:
		basket_h.moving_right=False
		basket.moving_right=False	
	elif event.key == pygame.K_LEFT:
		basket_h.moving_left=False
		basket.moving_left=False

def create_fleet(cg_settings, screen, hens):
	"""create fleet of hens."""

	hen = Hen(cg_settings, screen)	
	hen_width= hen.rect.width
	#available_space_x = cg_settings.screen_width - 2*hen_width
	#number_hens_x = int(available_space_x/(2*hen_width))
	number_hens_x = cg_settings.num_hens
	#create the row of hens
	if(len(hens)!=0):
		hen = Hen(cg_settings, screen)
		hen.rect.x = hen_width + 2*(cg_settings.num_hens-1)*hen_width
		hens.append(hen)
		return
	for hen_number in range(number_hens_x):
		#create the hen and place it in the row
		hen = Hen(cg_settings, screen)
		hen.rect.x = hen_width + 2*hen_number*hen_width
		hens.append(hen)




def eggs_w_update(eggs,basket_h,gs,score):
	
	for egg in eggs.copy():
		if egg.rect.bottom>=1200:
			eggs.remove(egg)
			#gc.egg_active-=1;
	egg_basket_collision(eggs,basket_h,gs,score)
	eggs.update()		

def eggs_g_update(eggs,basket_h,gs,score):
	for egg in eggs.copy():
		if egg.rect.bottom>=1200:
			eggs.remove(egg)
			#gc.egg_active-=1;	
	egg_basket_collision(eggs,basket_h,gs,score)
	eggs.update()				

def poops_update(poops,basket_h,gs,score):
	poops.update()
	for poop in poops.copy():
		if poop.rect.bottom>=1200:
			poops.remove(poop)
			#gc.egg_active-=1;	
	poop_basket_collision(poops,basket_h,gs,score)				

def do_something(what,poops,eggs_w,eggs_g,screen,cg_settings,hen):
	#hen.image = pygame.image.load("images/poop21.png")
	#pygame.display.update()
	if what==0:
		poop = Poop(screen,cg_settings)
		rect = hen.rect
		poop_x = rect.centerx
		poop_y = rect.bottom
		poop.rect.x=poop_x
		poop.y=float(poop_y)
		poop.rect.y=poop.y
		#gc.egg_active+=1
		poops.add(poop)
	elif what==1:
		egg = Egg_W(screen,cg_settings)
		
		rect = hen.rect
		egg_x = rect.centerx
		egg_y = rect.bottom
		egg.rect.x=egg_x
		egg.y=float(egg_y)
		egg.rect.y=egg.y
		gc.egg_active+=1
		eggs_w.add(egg)
	elif what==2:
		egg = Egg_G(screen,cg_settings)
		
		rect = hen.rect
		egg_x = rect.centerx
		egg_y = rect.bottom
		egg.rect.x=egg_x
		egg.y=float(egg_y)
		egg.rect.y=egg.y
		gc.egg_active+=1
		eggs_g.add(egg)	
	#hen.image = pygame.image.load("images/hen.png")	

def egg_basket_collision(eggs,basket,gs,score):
	
	if pygame.sprite.spritecollide(basket, eggs,True):#,usethis):
		#eggs.remove(egg)
	#for egg in eggs.copy():
	#	if egg.rect.top>basket.rect.top:
	#		eggs.remove(egg)
		
		gs.score+=score



def poop_basket_collision(poop,basket,gs,score):
	#for egg in eggs:
	if pygame.sprite.spritecollide(basket, poop,True):
		#eggs.remove(egg)
		gs.score+=score
		print("pooop in basket")


def usethis(basket,egg):
	if basket.rect.left<egg.rect.left and basket.rect.right>egg.rect.right:
		print(basket.rect.top+20,egg.rect.bottom ,basket.rect.top/2 )
		if 0<egg.rect.bottom :#and egg.rect.bottom<basket.rect.top/2:
			print(basket.rect.top)
			return True
	else:
		return False 		

def check_level_crossed(cg_settings, screen,sb, basket_h,basket, hens, eggs_w,eggs_g, poops,stats,player_name):
	n = stats.level
	base_score = cg_settings.base_level_score
	if((base_score*(n*(n+1)/2))<=stats.score):
		cg_settings.poop_speed_factor = cg_settings.poop_speed_factor+cg_settings.drop_speed_increase 
		cg_settings.egg_speed_factor+=cg_settings.drop_speed_increase
		stats.level+=1	
		
		if stats.level>3 and not cg_settings.num_hens==4:
			cg_settings.num_hens=4
			create_fleet(cg_settings, screen, hens)
		
		if stats.level == 4:
			stats.game_active = False
			show_win_msg(screen,player_name+" you Win!! ")
			return


		show_msg(screen,poops,eggs_w,eggs_g,"Levelling up in ")
		

def show_msg(screen,poops,eggs_w,eggs_g,msg):
	#rounded_score = int(round(self.stats.score, -1))
	font = pygame.font.SysFont(None, 100)
	#score_str = "{:,}".format()
	text_color = (0,117,138)
	
	screen_rect = screen.get_rect()
	score_image = font.render(msg+str(3)+" seconds",True,text_color,(2,4,88))
	#display  the score at the top right of the screen.
	score_rect = score_image.get_rect()
	score_rect.centerx = screen_rect.centerx
	score_rect.centery = screen_rect.centery
	
	screen.blit(score_image,score_rect)	
	pygame.display.flip()
	sleep(1)
	score_image = font.render(msg+str(2)+" seconds",True,text_color,(2,4,88))
	screen.blit(score_image,score_rect)	
	pygame.display.flip()
	sleep(1)
	score_image = font.render(msg+str(1)+" seconds",True,text_color,(2,4,88))
	screen.blit(score_image,score_rect)	
	pygame.display.flip()
	sleep(1)
	#update_screen(cg_settings, screen,sb, basket_h,basket, hens, eggs_w,eggs_g, poops)

def show_win_msg(screen,msg):
	#rounded_score = int(round(self.stats.score, -1))
	font = pygame.font.SysFont(None, 100)
	#score_str = "{:,}".format()
	text_color = (0,117,138)
	
	screen_rect = screen.get_rect()
	score_image = font.render(msg,True,text_color,(2,4,88))
	#display  the score at the top right of the screen.
	score_rect = score_image.get_rect()
	score_rect.centerx = screen_rect.centerx
	score_rect.centery = screen_rect.centery
	screen.blit(score_image,score_rect)	
	pygame.display.flip()
	sleep(5)










				







