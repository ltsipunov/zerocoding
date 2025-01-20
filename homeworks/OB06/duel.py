from random import random as rnd
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.shots = 10
        self.turns_to_reload = 3
        self.reload=0

    def precision(self,distance):
        return round(self.health/100*(100-distance)/100 ,2)

    def attack(self, other,distance):
        if self.shots:
            self.shots-= 1
            self.reload=self.turns_to_reload
            print(f"{self.name} стреляет! ")
            if rnd() < self.precision(distance):
                print('Попал!')
                other.health -= self.attack_power
            else:
                print('Мимо!')
        else:
            print(f"{self.name} больше не может стрелять! ")

    def is_active(self):
        return self.shots > 0

    def is_alive(self):
        return self.health > 0

    def report_status(self):
        print(f"{self.name} осталось здоровья: {self.health} и выстрелов {self.shots}")

    def report_final_status(self):
        if self.health == 0:
            print(f"{self.name} погиб на месте ! ")
        elif self.health <= 20:
            print(f"После дуэли  {self.name} был доставлен в госпиталь, где вскоре умер от ран ")
        elif self.health <= 50:
            print(f"{self.name} лечится в госпитале ")
        elif self.health < 95:
            print(f"Легко раненый {self.name}  уехал в деревню ")
        else :
            print(f" {self.name} женился ! :))   ")

class Game:
    def __init__(self, names):
        self.players=[ Hero(names[0]),Hero(names[1]) ]
        self.distance = 100

    def start(self):
        print(f" {self.players[0].name} вызвал на дуэль {self.players[0].name} ! Противники сближаются... ")
        while self.go() :
            self.distance = max(4,self.distance - 4 )
            print(f"========= Дистанция {self.distance} шагов =========")
            for i in [0,1]:
                if self.players[i].reload > 0:
                    print(f"{self.players[i].name} перезаряжает.. ")
                    self.players[i].reload -= 1
                elif rnd()>0.5 :
                    self.players[i].attack(self.players[1-i],self.distance)
                    self.players[1-i].report_status()
                else:
                    print(f"{self.players[i].name} Готов к стрельбе. Целится....")

        self.report_final_status()

    def go(self):
        return all([p.is_alive() for p in  self.players]) and any([p.is_active() for p in  self.players])

    def report_final_status(self):
        if  self.players[0].health ==0 or  self.players[1].health == 0:
            print("Дуэль закончилась трагически :(.... ")
        elif self.players[0].shots <= 0 and self.players[1].shots <= 0:
            print(" Противники расстреляли все патроны , чем защитили свою честь  :)" )
        else:    # This should not happen
            print("Дуэль законилась неописуемым скандалом!")
        for  i in [0,1]:
            self.players[i].report_final_status()
        print('======= GAME OVER ======= ' )