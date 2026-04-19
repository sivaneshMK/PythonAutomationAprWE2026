
'''
inherites properties of parent class by the child class

use
------
it will reduce the number object creations
it will improve code reusablity
it will improve code readability

types
------
single  --> parent --> child
multiple --> parent1
                       child
             parent2
multilevel --> parent --> child --> grandchild
hierarchical --> parent --> child1
                        --> child2
hybrid --> combination of one or more inheritance type
is called as hybrid

Halamma    --> Madhu --> Aari
         --> Anandhi
         --> gokul
Mahalingan

'''

class Halamma():
    def gold(self):
        print("5KG of gold")

    def silver(self):
        print("10 KG of silver")

    def house(self):
        print("3BHK ECR Chennai")

class Mahalingan:

    def house(self):
        print("2BHK OMR Chennai")

    def car(self):
        print("Audi q4")

class Madhupriya(Halamma, Mahalingan ):

    def bike(self):
        print("Honda Deo")

    def laptop(self):
        print("HP")

# maha = Mahalingan()
# maha.car()
# maha.house()

class Aari(Madhupriya):

    def toys(self):
        print("Gun")

class Anandhi(Mahalingan, Halamma):
    def Cycle(self):
        print("Hero Cycle")

class Gokul(Mahalingan, Halamma):
    def Scooty(self):
        print("TVS Pep+")



# anandhi = Anandhi()
# anandhi.car()
# anandhi.Cycle()
# anandhi.house()
# #anandhi.laptop()

madhu = Madhupriya()
madhu.bike()
madhu.laptop()
madhu.car()
madhu.house()
madhu.gold()
madhu.silver()

# aari = Aari()
# aari.toys()
# aari.laptop()
# aari.house()
# aari.car()
# aari.bike()

'''
driver = webdriver.Chrome()
driver.get("url")
driver.find_element(By.NAME, "q").send_keys("email id")

XPath  --> XML Path

Relative
    
    //tagname[@propertyname = 'property value']
    //tagname[text()= 'Text of the element']
    //tagname[contains(@propertyname, "property value")]
    //tagname[contains(text(),'text of the element')]
    //parentelement/childelemnet
    //precedingsibling//following-sibling::follow sibling element
    
Absolute
        /html/body..../div

'''