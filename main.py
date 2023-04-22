from tkinter import messagebox
from tkinter import *
import random,os
import time
class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Biling Software")
        bg_color='#074463'
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg='white',font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #====variables
        #+++++++variables of prices
        self.lipstickp=100 
        self.highlightp=120
        self.bronzerp=150
        self.eyelinearp=220
        self.foundationp=180
        self.tonerp=170
        #+++++++++variable of prices for grocery
        self.aatap=100 
        self.maidap=120
        self.pastap=150 
        self.cheesep=220
        self.ricep=180 
        self.daalp=170
        #+++++++++++Variable of prices for beverages
        self.cokep=100 
        self.limcap=120 
        self.beerp=150 
        self.redbullp=220 
        self.fantap=180 
        self.spritep=170
        #=====variables fpr cosmetic
        self.lipstick=IntVar()
        self.eyelinear=IntVar()
        self.toner=IntVar()
        self.foundation=IntVar()
        self.bronzer=IntVar()
        self.highlight=IntVar()
        #variables for grocery
        self.daal=IntVar()
        self.rice=IntVar()
        self.aata=IntVar()
        self.cheese=IntVar()
        self.maida=IntVar()
        self.pasta=IntVar()
        #varibale for beverages
        self.coke=IntVar()
        self.limca=IntVar()
        self.fanta=IntVar()
        self.sprite=IntVar()
        self.beer=IntVar()
        self.redbull=IntVar()
        #==========Grand Total
        self.grandtotal=IntVar()
        
        #variables for customer
        self.cus_name=StringVar()
        self.cus_phone=StringVar()
        self.cus_bill=StringVar()
        self.bill_data=StringVar()
        self.randomm=random.randint(10000,99999)
        self.cus_bill.set(self.randomm)
        self.bill=StringVar()
        #variables for taxes
        self.costax=IntVar()
        self.grocerytax=IntVar()
        self.bevtax=IntVar()
        self.costotal=IntVar()
        self.grocerytotal=IntVar()
        self.search_bill=StringVar()
        self.bevtotal=IntVar()
         #====customer Detailings
        f1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f1.place(x=0,y=80,relwidth=1)
        cname_label=Label(f1,text="Customer name",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,padx=10,pady=5)
        cname_text=Entry(f1,width=17,font="arial 15",textvariable=self.cus_name,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=2)
        cphone_label=Label(f1,text="Phone Number",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=2,padx=10,pady=5)
        cphone_text=Entry(f1,width=17,font="arial 15",bd=7,textvariable=self.cus_phone,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=2)
        cbill_label=Label(f1,text="Bill Number",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=4,padx=10,pady=5)
        cbill_text=Entry(f1,width=17,font="arial 15",bd=7,textvariable=self.search_bill,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=2)
        butn=Button(f1,width=13,font="arial 15",bd=2,text="Search",command=self.bill_search).grid(row=0,column=6,padx=20,pady=10)
        #========Cosmetic Frame
        f2=LabelFrame(self.root,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=SUNKEN)
        f2.place(x=10,y=180,width=335,height=340)
        c1_label=Label(f2,text="Lipstick",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=5)
        c1_text=Entry(f2,width=12,font="arial 15",bd=7,textvariable=self.lipstick,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=2)
        c2_label=Label(f2,text="Eye Liner",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=5)
        c2_text=Entry(f2,width=12,font="arial 15",bd=7,textvariable=self.eyelinear,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=2)
        c3_label=Label(f2,text="Highlighter",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=5)
        c3_text=Entry(f2,width=12,font="arial 15",bd=7,textvariable=self.highlight,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=2)
        c4_label=Label(f2,text="bronzer",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=5)
        c4_text=Entry(f2,width=12,font="arial 15",bd=7,textvariable=self.bronzer,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=2)
        c6_label=Label(f2,text="Foundation",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=5)
        c5_text=Entry(f2,width=12,font="arial 15",bd=7,textvariable=self.foundation,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=2)
        c6_label=Label(f2,text="Toner",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=5)
        c6_text=Entry(f2,width=12,font="arial 15",bd=7,textvariable=self.toner,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=2)
        #==========grocery
        f3=LabelFrame(self.root,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=SUNKEN)
        f3.place(x=350,y=180,width=335,height=340)
        c7_label=Label(f3,text="Daal",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=5)
        c7_text=Entry(f3,width=12,font="arial 15",bd=7,textvariable=self.daal,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=2)
        c8_label=Label(f3,text="Rice",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=5)
        c8_text=Entry(f3,width=12,font="arial 15",bd=7,relief=SUNKEN,textvariable=self.rice).grid(row=1,column=1,pady=5,padx=2)
        c9_label=Label(f3,text="Pasta",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=5)
        c9_text=Entry(f3,width=12,font="arial 15",bd=7,textvariable=self.pasta,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=2)
        c10_label=Label(f3,text="Maida",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=5)
        c10_text=Entry(f3,width=12,font="arial 15",bd=7,textvariable=self.maida,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=2)
        c11_label=Label(f3,text="aata",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=5)
        c11_text=Entry(f3,width=12,font="arial 15",bd=7,textvariable=self.aata,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=2)
        c12_label=Label(f3,text="Cheese",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=5)
        c12_text=Entry(f3,width=12,font="arial 15",bd=7,textvariable=self.cheese,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=2)
        #===========Beverages
        f4=LabelFrame(self.root,text="Beverages",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,bd=10,relief=SUNKEN)
        f4.place(x=688,y=180,width=335,height=340)
        c13_label=Label(f4,text="Coke",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=5)
        c13_text=Entry(f4,width=12,font="arial 15",bd=7,textvariable=self.coke,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=2)
        c14_label=Label(f4,text="limca",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=5)
        c14_text=Entry(f4,width=12,font="arial 15",bd=7,textvariable=self.limca,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=2)
        c15_label=Label(f4,text="fanta",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=5)
        c15_text=Entry(f4,width=12,font="arial 15",bd=7,textvariable=self.fanta,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=2)
        c16_label=Label(f4,text="Red Bull",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=5)
        c16_text=Entry(f4,width=12,font="arial 15",bd=7,textvariable=self.redbull,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=2)
        c17_label=Label(f4,text="Beer",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=5)
        c17_text=Entry(f4,width=12,font="arial 15",bd=7,textvariable=self.beer,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=2)
        c18_label=Label(f4,text="Sprite",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=5)
        c18_text=Entry(f4,width=12,font="arial 15",bd=7,textvariable=self.sprite,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=2)
        f5=LabelFrame(self.root,bd=4,relief=SUNKEN)
        f5.place(x=1032,y=180,width=300,height=340)
        bill_text=Label(f5,text="Bill Area",font=("times new roman",18,"bold"),fg="black",relief=GROOVE,bd=3).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #==============button
        f6=LabelFrame(text="Billing System",font=("arial",15,"bold"),bd=4,relief=SUNKEN,bg=bg_color,fg="gold")
        f6.place(x=0,y=522,height=160,relwidth=1)
        c19_label=Label(f6,text="Cosmetics Total",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=5)
        c19_text=Entry(f6,width=20,font="arial 10",bd=7,textvariable=self.costotal,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=2)
        c20_label=Label(f6,text="Grocery Total",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=5)
        c20_text=Entry(f6,width=20,font="arial 10",bd=7,textvariable=self.grocerytotal,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=2)
        c21_label=Label(f6,text="Beverages Total",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=5)
        c21_text=Entry(f6,width=20,font="arial 10",bd=7,textvariable=self.bevtotal,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=2)
        c19_label=Label(f6,text="Cosmetic Tax",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=2,padx=10,pady=5)
        c19_text=Entry(f6,width=20,font="arial 10",bd=7,textvariable=self.costax,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=2)
        c20_label=Label(f6,text="Grocery Tax",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=2,padx=10,pady=5)
        c20_text=Entry(f6,width=20,font="arial 10",bd=7,textvariable=self.grocerytax,relief=SUNKEN).grid(row=1,column=3,pady=5,padx=2)
        c21_label=Label(f6,text="Beverages Tax",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=2,padx=10,pady=5)
        c21_text=Entry(f6,width=20,font="arial 10",bd=7,textvariable=self.bevtax,relief=SUNKEN).grid(row=2,column=3,pady=5,padx=2)
        #=====button frame
        f7=Frame(self.root,bd=4,relief=SUNKEN,bg="white")
        f7.place(x=680,y=550,height=115,width=650)
        total=Button(f7,relief=SUNKEN,bd=3,text="TOTAL",command=self.total,bg="cadetblue",pady=10,fg="white",font=("new times roman",20,"bold")).grid(row=0,column=0,padx=10,pady=17)
        generate_bill=Button(f7,relief=SUNKEN,bd=3,text="GENERATE BILL",command=self.bill_area,bg="cadetblue",pady=10,fg="white",font=("new times roman",20,"bold")).grid(row=0,column=1,padx=5,pady=17)
        clear=Button(f7,relief=SUNKEN,bd=3,text="CLEAR",bg="cadetblue",command=self.clear,fg="white",pady=10,font=("new times roman",20,"bold")).grid(row=0,column=2,padx=5,pady=17)
        exit_1=Button(f7,relief=SUNKEN,bd=3,text="EXIT",command=self.destroy,bg="cadetblue",fg="white",pady=10,font=("new times roman",20,"bold")).grid(row=0,column=3,padx=5,pady=17)
        # self.welcome()
    def total(self):
        #========cosmetics total
        self.total1=float(
            (self.lipstick.get()*100)+
            (self.highlight.get()*120)+
            (self.bronzer.get()*150)+
            (self.eyelinear.get()*220)+
            (self.foundation.get()*180)+
            (self.toner.get()*170)
         )
        self.costotal.set("Rs.."+str(self.total1))
        self.costax.set("Rs.."+str(self.total1*0.02))
        #++++++++++grocery total
        self.total2=float(
            (self.aata.get()*100)+
            (self.maida.get()*120)+
            (self.pasta.get()*150)+
            (self.cheese.get()*220)+
            (self.rice.get()*180)+
            (self.daal.get()*170)
         )
        self.grocerytotal.set("Rs.."+str(self.total2))
        self.grocerytax.set("Rs.."+str(self.total2*0.05))
        #==========beverages total
        self.total3=float(
            (self.coke.get()*100)+ 
            (self.limca.get()*120)+
            (self.beer.get()*150)+
            (self.redbull.get()*220)+
            (self.fanta.get()*180)+
            (self.sprite.get()*170)
         )
        self.bevtotal.set("Rs.."+(str(self.total3)))
        self.bevtax.set("Rs.."+str(self.total3*0.10))

        self.grandtotal=((self.total1*0.02)+(self.total2*0.05)+(self.total3*0.10)+(self.total1)+(self.total2)+(self.total3))
    def bill_area(self):
        if self.cus_name.get()=="" or self.cus_phone.get()=="":
            messagebox.showerror("Error","Customer Details are Must")
        elif self.grandtotal==0:
            messagebox.showerror("Error","No Item Purchased")
        else:
            self.txtarea.delete(1.0,END)
            self.txtarea.insert(END,"\tWelcome To Yatin's Store\n")
            self.txtarea.insert(END,"=================================\n")
            self.txtarea.insert(END,f"Bill No. {self.cus_bill.get()}\n")
            self.txtarea.insert(END,f"Customer Name- {self.cus_name.get()}\n")
            self.txtarea.insert(END,f"Phone No.- {self.cus_phone.get()}\n")
            self.txtarea.insert(END,"=================================\n")
            self.txtarea.insert(END,"Product\t    Quantity\t    Price\n")
            self.cosmetic1()
            self.grocery1()
            self.beverages1()
            self.txtarea.insert(END,"---------------------------------\n")
            self.txtarea.insert(END,f"Cosmetic Tax   = Rs.{str(self.total1*0.02)}\n")
            self.txtarea.insert(END,f"Grocery Tax    = Rs.{str(self.total2*0.05)}\n")
            self.txtarea.insert(END,f"Beverages Tex  = Rs.{str(self.total3*0.10)}\n")
            self.txtarea.insert(END,"---------------------------------\n")
            self.txtarea.insert(END,f"Grand Total    = Rs.{str(self.grandtotal)}\n")
            # time.sleep(1)
            self.bill_save()
    def bill_save(self):
        op=messagebox.askyesno("Save Bill","Do You want to Save the Bill")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("Bills/"+str(self.cus_bill.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved","Your Bill is Saved")
        else:
            return
    def bill_search(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill Number")
    #========if Conditions
    def cosmetic1(self):
        if self.lipstick.get()>0:
            self.txtarea.insert(END,"lipstick")
            self.txtarea.insert(END,f"\t     {self.lipstick.get()}")
            self.txtarea.insert(END,f"\t\t {self.lipstickp*self.lipstick.get()}\n")
        if self.eyelinear.get()>0:
            self.txtarea.insert(END,"Eyeliner")
            self.txtarea.insert(END,f"\t     {self.eyelinear.get()}")
            self.txtarea.insert(END,f"\t\t {self.eyelinearp*self.eyelinear.get()}\n")
        if self.highlight.get()>0:
            self.txtarea.insert(END,"Highligt.")
            self.txtarea.insert(END,f"\t    {self.highlight.get()}")
            self.txtarea.insert(END,f"\t\t {self.highlightp*self.highlight.get()}\n")
        if self.foundation.get()>0:
            self.txtarea.insert(END,"Foundation")
            self.txtarea.insert(END,f"\t   {self.foundation.get()}")
            self.txtarea.insert(END,f"\t\t {self.foundationp*self.foundation.get()}\n")
        if self.toner.get()>0:
            self.txtarea.insert(END,"Toner")                              
            self.txtarea.insert(END,f"\t      {self.toner.get()}")
            self.txtarea.insert(END,f"\t\t {self.tonerp*self.toner.get()}\n")
        if self.bronzer.get()>0:
            self.txtarea.insert(END,"Bronzer")
            self.txtarea.insert(END,f"\t      {self.bronzer.get()}")
            self.txtarea.insert(END,f"\t\t {self.bronzerp*self.bronzer.get()}\n")
    def grocery1(self):
        if self.aata.get()>0:
            self.txtarea.insert(END,"Atta")
            self.txtarea.insert(END,f"\t      {self.aata.get()}")
            self.txtarea.insert(END,f"\t\t {self.aatap*self.aata.get()}\n")
        if self.maida.get()>0:
            self.txtarea.insert(END,"Maida")
            self.txtarea.insert(END,f"\t      {self.maida.get()}")
            self.txtarea.insert(END,f"\t\t {self.maidap*self.maida.get()}\n")
        if self.cheese.get()>0:
            self.txtarea.insert(END,"Cheese")
            self.txtarea.insert(END,f"\t      {self.cheese.get()}")
            self.txtarea.insert(END,f"\t\t {self.cheesep*self.cheese.get()}\n")
        if self.daal.get()>0:
            self.txtarea.insert(END,"Daal")
            self.txtarea.insert(END,f"\t      {self.daal.get()}")
            self.txtarea.insert(END,f"\t\t {self.daalp*self.daal.get()}\n")
        if self.pasta.get()>0:
            self.txtarea.insert(END,"Pasta")
            self.txtarea.insert(END,f"\t      {self.pasta.get()}")
            self.txtarea.insert(END,f"\t\t {self.pastap*self.pasta.get()}\n")
        if self.rice.get()>0:
            self.txtarea.insert(END,"Rice")
            self.txtarea.insert(END,f"\t      {self.rice.get()}")
            self.txtarea.insert(END,f"\t\t {self.ricep*self.rice.get()}\n")
    def beverages1(self):
        if self.coke.get()>0:
            self.txtarea.insert(END,"Coke")
            self.txtarea.insert(END,f"\t      {self.coke.get()}")
            self.txtarea.insert(END,f"\t\t {self.cokep*self.coke.get()}\n")
        else:
            pass

        if self.limca.get()>0:
            self.txtarea.insert(END,"Limca")
            self.txtarea.insert(END,f"\t      {self.limca.get()}")
            self.txtarea.insert(END,f"\t\t {self.limcap*self.limca.get()}\n")
        else:
            pass

        if self.fanta.get()>0:
            self.txtarea.insert(END,"Fanta")
            self.txtarea.insert(END,f"\t      {self.fanta.get()}")
            self.txtarea.insert(END,f"\t\t {self.fantap*self.fanta.get()}\n")
        else:
            pass

        if self.beer.get()>0:
            self.txtarea.insert(END,"Beer")
            self.txtarea.insert(END,f"\t      {self.beer.get()}")
            self.txtarea.insert(END,f"\t\t {self.beerp*self.beer.get()}\n")
        else:
            pass
        
        if self.redbull.get()>0:
            self.txtarea.insert(END,"Red Bull")
            self.txtarea.insert(END,f"\t     {self.redbull.get()}")
            self.txtarea.insert(END,f"\t\t {self.redbullp*self.redbull.get()}\n")
        else:
            pass
        
        if self.sprite.get()>0:
            self.txtarea.insert(END,"Sprite")
            self.txtarea.insert(END,f"\t      {self.sprite.get()}")
            self.txtarea.insert(END,f"\t\t {self.spritep*self.sprite.get()}\n")
        else:
            pass
    def clear(self):
        #=====variables fpr cosmetic
        np=messagebox.askyesno("Clear","Do You Want to clear?")
        if np>0:
            self.txtarea.delete("1.0",END)
            self.lipstick.set(0)
            self.eyelinear.set(0)
            self.toner.set(0)
            self.foundation.set(0)
            self.bronzer.set(0)
            self.highlight.set(0)
            #variables for grocery
            self.rice.set(0)
            self.daal.set(0)
            self.aata.set(0)
            self.cheese.set(0)
            self.maida.set(0)
            self.pasta.set(0)
            #varibale for beverages
            self.coke.set(0)
            self.limca.set(0)
            self.fanta.set(0)
            self.sprite.set(0)
            self.beer.set(0)
            self.redbull.set(0)
            #==========Grand Total
            # self.grandtotal.set(0)
            
            #variables for customer
            self.cus_name.set("")
            self.cus_phone.set("")
            self.cus_bill.set("")
            self.bill_data=StringVar()
            self.randomm=random.randint(10000,99999)
            self.cus_bill.set(self.randomm)
            self.bill=StringVar()
            #variables for taxes
            self.costax.set(0)
            self.grocerytax.set(0)
            self.bevtax.set(0)
            self.costotal.set(0)
            self.grocerytotal.set(0)
            self.search_bill.set('')
            self.bevtotal.set(0)
    def destroy(self):
        lp=messagebox.askyesno("Exit","Do You Want to exit?")
        if lp>0:
            self.root.destroy()
root=Tk()
obj=bill_app(root)
root.mainloop()
