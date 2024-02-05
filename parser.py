import json
import re

class Parser:
    """
    Initializing the Parser class with information on team and applicant
    """
    def __init__(self):
        self.json = "test.json"
        self.team = None
        self.applicant = None
        self.__parse__()

    """
    Converts a json file into dictionary
    """
    def __parse__(self):
        try:
            #if the json is well formatted
            with open(self.json, 'r') as file:
                data = json.load(file)

            #separate function to process the teams and applicants because it could be the case that
            #applicants and teams have very different formats
            self.team = self.__processData__(data["team"])
            self.applicant = self.__processData__(data["applicants"])
        except:
            print("Json is ill-formatted")
            exit()

    """
    Process the data for better accessibility
    Each data point will be represented as an array 
    Ex) Team:      [[team], [attribute1, attribute2, attribute 3, etc.]]
        Applicant: [[applicant], [attribute1, attribute2, attribute 3, etc.]]
    """
    def __processData__(self, data):
        processed = []
        for d in data:
            curr = []
            li = list(d.items())
            for i in range(len(li)):
                if(type(li[i][1]) is not dict):
                    curr.append([li[i][1]])
                else:
                    #gets the numeric values from the list
                    attributes = [int(value) for value in li[i][1].values() if re.search(r'\d+', str(value))]
                    curr.append(attributes)
            processed.append(curr)
        return processed

    """
    Getter method for teams
    """
    def getTeam(self):
        return self.team

    """
    Getter method for applicants
    """
    def getApplicant(self):
        return self.applicant

    """
    Mutator method for applicants in case any changes need to be made
    @param applicantJSON            A new JSON file containing the information about applicants
    """
    def updateApplicant(self, applicantJSON):
        with open(applicantJSON, 'r') as file:
            data = json.load(file)
        self.applicant = self.__processData__(data["applicants"])
