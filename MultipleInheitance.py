#MultiplePublic
class Student:
	def getData(self,x,y):
		self.rollno=x
		self.name=y
class Sports:
	def getSportMarks(self,s):
		self.sportmarks=s
class Marks(Student,Sports):
    def getMarks(self,p,c,m):
        self.phy=p
        self.che=c
        self.maths=m
    def calculate(self):
        self.total=self.phy+self.che+self.maths+self.sportmarks
    def display(self):
        print("rollno:-",self.rollno)
        print("Name:-",self.name)
        print("PHy:-",self.phy)
        print("Che:-",self.che)
        print("Maths:",self.maths)
        print("Sportsmarks:-",self.sportmarks)
        print("Calculate:-",self.total)
#--main-- 
k=Marks()
k.getData(1234,"Chhavi")
k.getMarks(98,99,97)
k.getSportMarks(89)
k.calculate()
k.display()
