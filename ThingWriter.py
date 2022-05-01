#Thing Writer 1.0
from datetime import datetime
def Printer():
    Appendix = open('FixedLocation.txt', 'a')
    thingToAppend = input("What message would you like to add? > ")
    rn = datetime.now()
    timeForWords = rn.strftime("%m/%d/%Y")
    Appendix.writelines(timeForWords +
                   ' -- ' +
                   thingToAppend +
                   "\n")
    Appendix.close()
Printer()

