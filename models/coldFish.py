from fishProducts import FishProducts 
from qualityOfFish import QualityOfFish
from imports import Import
from kindOfFish import KindOfFish

class ColdFish (FishProducts):
	def __init__(self,keepingStorageConditon=True,price=0,fromWhichCountry="",qualityOfFish=QualityOfFish.MIDLEQUALITY,imports=Import.HOMEREGION,kindOfFish=KindOfFish.COLDFISH,
		     nameOfFish="",weight=0,temperature=0):
	    FishProducts.__init__(keepingStorageConditon,price,fromWhichCountry,qualityOfFish,imports,kindOfFish,
		     nameOfFish,weight)
	    self.temperature=temperature
		

	def __str__ (self):
		return  FishProducts.__str__ (self)+"temperature:{} ".format(
			 self.temperature
			)
	
	
	
	def __del__(self):
		print("obj deleted")

#print(o)
#u = Oscillograph(0,0,0,0,0,0)
#print(u)
#w = Oscillograph(0,0,0,0,0)
#print(w)
#print(Oscillograph.getSize())
