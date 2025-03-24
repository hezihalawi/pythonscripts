
from abc import ABC, abstractmethod

class QuestionQuiz(ABC):  # מחלקת אבסטרקט
    def __init__(self,google_form_url="",google_form_key={}, canBerefresh=True,state="Practise",maxscore=0):
        self.google_form_url=google_form_url
        self.google_form_key=google_form_key
        self.canBerefresh=canBerefresh
        self.state=state
        self.maxscore=maxscore
        self.scroe=0


    @abstractmethod
    def show_inputs(self):
        pass
    @abstractmethod
    def refreshquestion(self):
        pass
    def show_description(self,question_description,str_dict):
        res= question_description.format(**str_dict)
        show(html(res))

    @abstractmethod
    def store_stuntent_ans(self):
        pass

    @abstractmethod
    def grade_ans(self):
        pass
    @abstractmethod
    def submit_stuntent_ans_google(self):
        pass
