class Account:
    def __init__(self,accno,cutname,accbal):
        self._accno=accno
        self._cutname=cutname
        self.accbal=accbal


    @property
    def accno(self):
        return self._accno
    

    @accno.setter
    def accno(self,accno):
        self.accno=accno

    @property
    def cutname(self):
        return self._cutname

    @cutname.setter
    def custname(self,cutname):
        self.cutname=cutname

    @property
    def accbal(self):
        return self._accbal

    @accbal.setter
    def accbal(self,new_accbal):
        self._accbal =new_accbal
    




            
        