import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gameproject.settings")
import django
django.setup()

from halligalli.models import Player
from halligalli.models import Card

if __name__=='__main__':

    Player(player_name = 'Computer1', comment = 'None', card_num =15, score = 0, current_card = 'None', bell_flag = 0).save()
    Player(player_name = 'Computer2', comment = 'None', card_num =15, score = 0, current_card = 'None', bell_flag = 0).save()
    Player(player_name = 'Computer3', comment = 'None', card_num =15, score = 0, current_card = 'None', bell_flag = 0).save()
    Player(player_name = 'User', comment = 'None', card_num =6, score = 0, current_card = 'None', bell_flag = 0).save()

    Card(owner= 'None', card_info ={1: 'banana, 1', 2:'banana, 2', 3:'banana, 3', 4: 'banana, 4', 5: 'banana, 5'
    ,6: 'strawberry, 1', 7:'strawberry, 2', 8:'strawberry, 3', 9: 'strawberry, 4', 10: 'strawberry, 5'
    ,11: 'plum, 1', 12:'plum, 2', 13:'plum, 3', 14: 'plum, 4', 15: 'plum, 5'
    ,16: 'lime, 1', 17:'lime, 2', 18:'lime, 3', 19: 'lime, 4', 20: 'lime, 5'}).save()