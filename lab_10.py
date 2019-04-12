class Oscillograph :
	def __init__(self,maximumSignalFrequency,memoryCapacity,brand,
		     color="",amplitude=0,minimumSignalFrequency=0):
		self.maximumSignalFrequency=maximumSignalFrequency
		self.memoryCapacity=memoryCapacity
		self.brand=brand
		self.color=color
		self.amplitude=amplitude
		self.minimumSignalFrequency=minimumSignalFrequency
	def __str__ (self):
		return "maximumSignalFrequency :{},memoryCapacity:{},brand:{},color:{},amplitude:{},minimumSignalFrequency:{}, ".format(
			self.maximumSignalFrequency,self.memoryCapacity,
			self.brand,self.color,self.amplitude,
			self.minimumSignalFrequency
			)
	size=10
	
	def getSize():
		return Oscillograph.size
	def __del__(self):
		print("obj deleted")

o = Oscillograph(0,0,0)
print(o)
u = Oscillograph(0,0,0,0,0,0)
print(u)
w = Oscillograph(0,0,0,0,0)
print(w)
print(Oscillograph.getSize())
