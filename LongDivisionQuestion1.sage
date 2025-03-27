class PolynominalLongDivisionQuestion(QuestionQuiz):
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
        print("try")
        for key in self.store_ans:
            print(self.store_ans[key])
            if (self.store_ans[key]=="None"):
                html("")

        table_str=""
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
        table_html+=table_str_rows.format(var_name=" \\(q(x)\\)",
                                          sduent_ans=" \\( " + latex(self.stuntent_ans["q"]) +"\\)",
                                          expect_ans=" \\( " + latex(self.expect_ans["q"]) +"\\)",
                                          howwrite=str(self.expect_ans["q"])
                                          )
        table_html+=table_str_rows.format(var_name=" \\(r(x)\\)",
                                          sduent_ans=" \\( " + latex(self.stuntent_ans["r"]) +"\\)",
                                          expect_ans=" \\( " + latex(self.expect_ans["r"]) +"\\)",
                                          howwrite=str(self.expect_ans["r"])
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
        coeff_set=list(range(self.min_bound,self.max_bound))
        degd= randint(2, 4 )
        d= GeneratorNumberLsrt.randomPoly(P,degd,coeff_set)

        degr= randint(0, degd-1 )
        r= GeneratorNumberLsrt.randomPoly(P,degr,coeff_set)

        degq= randint(1, 4 )
        q= GeneratorNumberLsrt.randomPoly(P,degq,coeff_set)

        p= d*q+r
        self.expect_ans={"q" : q ,"r" :r }
        self.store_ans={"q" : "None" ,"r" : "None" }
        self.stuntent_ans={"q" : "None" ,"r" : "None" }
        self.question_vars={"p": p, "d" :d }
        self.hascheck=False
        self.score=0


    def store_stuntent_ans(self):
        str_print="{var_name}={yours}"
        for key in self.stuntent_ans:
            self.stuntent_ans[key]= self.store_ans[key]
        table_html = "<p>המערכת זיהתה שהכנסת את התשובות הבאות:<table border='1' style='border-collapse: collapse; width: 100%;'>"

        table_str_rows="<tr>" + "<th> {var_name}</th>" + "<th> {sduent_ans} </th>" + "</tr>"
        table_html+=table_str_rows.format(var_name=" משתנה",
                                          sduent_ans="תשובתך",
                                          )

        table_html+=table_str_rows.format(var_name=" \\(q(x)\\)",
                                          sduent_ans=" \\( " + latex(self.stuntent_ans["q"]) +"\\)",
                                          )
        table_html+=table_str_rows.format(var_name=" \\(r(x)\\)",
                                          sduent_ans=" \\( " + latex(self.stuntent_ans["r"]) +"\\)",

                                          )

        table_html += "</table></p>"
        show(html(table_html))


    def show_inputs(self):
        label_keys={"q": "q(x)", "r": "r(x)" }
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
עבור הפולינומים
$$\\begin{aligned}
p(x)&={pvar} & d(x)&={dvar}
\\end{aligned}$$
חשבו את החלוקה של הפולינום

\\({px}\\)
 בפולינום
 \\({dx}\\)
 </p>
"""

        str_place_holder={}
        str_place_holder["px"]= "p(x)"
        str_place_holder["pvar"]= latex(self.question_vars["p"])
        str_place_holder["dx"]= "d(x)"
        str_place_holder["dvar"]= latex(self.question_vars["d"])
        str_place_holder["aligned"]=aligned
        super().show_description(html_code,str_place_holder)

