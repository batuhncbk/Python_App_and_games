import designes as dsgn
import characters as chr
import random as rdm

market_1 = False
market_2 = False
market_3 = False
lvl = 0

print(dsgn.main_screen())
cvp = int(input())


if cvp != 1:
    print("ÇIKIŞ YAPILIYOR")

while 1:
    print("""************************************************************************************************************
    """)
    print(f"HP: {chr.hero.hp}    AP: {chr.hero.ap}      GOLD: {chr.hero.gold}")


    dsgn.choice_screen()                  #seçim ekranı: 1-taverna 2-market 3-büyücü 4-arena
    cvp = int(input())
    if cvp == 1:
        dsgn.tavern_screen()              #taverna sayfasına giriş

        print("""************************************************************************************************************
            """)
        print(f"HP: {chr.hero.hp}    AP: {chr.hero.ap}      GOLD: {chr.hero.gold}")

        cvp = int(input())
        if cvp == 1:
            if chr.hero.gold > 80:
                chr.hero.hp = chr.hero.hp + rdm.randint(10, 40)
                chr.hero.gold = chr.hero.gold-80
            else:
                print("yeterli altının yok!")
        else:
            continue

    elif cvp == 2:
        dsgn.market_screen()              #market sayfasına giriş

        print("""************************************************************************************************************
            """)
        print(f"HP: {chr.hero.hp}    AP: {chr.hero.ap}      GOLD: {chr.hero.gold}")

        cvp = int(input())
        if cvp == 1:
            if chr.hero.gold > 50 and market_1 == False:
                chr.hero.ap = chr.hero.ap + 15
                chr.hero.gold = chr.hero.gold-50
                market_1 =True
            else:
                print("yeterli altının yok!")
        elif cvp == 2:
            if chr.hero.gold > 150 and market_2 == False:
                chr.hero.ap = chr.hero.ap + 35
                chr.hero.gold = chr.hero.gold - 150
                market_2 = True
            else:
                print("yeterli altının yok!")
        elif cvp == 3:
            if chr.hero.gold > 300 and market_3 == False:
                chr.hero.hp = chr.hero.hp + 200
                chr.hero.gold = chr.hero.gold - 300
                market_3 = True
            else:
                print("yeterli altının yok!")
        else:
            pass
            continue

    elif cvp == 3:
        dsgn.magic_screen()               #büyücü sayfasına giriş
        dsgn.durum()

        cvp = int(input())
        if cvp == 1:
            if chr.hero.gold > 150:
                chr.hero.hp = chr.hero.hp + rdm.randint(50,100)
                chr.hero.gold = chr.hero.gold - 150
            else:
                print("yeterli altının yok!")
        else:
            pass
            continue

    elif cvp == 4:
        dsgn.durum()
        dsgn.attack_wait_screen()         #saldırı bekleme seçim ekranı

        while chr.monster.hp > 0 and chr.hero.hp > 0:
            cvp = int(input())
            monster_cvp = rdm.randint(1, 4)

            if cvp == 1:
                if monster_cvp == 1:
                    dsgn.durum()
                    dsgn.attack_hero_miss_screen()
                    print("ıskaladın")
                else:
                    chr.monster.hp = chr.monster.hp - rdm.randint(0, chr.hero.ap)
                    dsgn.durum()
                    dsgn.attack_hero_action_screen()
                    if chr.monster.hp < 0:
                        chr.hero.gold = chr.hero.gold + chr.monster.gold
            elif cvp == 2:
                if monster_cvp == 2:
                    dsgn.durum()
                    dsgn.attack_hero_miss_screen()
                    print("ıskaladın")
                else:
                    chr.monster.hp = chr.monster.hp - rdm.randint(0, chr.hero.ap)
                    dsgn.durum()
                    dsgn.attack_hero_action_screen()
                    if chr.monster.hp < 0:
                        chr.hero.gold = chr.hero.gold + chr.monster.gold
            elif cvp == 3:
                if monster_cvp == 3:
                    dsgn.durum()
                    dsgn.attack_hero_miss_screen()
                    print("ıskaladın")
                else:
                    chr.monster.hp = chr.monster.hp - rdm.randint(0, chr.hero.ap)
                    dsgn.durum()
                    dsgn.attack_hero_action_screen()
                    if chr.monster.hp < 0:
                        chr.hero.gold = chr.hero.gold + chr.monster.gold
            else:
                chr.hero.hp += 20

            monster_atack_chance = rdm.randint(1,4)

            if monster_atack_chance == 1:
                dsgn.durum()
                dsgn.attack_hero_miss_screen()
                print("Saldırıdan kurtuldun")

            else:
                dsgn.durum()
                dsgn.attack_hero_action_screen()
                chr.hero.hp -= rdm.randint(0,chr.monster.ap)
                print("Hasar aldın")

        if chr.hero.hp < 0:
            print("ÖLDÜN")
            break
        elif chr.monster.hp < 0:
            print("CANAVARI ÖLDÜRDÜN")
            lvl += 1
            chr.monster.hp += 100 * (lvl * 0.5)
            chr.monster.gold += 40 * (lvl)
            chr.monster.ap += 40 * (lvl * 0.1)
            continue
        else:
            pass
    else:
        print("lütfen geçerli bir değer giriniz")