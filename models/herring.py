from fishProducts import FishProducts 
from qualityOfFish import QualityOfFish
from imports import Import
from kindOfFish import KindOfFish
s
class Herring (FishProducts):
	def __init__(self,keepingStorageConditon=True,price=0,fromWhichCountry="",qualityOfFish=QualityOfFish.MIDLEQUALITY,imports=Import.HOMEREGION,kindOfFish=KindOfFish.HERRING,
		     nameOfFish="",weight=0,experiationDate=0,quantiti=0):
	     FishProducts.__init__(keepingStorageConditon,price,fromWhichCountry,qualityOfFish,imports,kindOfFish,
		     nameOfFish,weight)
	    self.experiationDate=experiationDate
	    self.quantiti=quantiti
		

	def __str__ (self):
		return FishProducts.__str__ (self)+"experiationDate:{},inWhichStatus:{} ".format(
			 self.experiationDate
			 self.quantiti
			)
	
	
	
	def __del__(self):
		print("obj deleted")