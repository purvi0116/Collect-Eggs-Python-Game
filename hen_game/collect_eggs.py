import sys
from settings import Settings
from pygame.sprite import Group
from basket_h import Basket_hidden
from basket import Basket
import game_functions as gf
import pygame
from egg_golden import Egg_G
from egg_white import Egg_W
from poop import Poop
from stats import GameStats 
from scoreboard import Scoreboard
from pygame import mixer
from Button import Button

def run_game(player_name):
	# Initialize game and create a screen object.
	pygame.init()
	cg_settings = Settings()
	screen = pygame.display.set_mode((cg_settings.screen_width, cg_settings.screen_height))
	pygame.display.set_caption("Collect the Eggs!")

	#Make a play button
	play_btn = Button(screen,"Let's Play!!")
	
	#make hidden bsket
	basket_h = Basket_hidden(cg_settings,screen)
	# Make a basket.
	basket = Basket(cg_settings,screen)
	# Make a group of hens.
	hens = []
	#eggs
	eggs_w=Group()
	eggs_g=Group()
	#poops
	poops=Group()
	
	gs = GameStats(cg_settings)
	sb  = Scoreboard(cg_settings,screen,gs)
	sb.prep_score()


	#create the fleet of hens
	gf.create_fleet(cg_settings, screen, hens)
	while True:
		gf.check_events(basket,basket_h,play_btn,gs)
		basket.update()
		basket_h.update(basket)
		gf.eggs_g_update(eggs_g,basket_h,gs,cg_settings.golden_score)
		gf.eggs_w_update(eggs_w,basket_h,gs,cg_settings.white_score)
		gf.poops_update(poops,basket_h,gs,cg_settings.poop_score)
		sb.prep_score()
		if(gs.score>gs.high_score):
			gs.high_score=gs.score
	
		sb.prep_high_score()
		sb.prep_level()

		#gf.create_egg(screen,egg)
		gf.update_screen(cg_settings, screen,sb,basket_h, basket, hens, eggs_w,eggs_g,poops,gs,play_btn)
		gf.check_level_crossed(cg_settings, screen,sb, basket_h,basket, hens, eggs_w,eggs_g, poops,gs,player_name)

print("PLEASE ENTER YOUR NAME!")	
player_name = raw_input()
run_game(player_name)		