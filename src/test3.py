#Program Luas
#{Input : x1,y1,x2,y2
# Output : Luas
# }

#Program Segiempat
#{Input : 
# Output : Luas dan dituliskan apa input benar atau tidak
# }
# Kamus
# TAwalX,TAwalY,TAkhirX,TAkhirY : Integer
# x1,y1,x2,y2 : integer
# segiempat1,segiempat2 : Integer

def luas(x1,y1,x2,y2):
    return abs(x1-x2) * abs(y1-y2)

def segiempat() :
    TAwalX = int(input("TAwalX = "))
    TAwalY = int(input("TAwalY = "))
    TAkhirX = int(input("TAakhirX = "))
    TAkhirY = int(input("TAakhirY = "))
    if TAwalX > 0 and TAwalY>0 :
        if TAkhirY<0 and TAkhirX<0 :
            return luas(TAwalX,TAwalY,TAkhirX,TAkhirY)
        else :
            return 0
    elif TAwalX < 0 and TAwalY>0 :
        if TAkhirY<0 and TAkhirX>0 :
            return luas(TAwalX,TAwalY,TAkhirX,TAkhirY)
        else :
            return 0
    else :
        return 0

print("Masukkan titik segi empat untuk dicari hasilnya")
print("Titik Segiempat pertama")
segiempat1 = segiempat()
print("Titik Segiempat kedua")
segiempat2 = segiempat()
if segiempat1 == 0 or segiempat2 == 0 :
    print("Input invalid")
elif segiempat1>segiempat2 :
    print("SegiEmpat pertama lebih luas daripada SegiEmpat kedua")
elif segiempat1<segiempat2 :
    print("SegiEmpat kedua lebih luas daripada SegiEmpat pertama")
else :
    print("Luas SegiEmpat sama")