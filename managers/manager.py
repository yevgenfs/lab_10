import sys
sys.path.insert(0,'../models')

from fishProducts import FishProducts 
from qualityOfFish import QualityOfFish
from imports import Import
from kindOfFish import KindOfFish
from inWhichStatus import InWhichStatus


class FishProductsManager:
    def __init__(self, fishProducts):
        self.fishProducts = fishProducts

    @staticmethod
    def sortByName(fishProducts, descending=False):
        return sorted(fishProducts, key=lambda fishProducts: fishProducts.nameOfFish, reverse=descending)

    @staticmethod
    def sortingByWeight(fishProducts, descending=True):
        return sorted(fishProducts, key=lambda fishProducts: fishProducts.weight, reverse=descending)
    
    @staticmethod
    def sortingByPrice(fishProducts, descending=True):
        return sorted(fishProducts, key=lambda fishProducts: fishProducts.price, reverse=descending)
     







def main():
    
    fishes = []
    fishes.append(FishProducts(True, 20, "Ukraine", QualityOfFish.MIDLEQUALITY, Import.HOMEREGION, KindOfFish.COLDFISH, "ama",45))
    fishes.append(FishProducts(True, 20, "Ukraine", QualityOfFish.MIDLEQUALITY, Import.HOMEREGION, KindOfFish.COLDFISH, "ama",45 ))
    fishes.append(FishProducts(True, 10, "Ukraine", QualityOfFish.MIDLEQUALITY, Import.HOMEREGION, KindOfFish.COLDFISH, "fa" ,60))
    fishes.append(FishProducts(True, 50, "Ukraine", QualityOfFish.MIDLEQUALITY, Import.HOMEREGION, KindOfFish.FRESHFISH,    "da" ,90 ))
    fishes.append(FishProducts(True, 50, "Ukraine", QualityOfFish.MIDLEQUALITY, Import.HOMEREGION, KindOfFish.HERRING,  "sha",20))

    manager = FishProductsManager(fishes)

    for i in FishProductsManager.sortByName(fishes):
        print(i)
    print()

    for i in FishProductsManager.sortingByWeight(fishes):
        print(i)
    print()
    for i in FishProductsManager.sortingByPrice(fishes):
        print(i)
    print()

main()
