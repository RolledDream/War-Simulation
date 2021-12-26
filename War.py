from tkinter import *
import random


class Unit:
    def __init__(self,hp=1000):
        self.hp=hp

    def under_attack(self,num):
        self.hp-=num


class Attacker(Unit):
    def __init__(self,attack_point=90,hp=1000):
        self.hp=hp
        self.attack_point=attack_point

    def attack(self):
        return self.attack_point


class Healer(Unit):
    def __init__(self,healing_point=30,hp=1000):
        self.hp=hp
        self.healing_point=healing_point

    def healing(self,unit):
        unit.hp += int(self.AP.get())


def D_Attack(Attacker,Receiver):
    Receiver.hp=int(Receiver.HP.get())
    Receiver.under_attack(int(Attacker.AP.get()))
    Receiver.HP.delete(0,END)
    Receiver.HP.insert(END,Receiver.hp)

def D_Heal(aHealer,Receiver):
    Receiver.hp=int(Receiver.HP.get())
    aHealer.healing(Receiver)
    Receiver.HP.delete(0,END)
    Receiver.HP.insert(END,Receiver.hp)
    

monster = Attacker(10)
warrior = Attacker(10)
healer = Healer(10)


War=Tk()
War['bg']='white'
War.title("War ='^'=")
War.geometry("600x500")

Name=Label(War,text='Name',width=20)
Name.grid(row=0,column=0)
HP=Label(War,text='HP',width=20)
HP.grid(row=0,column=1)
AP=Label(War,text='Attack/Healing',width=20)
AP.grid(row=0,column=2)
Deal=Label(War,text='Deal',width=20)
Deal.grid(row=0,column=3)

def DD_monster():
    D_Attack(monster,warrior)
def DD_warrior():
    D_Attack(warrior,monster)
def DD_healer():
    D_Heal(healer,warrior)

c_c=0 ##chosen class

def warrioract():
    global c_c
    c_c='warrior'
    print(c_c)
def healeract():
    global c_c
    c_c='healer'
    print(c_c)
monster.N=Label(War,width=20,text='monster')
monster.N.grid(row=1,column=0)
monster.HP=Entry(War,width=20,bg='white')
monster.HP.grid(row=1,column=1)
monster.AP=Entry(War,width=20)
monster.AP.grid(row=1,column=2)
monster.D=Label(War,width=20,text="상대")
monster.D.grid(row=1,column=3)

warrior.N=Label(War,width=20,text='warrior')
warrior.N.grid(row=2,column=0)
warrior.HP=Entry(War,width=20,bg='white')
warrior.HP.grid(row=2,column=1)
warrior.AP=Entry(War,width=20)
warrior.AP.grid(row=2,column=2)
warrior.D=Button(War,width=18,text="Attack",command=warrioract)
warrior.D.grid(row=2,column=3)

healer.N=Label(War,width=20,text='healer')
healer.N.grid(row=3,column=0)
healer.HP=Entry(War,width=20,bg='white')
healer.HP.grid(row=3,column=1)
healer.AP=Entry(War,width=20)
healer.AP.grid(row=3,column=2)
healer.D=Button(War,width=18,text="Heal",command=healeract)
healer.D.grid(row=3,column=3)

monster.HP.insert(END,monster.hp)
warrior.HP.insert(END,warrior.hp)
healer.HP.insert(END,healer.hp)
monster.AP.insert(END,monster.attack_point)
warrior.AP.insert(END,warrior.attack_point)
healer.AP.insert(END,healer.healing_point)


def starting():
    global start, wta, SC, c_c
    wta=random.randint(0,1) ##Whom to attack
    
    if wta == 0:
        anouncement['text']='monster attacked warrior!'
        DD_monster()

    if wta == 1:
        anouncement['text']='monster attacked healer!'
        D_Attack(monster,healer)

def scene1():
    global c_c
    anouncement['text']='Select your Action'

        
def scene2():
    global c_c, SC
    
    print(SC, c_c)
    if c_c == 'warrior':
        anouncement['text']='warrior\'s attack'
        DD_warrior()
        c_c=0
        
    elif c_c == 'healer':
        anouncement['text']='healing warrior'
        DD_healer()
        c_c=0
        
    else:
        SC=2


SC=0

def nextscene():
    global SC
    #SC=1 ##Scene Change
    SC = (SC+1)%3
    #if start==0:
    if SC == 1:
        starting()
    elif SC == 2:
        scene1()
    elif SC == 0:
        scene2()
    
anouncement=Label(War,width=60,bg='gray',text='Attack과 Healing 점수를 정하세요')
anouncement.grid(row=4,column=0,columnspan=3)
nextB=Button(War,width=18,bg='gray',text='다음',command=nextscene)
nextB.grid(row=4,column=3)
wta=random.randint(0,1) ##Whom to attack
start=0


        
