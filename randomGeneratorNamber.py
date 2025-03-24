class GeneratorNumberLsrt:
    @staticmethod
    def non_forbidden_lst(min_bound,max_bound,forbidden_elements):
        all_num=set(list(range(min_bound,max_bound)))
        all_num.difference_update(forbidden_elements)
        return all_num

    @staticmethod
    def random_element_from_lst(lst):
        n= len(lst)
        index=randint(0,n-1)
        return lst[index]
    @staticmethod
    def randomPoly(P,deg,bounded_coef_lst,has_free=True):
        deg_coef=[GeneratorNumberLsrt.random_element_from_lst(bounded_coef_lst) for i in list(range(deg))]
        deg_coef.insert(0,GeneratorNumberLsrt.random_element_from_lst(bounded_coef_lst))
        deg_coef[deg]=randint(1, max(bounded_coef_lst))
        return P(deg_coef)



from abc import ABC, abstractmethod

class QuestionQuiz(ABC):  # מחלקת אבסטרקט
    def __init__(self, question_description,stuntent_ans,expect_ans,google_form_url="",google_form_key={}, canBerefresh=True,state="Practise",maxscore=0):
        self.question_description = question_description
        self.stuntent_ans= stuntent_ans
        self.store_ans={}
        self.expect_ans=expect_ans
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
    def show_description(self,str_dict):
        res= self.question_description.format(**str_dict)
        html(res)

    @abstractmethod
    def submit_stuntent_ans(self):
        pass

    @abstractmethod
    def submit_stuntent_ans_google(self):
        pass



class PolynominalLongDivisionQuestion(QuestionQuiz):
    def __init__(self, question_description,stuntent_ans,expect_ans,google_form_url="",google_form_key={}, canBerefresh=True,state="Practise",maxscore=0,min_bound=-5,max_bound=5):
        super().__init__(question_description,stuntent_ans,expect_ans,google_form_url=google_form_url,google_form_key=google_form_key, canBerefresh=canBerefresh,state=state,maxscore))
        self.min_bound=min_bound
        self.max_bound=max_bound

        self.P=P.<x>=PolynomialRing(QQ)

    def refreshquestion(self):
        P=self.P
        coeff_set=list(range(self.min_bound,self.max_bound))
        degd= randint(2, 4 )
        d= GeneratorNumberLsrt.randomPoly(P,degd,coeff_set)

        degr= randint(0, degd-1 )
        r= GeneratorNumberLsrt.randomPoly(P,degd,coeff_set)

        degq= randint(1, 4 )
        q= randomPoly(P,degq,bounded_coef)
        p= d*q+r
        self.expect_ans={"q" : q ,"r" :r }
        self.store_ans={"q" : "None" ,"r" : "None" }
        self.stuntent_ans={"q" : "None" ,"r" : "None" }
        self.question_vars={"p": p, "d" :d }


    def show_inputs(self):
        label_keys={"q": "\\(q(x)\\)", "r": "\\(r(x)\\)" }

        def create_inputbox(key,label):
            @interact
            def inputbox(qx=input_box(defult="",label=label, width=90, height=2)):
                if(qx=="None"):
                    return
                else:
                    try:
                        self.store_ans[key]=P(qx)
                        show("{label}" +latex(self.store_ans[key]))
                    except:
                        print("Invalid input please check your input")
            for key in label_keys:
                create_inputbox(key,label_keys[key])


    def show_description(self):
        html_code = "<p>"
        px="\\(p(x)\\)"
        pvar="\\("+latex(1/2) +"\\)"
        dx="\\(d(x)\\)"
        dvar="\\("+latex(1/3) +"\\)"
        aligned="{aligned}"
        html_code += """
עבור הפולינומים
$$\\begin{aligned} 2x - 4 &= 6 \\\\
\\\\ 2x &= 10 \\\\
\\\\ x &= 5 \\end{aligned}$$
חשבו את החלוקה של הפולינום

{pvar}
 בפולינום
 {dvar}
 </p>
"""

        str_place_holder={}
        str_place_holder["px"]= "\\(p(x)\\)"
        str_place_holder["pvar"]= "\\("+latex(self.question_vars[p]) +"\\)"
        str_place_holder["dx"]= "\\(d(x)\\)"
        str_place_holder["dvar"]= "\\("+latex(self.question_vars[d]) +"\\)"
        super().show_description(html_code)


