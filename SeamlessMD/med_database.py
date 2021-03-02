#importing json files
import json

# Name of patient:
# Organization name:
# Gender:
# Number of conditions they have:
# List of all conditions:
#'name': [{'family': ['Levin'], 'given': ['Henry']}], 'gender': 'male', 'birthDate': '2002-09-24', 'managingOrganization': {'reference': 'Organization/2.16.840.1.113883.19.5', 'display': 'University Health Network'}, 'conditions': ['Diabetes', 'High blood pressure', 'Asthma']}

def Rewrite(elements):
    string = "<!DOCTYPE html>\n<html lang=\"en\">\n<ul>\n"
    for s in elements:
        string += "<p>" + s + "</p>\n"
    string += "</ul>\n</html>"
    return string
    
with open('patient.json') as f:
    data = json.load(f)

name = str(data["name"][0]["given"][0] + " " + data["name"][0]["family"][0])
orgName = str(data["managingOrganization"]["display"])
gender = str(data["gender"])
numConditions = str(len(data["conditions"]))
ConditionList = ', '.join([str(elem) for elem in data["conditions"]])

OutputList = ["Name of patient: "+name, "Organization name: "+orgName, "Gender: "+gender, "Number of conditions they have: "+numConditions, "List of all conditions: "+ConditionList]
outString = Rewrite(OutputList)

file = open("index.html", "w")
file.write(outString)
file.close()



