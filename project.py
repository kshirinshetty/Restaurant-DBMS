''' Restaurant Management : Menu '''

from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector as sql

root=Tk()
root.geometry("1550x850+0+0")
root.title("Restaurant Del Luna")
root.configure(background='MediumPurple3')

'''#SQL connection
con = sql.connect(host = "localhost", user="root",passwd = "HPSdb2018", database="restaurant")
cur = con.cursor()'''

#Frames
Tops = Frame(root, width=1550, height=80, bd=12, relief="raise", background='Indian Red')
Tops.place(x=50, y=10)
lblTitle = Label(Tops, font=("COOPER BLACK", 50, 'bold'), text="        RESTAURANT DEL LUNA          ",fg='red')
lblTitle.grid(row=0, column=0)

f1 = Frame(root, width=500, height=570, bd=12, relief="raise")
f1.place(x=50, y=150)

f2Top = Frame(root, width=400, height=350, bd=12, relief="raise")
f2Top.place(x=420, y=150)

f2Bottom = Frame(root, width=400, height=450,bd=4, relief="raise")
f2Bottom.place(x=424, y=463)

f3 = Frame(root, width=400, height=770, bd=12, relief="raise")
f3.place(x=1000, y=150)


# FRAME 1 VARIABLES
vp = StringVar()
vt = StringVar()
vw = StringVar()
vc = StringVar()
vb = StringVar()
vcs = StringVar()
vs = StringVar()
vco = StringVar()

vp.set(0)
vt.set(0)
vw.set(0)
vc.set(0)
vb.set(0)
vcs.set(0)
vs.set(0)
vco.set(0)

#FRAME 2 TOP VARIABLES
vcb = StringVar()
vg = StringVar()
vf = StringVar()
vr = StringVar()
vj = StringVar()

vcb.set(0)
vg.set(0)
vf.set(0)
vr.set(0)
vj.set(0)

#FRAME 2 BOTTOM FRAME VARIABLES
varTotal = StringVar()
varTotal.set(0)

#FRAME 3 VARIABLES
vt = StringVar()
vcol = StringVar()
vcof = StringVar()
vor = StringVar()
vmw= StringVar()
vcp = StringVar()
vmp = StringVar()
vat = StringVar()

vt.set(0)
vcol.set(0)
vcof.set(0)
vor.set(0)
vmw.set(0)
vcp.set(0)
vmp.set(0)
vat.set(0)

#EXIT FUNCTION
def iExit():
    qExit = messagebox.askyesno("Restraunt Menu App","Do you want to quit ?")
    if qExit > 0:
        root.destroy()
        return 
    
#RESET FUNCTION
def Reset():
    vp.set(0)
    vt.set(0)
    vw.set(0)
    vc.set(0)
    vb.set(0)
    vcs.set(0)
    vs.set(0)
    vco.set(0)
    vcb.set(0)
    vg.set(0)
    vf.set(0)
    vr.set(0)
    vj.set(0)
    varTotal.set(0)
    vt.set(0)
    vcof.set(0)
    vcol.set(0)
    vor.set(0)
    vmw.set(0)
    vcp.set(0)
    vmp.set(0)
    vat.set(0)

