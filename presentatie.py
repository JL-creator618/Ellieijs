from helper import som

mijn_dict = {
    'vis' : 10, 
    'vlees' : 25, 
    'overige' : 15
    }
totaal = som(mijn_dict)
#totaal = 50

def presenteer (dict,totaal):
    pass
    k = dict.keys()
    v = dict.values()
    for k, v in dict.items():
        print (f"{k} : {v} euro")
    pass
    print ("=======================")
    print (f"Totaal : {totaal} euro")
    return()

#print(presenteer(mijn_dict,totaal))
    










