from parser import Parser
import numpy as np
import json

class Calculation():
    """
    Initializing the Calculation class
    @param applicant      A Json file of the applicant that the user want to compare
    """
    def __init__(self, applicant = None):
        self.parser = Parser()
        if(applicant is not None):
            self.parser.updateApplicant(applicant)

    """
    Compute the weighted cosine similarity
    @param weight       The importance of each attribute when considering an applicant
    """
    def __cosineSim__(self, weight):
        #Get the information from the parser
        team = self.parser.getTeam()
        applicant = self.parser.getApplicant()
        #extracting the information that's needed
        appName, appAtt = self.__extract__(applicant)
        _, teamAtt = self.__extract__(team)
        # compute the dot product between the weightedTeamAtt and appAtt
        appAtt, teamAtt = np.array(appAtt), np.array(teamAtt)
        teamAttAvg = np.transpose(np.mean(teamAtt,axis=0))
        weightedTeamAtt = np.multiply(teamAttAvg, weight)
        score = appAtt @ weightedTeamAtt
        #Finding the two norms for the two vectors
        normApp = np.linalg.norm(appAtt, axis=1)
        normTeam = np.linalg.norm(weightedTeamAtt)
        #compute the cosine similiarity for the two vectors
        score = score/(normApp * normTeam)
        return appName, score

    """
    Extract the information needed 
    @param data       The data from which to extract information from 
    """
    def __extract__(self, data):
        a = []
        b = []
        for i in data:
            a.append(i[0][0]) #retrieve the name
            b.append(i[1]) #retrieve the attributes
        return a, b

    """
    Publicly available to user to compute scores but does not allow them to directly
    alter any instance variables
    @param weight       The importance of each attribute when considering an applicant
    """
    def calculate(self, weight=None):
        if weight is None:
            weight = [1, 0.7, 0.5, .1]
        print(weight)
        weight = np.array(weight)
        appName, score = self.__cosineSim__(weight)
        self.outputJSON(appName, score)
        return 1

    """
    Outputs the computed score to a JSON file
    @param name         The name of the appicants 
    @param score        The cosine similarity score that each applicant recieved
    """
    def outputJSON(self, name, score):
        data = [{"name": name, "score": score} for name, score in zip(name, score)]
        headers = {"scoredApplicants": data}
        with open('scoredOutput.json', 'w') as file:
            json.dump(headers,file,indent=2, separators=(",", ": "))
