import xml.etree.cElementTree as ET

#Get the XML file data
stream = open ('sample.xml','r')

#Parse the data into an ElementTree object
xml = ET.parse(stream)

#Get the 'root' Element object from the ElementTree
root = xml.getroot()

#Iterate through each child of the root Element
for e in root:
    #Print the stringfield version of the element
    print(ET.tostring(e))
    print("")

    #Pring the 'Id' attribuete of the Element object
    print(e.get("Id"))