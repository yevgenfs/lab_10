from fishProducts import FishProducts 
from qualityOfFish import QualityOfFish
from imports import Import
from kindOfFish import KindOfFish
from inWhichStatus import InWhichStatus
class FreshFish (FishProducts):
	def __init__(self,keepingStorageConditon=True,price=0,fromWhichCountry="",qualityOfFish=QualityOfFish.MIDLEQUALITY,imports=Import.HOMEREGION,kindOfFish=KindOfFish.FRESHFISH,
		     nameOfFish="",weight=0,experiationDate=0,inWhichStatus=InWhichStatus.LIFE):
	    FishProducts.__init__(keepingStorageConditon,price,fromWhichCountry,qualityOfFish,imports,kindOfFish,
		     nameOfFish,weight)
	    self.experiationDate=experiationDate
	    self.inWhichStatus=inWhichStatus
		

	def __str__ (self):
		return  FishProducts.__str__ (self)+"experiationDate:{},inWhichStatus:{} ".format(
			 self.experiationDate
			 self.inWhichStatus
			)
	
	
	
	def __del__(self):
		print("obj deleted")