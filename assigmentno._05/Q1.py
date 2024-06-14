class company:

    companyname=""

    def __init__(self,companyname):
        self.companyname = companyname

class  Department(company):

    dname=""

    def __init__(self,companyname,dname):
        super().__init__(companyname)
        self.dname = dname


class Developer(Department):

    language=""

    def __init__(self,companyname,dname,language):
        super().__init__(companyname,dname)
        self.language = language

    def displaydeveloper(self):
        print("********DEVELOPER----DETAILS*********")
        print("Company Name:-",self.companyname)
        print("Department Name:-", self.dname)
        print("Language known:-", self.language)
        print("______________________________________")

class tester(Department):

    nooftestcases=""

    def __init__(self,companyname,dname,nooftestcases):
        super().__init__(companyname,dname)
        self.nooftestcases = nooftestcases

    def displaytester(self):
        print("********TESTER----DETAILS*********")
        print("Company Name:-",self.companyname)
        print("Department Name:-", self.dname)
        print("no.oftester:-", self.nooftestcases)
        print("______________________________________")

class managment(Department):

    typeofmanagment=""

    def __init__(self,companyname,dname,typeofmanagement):
        super().__init__(companyname,dname)
        self.typeofmanagment = typeofmanagement

class manager(managment):

    noofprojects=""

    def __init__(self,companyname,dname,typeofmanement,noofprojects):
        super().__init__(companyname,dname,typeofmanement)
        self.noofprojects = noofprojects

    def displaymanager(self):
        print("********Maneger----DETAILS*********")
        print("Company Name:-", self.companyname)
        print("Department Name:-", self.dname)
        print("Type of managment:-", self.typeofmanagment)
        print("No. of projects:-", self.noofprojects)
        print("______________________________________")

class hr(managment):

    noofincentives:''

    def __init__(self,companyname,dname,typeofmanagement,noofincentives):
        super().__init__(companyname,dname,typeofmanagement)
        self.noofincentives = noofincentives

    def displayhr(self):
        print("********Human resource----DETAILS*********")
        print("Company Name:-", self.companyname)
        print("Department Name:-", self.dname)
        print("Type of managment:-", self.typeofmanagment)
        print("No. of incentives:-", self.noofincentives)
        print("______________________________________")

c=input('enter the company name')
dep=input('enter the dep nmame')
lan=input('enter the lang')
test=int(input("enter the no of test cases"))
man=input("enter the management")
prj=int(input('enter the no. of project'))
inc=int(input("enter the incentives"))


ddd=Developer(c,dep,lan)
ddd.displaydeveloper()

tdd=tester(c,dep,test)
tdd.displaytester()

mdd=manager(c,dep,man,prj)
mdd.displaymanager()

hrdd=hr(c,dep,man,inc)
hrdd.displayhr()