class bank_account():
    def __init__(self,nr):
        self.nr=nr
        self.balance=0
    def show_info(self):   
        print(f"Rachunek nr: {self.nr[0:2]} {self.nr[2:6]} {self.nr[6:10]} {self.nr[10:14]} {self.nr[14:18]} {self.nr[18:22]} {self.nr[22:26]}")
        print(f"Saldo: {self.balance} zł ")
    def deposite(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount    
        else:
            print("Niewystarczjąca ilość środków na rachunku")     
konto=bank_account("12345655559090111100007722")     
konto.show_info()  
konto.deposite(25.30)  
konto.show_info() 
konto.withdraw(31.70)
konto.show_info()
konto.withdraw(14)  
konto.show_info()