import xml.etree.ElementTree as ET

dimensionCollection = {
    'path': "./xml/dimensionCollection.xml", 
    'headers': ["Dimension_Code"]}
measurementCollection = {
    'path': "./xml/measurementCollection.xml", 
    'headers': ["Measurement_ID", "Measurement_Code", "Dimension_Code"]}
unitCollection = {
    'path': "./xml/unitCollection.xml",
    'headers': ["Unit_Code", "Unit_Abbreviation", "Unit_Name", "Dimension_code", "Factor", "Offset"]}
unitSystemDefinitionCollection = {
    'path': "./xml/unitSystemDefinitionCollection.xml", 
    'headers': ["Unit_System_Code", "Measurement_ID", "Unit_ID"]}

def main():
    # handle dimensionCollection
    tree = ET.parse(dimensionCollection['path'])
    root = tree.getroot()
    with open("./csv/dimensionCollection.csv", "w+") as f:
        f.write(','.join(dimensionCollection['headers']) + '\n')
        for child in root:
            f.write(child[0].text + '\n')

    # handle measurementCollection
    tree = ET.parse(measurementCollection['path'])
    root = tree.getroot()
    with open("./csv/measurementCollection.csv", "w+") as f:
        f.write(','.join(measurementCollection['headers']) + '\n')
        numCols = len(measurementCollection['headers'])
        for child in root:
            values = [child[i].text for i in range(numCols)]
            f.write(','.join(values) + '\n')

    # handle unitCollection
    tree = ET.parse(unitCollection['path'])
    root = tree.getroot()
    with open("./csv/unitCollection.csv", "w+") as f:
        f.write(','.join(unitCollection['headers']) + '\n')
        numCols = len(unitCollection['headers'])
        for child in root:
            values = [child[i].text for i in range(numCols)]
            f.write(','.join(values) + '\n')

    # handle unitSystemDefinitionCollection
    tree = ET.parse(unitSystemDefinitionCollection['path'])
    root = tree.getroot()
    with open("./csv/unitSystemDefinitionCollection.csv", "w+") as f:
        f.write(','.join(unitSystemDefinitionCollection['headers']) + '\n')
        numCols = len(unitSystemDefinitionCollection['headers'])
        for child in root:
            values = [child[i].text for i in range(numCols)]
            f.write(','.join(values) + '\n')

if __name__ == "__main__":
    main()
