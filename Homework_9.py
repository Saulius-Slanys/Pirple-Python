# Homework #9



class Vehicle:
	def __init__(self, Make, Model, Year, Weight):
		self.Make = Make
		self.Model = Model
		self.Year = Year
		self.Weight = Weight
		self.NeedsMaitenance = False
		self.TripsSinceMaitenance = 0


	def repair(self):
		self.NeedsMaitenance = False
		self.TripsSinceMaitenance = 0

	def __str__(self):
		return(self.Make + ', ' + self.Model + ', ' + str(self.Year) + ', ' + str(self.Weight))




class Cars(Vehicle):
	def __init__(self, Make, Model, Year, Weight):
		Vehicle.__init__(self, Make, Model, Year, Weight)
		self.isDriving = False

	def drive(self):
		self.isDriving = True
		self.TripsSinceMaitenance += 1
		if self.TripsSinceMaitenance > 100:
			self.NeedsMaitenance = True

	def Stop(self):
		self.isDriving = False



class Planes(Vehicle):
	def __init__(self, Make, Model, Year, Weight):
		Vehicle.__init__(self, Make, Model, Year, Weight)
		self.isFlying = False

	def fly(self):
		self.isFlying = True
		if self.TripsSinceMaitenance >= 2:
			self.NeedsMaitenance = True
			print('This plane can not take off until repaired')
		else:
			self.TripsSinceMaitenance += 1

	def land(self):
		self.isFlying = False


myCar = Cars('Volvo', 'V40', 2001, 1500)
dadsCar = Cars('Nissan', 'Note', 2015, 1200)
brothersCar = Cars('Subaru', 'Legacy', 2005, 1400)


myCar.TripsSinceMaitenance = 100
dadsCar.TripsSinceMaitenance = 99
brothersCar.TripsSinceMaitenance = 98

myCar.drive()
dadsCar.drive()
brothersCar.drive()
myCar.drive()


print(myCar, ', needs maintenance: ', str(myCar.NeedsMaitenance), ', trips since last maintenance is: ', str(myCar.TripsSinceMaitenance))
print(dadsCar, ', needs maintenance: ', str(dadsCar.NeedsMaitenance), ', trips since last maintenance is: ', str(dadsCar.TripsSinceMaitenance))
print(brothersCar, ', needs maintenance: ', str(brothersCar.NeedsMaitenance), ', trips since last maintenance is: ', str(brothersCar.TripsSinceMaitenance))



myPlane = Planes('Airbus', 'A320', 2010, 11500)

myPlane.fly()
myPlane.land()

print(myPlane, ', needs maintenance: ', str(myPlane.NeedsMaitenance), ', flyies since last maintenance is: ', str(myPlane.TripsSinceMaitenance))

myPlane.fly()
myPlane.land()
myPlane.fly()

print(myPlane, ', needs maintenance: ', str(myPlane.NeedsMaitenance), ', flyies since last maintenance is: ', str(myPlane.TripsSinceMaitenance))
