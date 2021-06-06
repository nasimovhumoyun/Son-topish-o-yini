import random
def son_top(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim top qani")

    taxminlar = 0
    while True:
        taxminlar+=1
        taxmin = int(input(">>>> "))
        if tasodifiy_son> taxmin:
            print(f"Men o'ylagan son {taxmin} dan katta. Yana harakat qil")
        elif tasodifiy_son<taxmin:
            print(f"Men o'ylagan son {taxmin} dan kichik. Yana harakat qil")
        else:
            print("Yutdingiz")
            break
    print(f"BRAVO.{taxminlar} ta qadamda  topding")
    return taxminlar
def sontop_pc(x=10):
    taxminlar = 0
    input(f"1 dan {x} gacha son o'yla men topaman. Boshlash uchun ENTER ni bos ")
    quyi = 1
    yuqori = x
    while True:
        taxminlar+=1
        if quyi!= yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin=quyi
        javob = (input(
            f"Siz o'ylagan son {taxmin}. Siz o'ylagan son {taxmin} bo'lsa (t),"
            f" kichik bo'lsa (-), Katta bo'lsa (+) ni kirit ".lower()))
        if javob=="+":
            quyi = taxmin+1
        elif javob=="-":
            yuqori= taxmin-1
        else:
            break
    print(f"Men {taxminlar} ta qadamda topdim")
    return taxminlar
def play(x=10):
    yana = True
    while yana:
        taxmin_user = son_top(x)
        taxmin_pc = sontop_pc(x)
        if taxmin_user>taxmin_pc:
            print("Men yutdim")
        elif taxmin_user<taxmin_pc:
            print("Qoyiil sen yutding")
        else:
            print("Durrang")
        yana=int(input("Yana o'ynaymizmi. Ha(1) Yoq(0):"))

play()