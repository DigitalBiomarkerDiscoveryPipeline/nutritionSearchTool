# Author:        #theBlackFemaleEngineer
# Date:          28 October 2020
# Description:   This is a file for using Joshua's food2vec API to
#                get nutrition information for a food item.


from food2vec.semantic_nutrition import Estimator
import json

def test(search="apple"):
    estimator = Estimator()
    print("---Trying to get an estimate for %s" %search)
    print("\n")
    
    # Search database for nutrition estimates                                                                     
    match = estimator.natural_search("I ate %s" % search)
    outputDict = []
    
    print("\n")
    if (isinstance(match, list)):
        for i in match:
            obj = json.loads(i)
            outputDict.append(obj)
            print("%s" % obj["item_name"])
            print("carboydrates: %.2f" % obj["carbohydrates"])
            print("sugar: %.2f" % obj["sugar"])
            print("total_fats: %.2f" % obj["total_fats"])
            print("sat_fats: %.2f" % obj["sat_fats"])
            print("protein: %.2f" % obj["protein"])
            print("calories: %.2f" % obj["calories"])
            print("cholesterol: %.2f" % obj["cholesterol"])
            print("----------------------------------------\n")
    else:
        obj = json.loads(match)
        outputDict.append(obj)
        print("%s" % obj["item_name"])
        print("carboydrates: %.2f" % obj["carbohydrates"])
        print("sugar: %.2f" % obj["sugar"])
        print("total_fats: %.2f" % obj["total_fats"])
        print("sat_fats: %.2f" % obj["sat_fats"])
        print("protein: %.2f" % obj["protein"])
        print("calories: %.2f" % obj["calories"])
        print("cholesterol: %.2f" % obj["cholesterol"])
        print("----------------------------------------\n")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(outputDict)
    print("\n")
    print(type(outputDict))
    print("\n")
    print(json.dumps(outputDict, indent=4))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")    
    
    return json.dumps(outputDict, indent=4)

test()
