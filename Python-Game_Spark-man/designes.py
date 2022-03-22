#main_screen()
#tavern_screen()
#market_screen()
#attack_wait_screen()
#attack_hero_action_screen()
#attack_monster_action_screen()
#choice_screen()
#magic_screen()
#hero_dead_screen()
#hero_win_screen()

import characters as chr

def main_screen():
    print("""
                                      --------------------------------------
                                      |                                    |
                                      |         S P A R K - M A N          |
                                      |                                    |
                                      |     1 - START GAME                 |
                                      |     2 - QUIT GAME                  |
                                      |                                    |
                                      --------------------------------------
    """)


def choice_screen():
    print("""
                                      --------------------------------------
                                      |    ____________________________    |
                                      |   | < < <        T A V E R N A |   |            
                                      |   | M A R K E T          > > > |   |
                                      |   | < < <          B Ü Y Ü C Ü |   |
                                      |   | A R E N A            > > > |   |
                                      |    ----------------------------    |
                                      |                ||||                |
                                      |                ||||                |
                                      |                ||||                |
                                      |/\/\/\/\/\/\/\/\||||/\/\/\/\/\/\/\/\|
                                      --------------------------------------
                                      
                                        1 - TAVERNA
                                        2 - MARKET
                                        3 - BÜYÜCÜ
                                        4 - ARENA
                                        
    ************************************************************************************************************
    """)


def magic_screen():
    print("""
                                      --------------------------------------
                                      |  __    __    __      >>(O)<<       |
                                      |  )(    )(    )(       |o o |||     |
                                      | (--)  (--)  (--)       \- / |||    |
                                      |                        /---|||||   |
                                      |                \__/===/( ( |||||   |
                                      |                       ||   |||||   |
                                      --------------------------------------


    EZGİ: Esikisi gibi koşup canavar mı ödürmek istiyorsun. Ver parayı al canını!

    (can 50-100 arasında iyileşir) ------> (150 gold)
    
    1 - AL
    2 - GERİ DÖN

    ************************************************************************************************************
    """)

def tavern_screen(): # tavernacı görkem olacak
    print("""
                                      --------------------------------------
                                      |                      _____         |
                                      |                   __|_____|___     |
                                      |                      |- - |        |
                                      |                     __\^ /__       |
                                      |                 / /{   ||   }\ \   |
                                      |                / /  {  ||  }  \ \  |
                                      --------------------------------------
                                      
                                      
    Görkem: Stresini atmak ister misin savaşçı? içeride tutuşmuş sönmeyi bekleyen kadınlarım var,alev at yeter!
    
    (can 10-40 arasında iyileşir) ------> (80 gold)
    
    1 - AL
    2 - GERİ DÖN
    
    ************************************************************************************************************
    """)

def market_screen():
    print("""
                                      --------------------------------------
                                      |    _|_        ||        ___    ___ |
                                      |   / | \     <<||>>     /   \__/   \|
                                      |     |         /        |          ||
                                      |     |         \         \________/ |
                                      |     |         /         /________\ |
                                      |     |         \                    |
                                      --------------------------------------
                                      
    Engin: yeni çıktı közden. almayan düşer gözden! ASKPAVA!            (Allah sağlık kuvvet para versin. amin!)
    
    1 - ardıç kılıç - - - - - - ( 50 gold)   ->  +15 AP
    2 - kadim kılıç - - - - - - (150 gold)   ->  +35 AP
    3 - görkemli zırh - - - - - (300 gold)   -> +200 HP
    4 - GERİ DÖN

    ************************************************************************************************************
    """)

def attack_wait_screen():
    print("""
                                      --------------------------------------
                                      |                                    |
                                      |      (00)    /     \     (00)      |
                                      |      /||\   /       \   /(  )\     |
                                      |     / || \=/         \=/  ()  \    |
                                      |       /\                  /\       |
                                      |      |_ \_               /  \      |
                                      --------------------------------------
    
                                      1 - * * * * * * * * *  kafasına saldır
                                      2 - * * * * * * * * * * göğsüne saldır
                                      3 - * * * * * * * * * * ayağına saldır
                                      4 - * * * * * * * * * * * * * * dinlen
    
    ************************************************************************************************************
    """)


def attack_hero_action_screen():
    print("""
                                      --------------------------------------
                                      |                                    |
                                      |           (00)    /\     (00)      |
                                      |           /||\   /  \   /(  )\     |
                                      |          / || \=/    \=/  ()  \    |
                                      |            /\             /\       |
                                      |           |_ \_          /  \      |
                                      --------------------------------------





    ************************************************************************************************************
    """)

def attack_hero_miss_screen():
    print("""
                                      --------------------------------------
                                      |                  ISKA              |
                                      |           (00)    /\     (00)      |
                                      |           /||\   /  \   /(  )\     |
                                      |          / || \=/    \=/  ()  \    |
                                      |            /\             /\       |
                                      |           |_ \_          /  \      |
                                      --------------------------------------





    ************************************************************************************************************
    """)


def attack_monster_action_screen():
    print("""
                                      --------------------------------------
                                      |                                    |
                                      |      (00)    /\     (00)           |
                                      |      /||\   /  \   /(  )\          |
                                      |     / || \=/    \=/  ()  \         |
                                      |       /\             /\            |
                                      |      |_ \_          /  \           |
                                      --------------------------------------

 
 


    ************************************************************************************************************
    """)


def attack_monster_miss_screen():
    print("""
                                      --------------------------------------
                                      |             ISKA                   |
                                      |      (00)    /\     (00)           |
                                      |      /||\   /  \   /(  )\          |
                                      |     / || \=/    \=/  ()  \         |
                                      |       /\             /\            |
                                      |      |_ \_          /  \           |
                                      --------------------------------------





    ************************************************************************************************************
    """)

def hero_dead_screen():
    print("""
                                      --------------------------------------
                                      |                                    |
                                      |    _________       \     (00)      |
                                      |   ||-------||       \   /(  )\     |
                                      |   || R.I.P ||        \=/  ()  \    |
                                      |   ||       ||             /\       |
                                      |   ||       ||            /  \      |
                                      --------------------------------------



                                                    Ö L D Ü N
    
    
    ************************************************************************************************************
    """)


def hero_win_screen():
    print("""
                                      --------------------------------------
                                      |                                    |
                                      |      (00)    /       _________     |
                                      |      /||\   /       ||-------||    |
                                      |     / || \=/        || R.I.P ||    |
                                      |       /\            ||       ||    |
                                      |      |_ \_          ||       ||    |
                                      --------------------------------------


                                                    Z A F E R


    ************************************************************************************************************
    """)

def durum():
    print("""************************************************************************************************************
        """)
    print(
        f"HP: {chr.hero.hp}  AP: {chr.hero.ap}  GOLD: {chr.hero.gold}                        HP: {chr.monster.hp}  AP: {chr.monster.ap}  GOLD: {chr.monster.gold}")
