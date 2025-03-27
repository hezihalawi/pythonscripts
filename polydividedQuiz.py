try:
    load("https://raw.githubusercontent.com/hezihalawi/pythonscripts/refs/heads/main/GeneratorNumberLst.py")
    load("https://raw.githubusercontent.com/hezihalawi/pythonscripts/refs/heads/main/Questionbank.py")
    load("https://raw.githubusercontent.com/hezihalawi/pythonscripts/refs/heads/main/LongDivisionQuestion1.sage")
    Q=[[]]
    Q[0]=PolynominalLongDivisionQuestion(google_form_url="")
    print("הלומדה נוצרה בהצלחה")
except:
    print("fail")
