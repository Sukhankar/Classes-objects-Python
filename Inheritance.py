# Single Inheritance
 class Animal:
     def speak(self):
         print("this is the parent class")

 class Dog(Animal):
     def bark(self):
         print("Dog is child of Animal class")
 d=Dog()
 d.bark()
 d.speak()


# Multiple inheritance
 class A:
     def papu(self):
         print("This is papu who can't dance sala")

 class B:
     def raju(self):
         print("25 din me paisa double, Saala paisa he paisa hoga 😁😁😁")
        
 class C(A,B):
     def tuntun_mosi(self):
         print("Hello friends Ladu Kha LOO ")

 output_deka=C()
 output_deka.papu()
 output_deka.raju()
 output_deka.tuntun_mosi()

# multi level inheritance
 class Ajja:
     def supari(self):
         print("Ajja: Are pora jara tabaku chuna de re")
 class Por(Ajja):
     def bap(self):
         print("Bap: Papa man bal")
 class Natu(Por):
     def harami(self):
         print("Natu: Me lay harami natu ahe jo ajja cha chunya cha paket lapvtho")
 nati_goti=Natu()
 nati_goti.supari()
 nati_goti.bap()
 nati_goti.harami()
