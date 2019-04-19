from fishSearchAndSort import FishSearchAndSort 
from qualityOfFish import QualityOfFish
from imports import Import
from kindOfFish import KindOfFish

class FishProducts (FishSearchAndSort):
	def __init__(self,keepingStorageConditon=True,price=0,fromWhichCountry="",qualityOfFish=QualityOfFish.MIDLEQUALITY,imports=Import.HOMEREGION,kindOfFish=KindOfFish.COLDFISH,
		     nameOfFish="",weight=0):
		self.keepingStorageConditon=keepingStorageConditon
		self.price=price
		self.fromWhichCountry=fromWhichCountry
		self.qualityOfFish=qualityOfFish
		self.imports=imports
		self.kindOfFish=kindOfFish
		self.nameOfFish=nameOfFish
		self.weight=weight
		
	def __str__ (self):
		return "keepingStorageConditon :{},price:{},fromWhichCountry:{},qualityOfFish:{},imports:{},kindOfFish:{},nameOfFish:{},weight:{}, ".format(
			self.keepingStorageConditon,self.price,
			self.fromWhichCountry,self.qualityOfFish,self.imports,
			self.kindOfFish,self.nameOfFish ,self.weight
			)
	
	
	
	def __del__(self):
		print("obj deleted")

