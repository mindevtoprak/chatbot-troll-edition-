durum=True
while durum:
    try:
        userinput=input("Write something ").lower()
        if userinput=="kod yaz" or userinput=="write code":
            print("KALK KENDİN YAZ KODU")
            print("GET UP WRITE THE CODE")
        elif userinput=="exit" or userinput=="çıkış":
            print("ÇIKIYORUM TM")
            print("EXITING OK BRO")
            durum=False
        elif userinput=="selam" or userinput=="hello":
            print("SALQAM")
            print("HWLLO BRO")
        elif userinput=="nasılsın" or userinput=="how are you":
            print("İYİYİMİM")
            print("I'M FINENENENENENNENENEN")
        elif userinput=="görüşürüz" or userinput=="see you":
            print("GÖRÜŞÜRÜZ.")
            print("SEE YOU.")
        elif userinput=="teşekkürler" or userinput=="thank you":
            print("RICA EDERİMIJERGBIERGBIEG")
            print("YOU'RE WELCOMEEIORNIERGHERGUO")
        else:            
            print("BUNU ANLAMADIM")
            print("I DON'T UNDERSTAND THIS")
    except (KeyboardInterrupt, EOFError):
        print()
        print("ÇIKIYORUM TM")
        print("EXITING OK BRO")
        input("Press Enter to exit...")
        durum=False
