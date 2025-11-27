class LimQuestion(QuestionQuiz):
    def __init__(self,google_form_url="",google_form_key={}, canBerefresh=True,state="Practise",maxscore=0,min_bound=-5,max_bound=5):
        super().__init__(google_form_url=google_form_url,google_form_key=google_form_key, canBerefresh=canBerefresh,state=state,maxscore=maxscore)
        self.min_bound=min_bound
        self.max_bound=max_bound
        P=PolynomialRing(QQ,["x"])
        self.P=P
        self.refreshquestion()

    def submit_stuntent_ans_google(self):
        pass
    def grade_ans(self):
        isCorrect=True
        table_str="<p> </p>"
        for key in self.stuntent_ans:
            isCorrect=isCorrect and (self.stuntent_ans[key]== self.expect_ans[key])


        table_html = "<p><table border='1' style='border-collapse: collapse; width: 100%;'>"

        table_str_rows="<tr>" + "<th> {var_name}</th>" + "<th> {sduent_ans} </th>" + "<th> {expect_ans} </th>" + "<th> {howwrite} </th>"  "</tr>"
        table_html+=table_str_rows.format(var_name=" משתנה",
                                          sduent_ans="תשובתך",
                                          expect_ans="התשובה הנכונה",
                                          howwrite="איך מזינים"
                                          )

        table_str_rows="<tr>" + "<th> {var_name}</th>" + "<th> {sduent_ans} </th>" + "<th> {expect_ans} </th>" + "<th align=left; dir=""ltr""> {howwrite} </th>"  "</tr>"
        table_html+=table_str_rows.format(var_name=" \\(r(x)\\)",
                                          sduent_ans=" \\( " + latex(self.stuntent_ans["lim"]) +"\\)",
                                          expect_ans=" \\( " + latex(self.expect_ans["lim"]) +"\\)",
                                          howwrite=str(self.expect_ans["lim"])
                                          )

        table_html += "</table>"
        if(isCorrect):
            table_html+="תשובתך נכונה כל הכבוד"
            self.score=self.maxscore
        else:
            table_html+="תשובתך שגויה "
            self.score=0

        table_html += "</p>"
        self.hascheck=True
        show(html(table_html))





    def refreshquestion(self):
        P=self.P
        lst_gen= GeneratorNumberLsrt.non_forbidden_lst(self.min_bound,self.max_bound,set([0]))

        a=GeneratorNumberLsrt.random_element_from_lst(lst_gen)
        b= GeneratorNumberLsrt.random_element_from_lst(lst_gen)
        c=  -b*a

        num= self.P("x**2+b*x +c")
        den= self.P("x-a")

        self.a=a
        self.num=num
        self.den= den

        self.expect_ans={"lim" : 1+ b/(2*a)}
        self.store_ans={"lim" : "None"  }
        self.stuntent_ans={"lim" : "None" }
        self.question_vars={"p": num, "den" :den }
        self.hascheck=False
        self.score=0


    def store_stuntent_ans(self):
        str_print="{var_name}={yours}"
        for key in self.stuntent_ans:
            self.stuntent_ans[key]= self.store_ans[key]
        table_html = "<p>המערכת זיהתה שהכנסת את התשובה הבאה:<table border='1' style='border-collapse: collapse; width: 100%;'>"

        table_str_rows="<tr>" + "<th> {var_name}</th>" + "<th> {sduent_ans} </th>" + "</tr>"
        table_html+=table_str_rows.format(var_name=" משתנה",
                                          sduent_ans="תשובתך",
                                          )

        table_html+=table_str_rows.format(var_name=" \\Lim)\\)",
                                          sduent_ans=" \\( " + latex(self.stuntent_ans["lim"]) +"\\)",
                                          )
        table_html += "</table></p>"
        show(html(table_html))


    def show_inputs(self):
        label_keys={"Lim": "lim"}
        P=self.P
        def create_inputbox(key,label):
            @interact
            def inputbox(qx=input_box(defult="",label="\\("+ label+"\\)", width=90, height=2)):
                if(self.hascheck):
                    return
                if(qx=="None"):
                    return
                else:
                    try:
                        self.store_ans[key]=P(qx)
                        show(label+ "=" +latex(self.store_ans[key]))
                    except:
                        print("Invalid input please check your input")
        for key in label_keys:
            create_inputbox(key,label_keys[key])


    def show_description(self):
        html_code = "<p>"
        aligned="{aligned}"
        html_code += """
חשבו את הגבול הבא:

$$ \\lim_{x \\to {a}} \\frac{{\\sqrt{{{expression}}} - {a}}}{{{c}}} $$
 </p>
"""

        str_place_holder={}
        str_place_holder["a"]= latex(self.a)
        str_place_holder["expression"]= latex(self.num)
        str_place_holder["c"]= latex(self.den)
        str_place_holder["aligned"]=aligned
        super().show_description(html_code,str_place_holder)

