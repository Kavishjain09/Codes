#Class method

class Employee:

    company='Amazon'
    emp_id=3003

    def __init__(self):
        self.name='Pranay'
        self.address='UK'

    @classmethod
    def propertiesInfo(cls):
        print("Name of the company: ",cls.company)
        print("Employee ID: ",cls.emp_id)

e=Employee()

e.propertiesInfo()
Employee.propertiesInfo()
