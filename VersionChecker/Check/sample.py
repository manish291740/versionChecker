import re
a=['Tkmu80097.in.uhde.org','Tkmu61469.in.uhde.org','dhee1234567.in.uhde.org']
for i in a:
    matchreg = re.fullmatch(r'^[A-Za-z][\S]{3}[0-9][\S]{4}(.in.uhde.org)',i)
    # print(matchreg.group())
    try:
        if matchreg.group()==i:
            print(matchreg.group())
    except:
        print('error')