#PRICE LIST WINDOW
def price_list():
    roo = Tk()
    roo.geometry("600x700+0+0")
    roo.title("Price List")
    l = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    l.grid(row=0, column=0)
    l = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white")
    l.grid(row=0, column=2)
    l = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black")
    l.grid(row=0, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Pancakes", fg="gold")
    l.grid(row=1, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="150", fg="gold")
    l.grid(row=1, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Toast", fg="gold")
    l.grid(row=2, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="100", fg="gold")
    l.grid(row=2, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Waffles", fg="gold")
    l.grid(row=3, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="150", fg="gold")
    l.grid(row=3, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Cinnamon Rolls", fg="gold")
    l.grid(row=4, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="100", fg="gold")
    l.grid(row=4, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Baked potatoes", fg="gold")
    l.grid(row=5, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="150", fg="gold")
    
    l.grid(row=5, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Cheese Sandwich", fg="palevioletred")
    l.grid(row=6, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="100", fg="palevioletred")
    l.grid(row=6, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Sandwhich", fg="palevioletred")
    l.grid(row=7, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="100", fg="palevioletred")
    l.grid(row=7, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Corn Sandwhich", fg="palevioletred")
    l.grid(row=8, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="100", fg="palevioletred")
    
    l.grid(row=8, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Brownie", fg="lawn green")
    l.grid(row=9, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="140", fg="lawn green")
    l.grid(row=9, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Gulab Jamun", fg="lawn green")
    l.grid(row=10, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="100", fg="lawn green")
    l.grid(row=10, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Fruit Salad", fg="lawn green")
    l.grid(row=11, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="100", fg="lawn green")
    l.grid(row=11, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Rasmalai", fg="lawn green")
    l.grid(row=12, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="100", fg="lawn green")
    l.grid(row=12, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Jalebi", fg="lawn green")
    l.grid(row=13, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="85", fg="lawn green")
    l.grid(row=13, column=3)

    l = Label(roo, font=('aria', 15, 'bold'), text="Tea", fg="ORANGE")
    l.grid(row=14, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="60", fg="ORANGE")
    l.grid(row=14, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Coffee", fg="ORANGE")
    l.grid(row=15, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="90", fg="ORANGE")
    l.grid(row=15, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Cola", fg="ORANGE")
    l.grid(row=16, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="50", fg="ORANGE")
    l.grid(row=16, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Orange Juice", fg="ORANGE")
    l.grid(row=17, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="50", fg="ORANGE")
    l.grid(row=17, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Mineral Water", fg="ORANGE")
    l.grid(row=18, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="25", fg="ORANGE")
    l.grid(row=18, column=3)

    
    l = Label(roo, font=('aria', 15, 'bold'), text="Cheese Pasta", fg="DeepSkyBlue")
    l.grid(row=19, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="180", fg="DeepSkyBlue")
    l.grid(row=19, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Mexican Pizza", fg="DeepSkyBlue")
    l.grid(row=20, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="105", fg="DeepSkyBlue")
    l.grid(row=20, column=3)
    l = Label(roo, font=('aria', 15, 'bold'), text="Aloo Tikki Burger", fg="DeepSkyBlue")
    l.grid(row=21, column=0)
    l = Label(roo, font=('aria', 15, 'bold'), text="95", fg="DeepSkyBlue")
    l.grid(row=21, column=3)
    roo.mainloop()

#TOTAL FUNCTION
def TotalCost():
    m1 = int(vp.get())
    m2 = int(vt.get())
    m3 = int(vw.get())
    m4 = int(vc.get())
    m5 = int(vb.get())
    m6 = int(vcs.get())
    m7 = int(vs.get())
    m8 = int(vco.get())
    m9 = int(vcb.get())
    m10 = int(vg.get())
    m11 = int(vf.get())
    m12 = int(vr.get())
    m13 = int(vj.get())
    m14 = int(vt.get())
    m15 = int(vcol.get())
    m16 = int(vcof.get())
    m17 = int(vor.get())
    m18 = int(vmw.get())
    m19 = int(vcp.get())
    m20 = int(vmp.get())
    m21 = int(vat.get())

    iTotal = (m1*150 + m2*100 + m3*150 + m4*100 + m5*150 + m6*100 + m7*100 + m8*100 + m9*140 + m10*100 + m11*100 + m12*100 + m13*85 + m14*60 + m15*90 + m16*50 +
                 m17*50 + m18*25 + m19*180 + m20*105 + m21*95)

    striTotal = 'Rs',str(iTotal)
    varTotal.set(striTotal)

    #SQL Popularity
'''
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 1".format(m1))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 2".format(m2))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 3".format(m3))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 4".format(m4))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 5".format(m5))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 6".format(m6))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 7".format(m7))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 8".format(m8))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 9".format(m9))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 10".format(m10))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 11".format(m11))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 12".format(m12))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 13".format(m13))

    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 14".format(m14))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 15".format(m15))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 16".format(m16))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 17".format(m17))

    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 18".format(m18))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 19".format(m19))

    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 20".format(m20))
    cur.execute(" UPDATE MENU SET Popularity = Popularity + {} WHERE code = 21".format(m21))
    
    con.commit()
'''
#FRAME 1
    
meal = Label(f1,font=("arial",25,'bold'), text="Fast Meal", fg='goldenrod')
meal.grid(row=0, column=0)

Pan = Label(f1, text="Pancakes",  font=("arial", 18, 'bold'),fg='gold')
Pan.grid(row=1, column=0, sticky = W)
txtPan = Entry(f1, font=("arial", 18, 'bold'), bd=8, textvariable = vp, width=4, justify="right")
txtPan.grid(row=1, column=1)

To = Label(f1, text="Toast",font=("arial", 18, 'bold'),fg='gold')
To.grid(row=2, column=0, sticky = W)
txtTo = Entry(f1, font=("arial", 18, 'bold'), bd=8, textvariable = vt, width=4, justify="right")
txtTo.grid(row=2, column=1)

Waf = Label(f1, text="Waffles",  font=("arial", 18, 'bold'),fg='gold')
Waf.grid(row=3, column=0, sticky = W)
txtWaf = Entry(f1, font=("arial", 18, 'bold'), bd=8, textvariable = vw, width=4, justify="right")
txtWaf.grid(row=3, column=1)

Cin = Label(f1, text="Cinnamon Rolls", font=("arial", 18, 'bold'),fg='gold')
Cin.grid(row=4, column=0, sticky = W)
txtCin = Entry(f1, font=("arial", 18, 'bold'), bd=8, textvariable = vc, width=4, justify="right")
txtCin.grid(row=4, column=1)

Bp= Label(f1, text="Baked Potatoes", font=("arial", 18, 'bold'),fg='gold')
Bp.grid(row=5, column=0, sticky = W)
txtBp = Entry(f1, font=("arial", 18, 'bold'), bd=8, textvariable = vb, width=4, justify="right")
txtBp.grid(row=5, column=1)

Space = Label(f1,text="\n")
Space.grid(row=6, column=0)
S = Label(f1,font=("arial",25,'bold'), text="Sandwiches",fg='violetred3')
S.grid(row=7, column=0)

Che = Label(f1, text="Cheese Sandwich",  font=("arial", 18, 'bold'),fg='palevioletred')
Che.grid(row=8, column=0, sticky = W)
txtChe = Entry(f1, font=("arial", 18, 'bold'), bd=8, textvariable = vcs, width=4, justify="right")
txtChe.grid(row=8, column=1)

Cho = Label(f1, text="Chocolate Sandwich",  font=("arial", 18, 'bold'),fg='palevioletred')
Cho.grid(row=9, column=0, sticky = W)
txtCho = Entry(f1, font=("arial", 18, 'bold'), bd=8, textvariable = vs, width=4, justify="right")
txtCho.grid(row=9, column=1)

Cs = Label(f1, text="Corn Sandwhich", font=("arial", 18, 'bold'),fg='palevioletred')
Cs.grid(row=10, column=0, sticky = W)
txtCs = Entry(f1, font=("arial", 18, 'bold'), bd=8, textvariable = vco, width=4, justify="right")
txtCs.grid(row=10, column=1)


#FRAME 2 Top

meal = Label(f2Top,font=("arial",25,'bold'), text="Desserts",fg='forest green')
meal.grid(row=0, column=0)

Cb = Label(f2Top, text="Chocolate Brownie                                  ",  font=("arial", 18, 'bold'),fg='lawn green')
Cb.grid(row=1, column=0, sticky = W)
txtCb = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = vcb, width=4, justify="right")
txtCb.grid(row=1, column=1)

Gj = Label(f2Top, text="Gulab Jamun", font=("arial", 18, 'bold'),fg='lawn green')
Gj.grid(row=2, column=0, sticky = W)
txtGj = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = vg, width=4, justify="right")
txtGj.grid(row=2, column=1)

Fs = Label(f2Top, text="FruitSalad", font=("arial", 18, 'bold'),fg='lawn green')
Fs.grid(row=3, column=0, sticky = W)
txtFs= Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = vf, width=4, justify="right")
txtFs.grid(row=3, column=1)

R= Label(f2Top, text="Rasmalai",font=("arial", 18, 'bold'),fg='lawn green')
R.grid(row=4, column=0, sticky = W)
txtR = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = vr, width=4, justify="right")
txtR.grid(row=4, column=1)

J = Label(f2Top, text="Jalebi", font=("arial", 18, 'bold'),fg='lawn green')
J.grid(row=5, column=0, sticky = W)
txtJ = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = vj, width=4, justify="right")
txtJ.grid(row=5, column=1)


#FRAME 2 BOTTOM

lblT = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Total", bd=10, width=16, anchor='e')
lblT.grid(row=2,column=1)
txtT = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varTotal, width=9, justify="right")
txtT.grid(row=2, column=2)

Space = Label(f2Bottom,text="\n")
Space.grid(row=3, column=0)

#BUTTONS

btnprice=Button(f2Bottom, bd=10 ,font=('arial' ,16,'bold'),width=9, text="PRICE LIST", command = price_list)
btnprice.grid(row=4, column=0)

btnTotal = Button(f2Bottom,  bd=10,  font=("arial", 16, 'bold'), width=7,
                  text="TOTAL", command = TotalCost).grid(row=4, column=2)

btnReset=Button(f2Bottom,bd=10,font=('arial',16,'bold'),width=9,text="RESET", command=Reset)
btnReset.grid(row=5,column=0)

btnExit=Button(f2Bottom,bd=10,font=('arial',16,'bold'),width=7,text="EXIT", command = iExit)
btnExit.grid(row=5,column=2)


#FRAME 3

Drinks = Label(f3,font=("arial",25,'bold'), text="Drinks",fg='orangered1')
Drinks.grid(row=0, column=0)

T = Label(f3, text="Tea", font=("arial", 18, 'bold'),fg='orange')
T.grid(row=1, column=0, sticky = W)
txtT = Entry(f3, font=("arial", 18, 'bold'), bd=8, textvariable = vt, width=4, justify="right")
txtT.grid(row=1, column=1)

C = Label(f3, text="Cola",font=("arial", 18, 'bold'),fg='orange')
C.grid(row=2, column=0, sticky = W)
txtC = Entry(f3, font=("arial", 18, 'bold'), bd=8, textvariable = vcol, width=4, justify="right")
txtC.grid(row=2, column=1)

Cof = Label(f3, text="Coffee",  font=("arial", 18, 'bold'),fg='orange')
Cof.grid(row=3, column=0, sticky = W)
txtCof = Entry(f3, font=("arial", 18, 'bold'), bd=8, textvariable = vcof, width=4, justify="right")
txtCof.grid(row=3, column=1)

O = Label(f3, text="Orange Juice", font=("arial", 18, 'bold'),fg='orange')
O.grid(row=4, column=0, sticky = W)
txtO = Entry(f3, font=("arial", 18, 'bold'), bd=8, textvariable = vor, width=4, justify="right")
txtO.grid(row=4, column=1)

w = Label(f3, text="Mineral Water        ", font=("arial", 18, 'bold'),fg='orange')
w.grid(row=5, column=0, sticky = W)
txtw = Entry(f3, font=("arial", 18, 'bold'), bd=8, textvariable = vmw, width=4, justify="right")
txtw.grid(row=5, column=1)

Space = Label(f3,text="\n")
Space.grid(row=6, column=0)

Shakes = Label(f3,font=("arial",25,'bold'), text="Meals",fg='DodgerBlue')
Shakes.grid(row=7, column=0)

cp = Label(f3, text="Cheese Pasta", font=("arial", 18, 'bold'),fg='DeepSkyBlue')
cp.grid(row=8, column=0, sticky = W)
txtcp = Entry(f3, font=("arial", 18, 'bold'), bd=8, textvariable = vcp, width=4, justify="right",)
txtcp.grid(row=8, column=1)

mp = Label(f3, text="Mexican Pizza", font=("arial", 18, 'bold'),fg='DeepSkyBlue')
mp.grid(row=9, column=0, sticky = W)
txtmp = Entry(f3, font=("arial", 18, 'bold'), bd=8, textvariable = vmp, width=4, justify="right",)
txtmp.grid(row=9, column=1)

atb = Label(f3, text="Aloo Tikki Burger",font=("arial", 18, 'bold'),fg='DeepSkyBlue')
atb.grid(row=10, column=0, sticky = W)
txtatb = Entry(f3, font=("arial", 18, 'bold'), bd=8, textvariable = vat, width=4, justify="right")
txtatb.grid(row=10, column=1)



root.mainloop()
