from rapidfuzz import fuzz
from rapidfuzz import process
from rapidfuzz.fuzz import partial_ratio
from rapidfuzz.utils import default_process


class Choice:
    '''
        Utility Class to use fuzzy logic to return a match
        for a query from a set of choices
    '''
    __confidenceLevel = 80

    @staticmethod
    def getChoice(request:str=None, options: list=None):
        '''
        This returns a single value that matches your request
        :param request: the value you are searching for
        :param options: a list of the options you can choose from
        :return result: a tuple (match, confidence, index)
            match: a value in options that closest matches request value
            confidence: a value out of 100 that reflects the percentage of confidence that the request matches the match
            index: returns the index of the match in the options list
        '''

        choice = None

        ''' Check of "Choice" is in one of the "Options'''
        result = process.extractOne(request, options, scorer=fuzz.WRatio, processor=default_process)
        (match, confidence, index) = result

        if confidence > Choice.getConfidenceLevel():
            choice = match

        return choice
    
    @staticmethod
    def match(word1, word2) -> bool:
        '''
        Compares 2 words and if within level of confidence they match returns TRUE, else  return FALSE
        '''
        return fuzz.ratio(word1, word2, processor=default_process) > Choice.getConfidenceLevel()
    
    @staticmethod
    def getChoices(request=None, options=None):
        ''' This returns multiple values that match your request'''
        choices = []
        results = process.extract(request, options, scorer=fuzz.WRatio, processor=default_process)
        # return an set of choices [(match,confidence, index),(match,confidence, index)...]

        for result in results:
            (match,confidence,index) = result
            if confidence > Choice.getConfidenceLevel():
                choices.append(match)

        return choices
    
   
    @staticmethod
    def getConfidenceLevel():
        return Choice.__confidenceLevel

    @staticmethod
    def setConfidenceLevel(confidence):
        Choice.__confidenceLevel = confidence