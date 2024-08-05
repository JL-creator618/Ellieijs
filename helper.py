def decoreer(tekst=""):
    lengte = len (tekst) + 4
    print ()
    print (lengte * "*")
    print (f"* {tekst} *")
    print (lengte * "*")
    print ()

def fooi_pp (bedrag, persoon):
    try:
        bedrag_pp = bedrag / persoon
    except:
        bedrag_pp = "??"
    return f"Het bedrag per persoon {bedrag_pp} euro."

#b = int (input("Welk bedrag zit er in  de fooienpot?"))
#p = int (input ("Over hoeveel mensen moet de pot verdeeld worden?"))

#print (fooi_pp (b, p))

def onderstreep (tekst = ""):
    uit = []
    uit.append (tekst)
    uit.append (len(tekst) * "=")
    return uit

#print (onderstreep ("korting"))
    
def som(any_dict = {}):
    total_som = sum (any_dict.values())
    return total_som
