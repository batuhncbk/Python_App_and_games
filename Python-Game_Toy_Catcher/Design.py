import time
import random as rdm
bosluk = " "

def catched():
    print(f"""
     0         10         20         30         40         50
    ___________________________________________________________
      |||
      |||
      |||
      |||
      |||
      / \  
      \ /
      
    -----------------------------------------------------------
    
    """)

def catching():
    catched()
    katsayi = int(input("İndirmek istediğiniz kolon numarasını giriniz = "))
    print(f"""
         0         10         20         30         40         50
        ___________________________________________________________
        {" " * katsayi}  |||
        {" " * katsayi}  / \  
        {" " * katsayi}  \ /
      
      
      
      
      
        -----------------------------------------------------------

    """)
    time.sleep(0.5)
    print(f"""
         0         10         20         30         40         50
        ___________________________________________________________
        {" " * katsayi}  |||
        {" " * katsayi}  |||
        {" " * katsayi}  / \  
        {" " * katsayi}  \ /




        -----------------------------------------------------------

        """)
    time.sleep(0.5)
    print(f"""
         0         10         20         30         40         50
        ___________________________________________________________
        {" " * katsayi}  |||
        {" " * katsayi}  |||
        {" " * katsayi}  |||
        {" " * katsayi}  / \  
        {" " * katsayi}  \ /



        -----------------------------------------------------------

        """)
    time.sleep(0.5)
    print(f"""
         0         10         20         30         40         50
        ___________________________________________________________
        {" " * katsayi}  |||
        {" " * katsayi}  |||
        {" " * katsayi}  |||
        {" " * katsayi}  |||
        {" " * katsayi}  / \  
        {" " * katsayi}  \ /


        -----------------------------------------------------------

        """)
    time.sleep(0.5)
    print(f"""
         0         10         20         30         40         50
        ___________________________________________________________
        {" " * katsayi}  |||
        {" " * katsayi}  |||
        {" " * katsayi}  |||
        {" " * katsayi}  |||
        {" " * katsayi}  |||
        {" " * katsayi}  / \  
        {" " * katsayi}  \ /

        -----------------------------------------------------------

        """)
    time.sleep(0.5)
    print(f"""
         0         10         20         30         40         50
        ___________________________________________________________
        {" " * katsayi}  |||
        {" " * katsayi}  / \  
        {" " * katsayi}  \ /





        -----------------------------------------------------------

        """)
    chanse = rdm.randint(1,3)
    if chanse == 1:
        print("""
        
                                   _________
                              ____/______ \ \ 
                             /         \ \ \ \_____
                            /   ======  \ \ \ \  \ \ 
                           /   /         \ \/ /   \ \   
                           \   \======    // /===  \ \  
                            \        /   //_/   /  / /
                             \  ====/   //  ===/  / /
                              \________// \______/_/
            
            
            * * * * * * * * * * * * YAKALADIN! * * * * * * * * * * * *
            -----------------------------------------------------------
        """)
    else:
        print("""
                                          ___
                                         /   \ 
                                         |   |
                                         |   |                          
                                ___  ___ |   | ___
                               /   \/   \|   |/   \ 
                               |                  |_
                               |                  | \ 
                                \                    |
                                 \                  /
                                  |                /
                                  |               |
            * * * * * * * * * * * YAKALAYAMADIN! * * * * * * * * * * *
            -----------------------------------------------------------
        """)

    cvp = input("Tekrar denemek ister misiniz e/h")
    if cvp == "e":
        pass
    else:
        while 1:
            break
