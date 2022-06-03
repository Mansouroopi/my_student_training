from asyncio.log import logger
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Employee:
    """A sample employee class"""

    num_of_employee = 0
    raise_amt = 1.04


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employee += 1

        logger.info('Created Employee: {} - {} with pay {}'.format(self.fullname, self.email, self.pay))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @property
    def email(self):
        """employee email attribute"""
        return "{}.{}@mail.com".format(self.first, self.last)

    @property
    def fullname(self):
        """employee email attribute"""
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, fullname):
        """set employee fullname attribute"""
        print('Setting first and last')
        self.first, self.last = fullname.split(' ')

    @fullname.deleter
    def fullname(self):
        """delete employee email attribute"""
        print('Delete Name')
        self.first = None
        self.last = None

    @staticmethod
    def is_workdays(day):
        if day.weekday() ==5 or day.weekday() == 6:
            return False
        return True


emp1_string = "Maizatul-Zainuddin-120000"
emp1 = Employee('mansour', 'hassani', 1800000)
emp2 = Employee('sumayyah', 'mansour', 300000)
emp3 = Employee('shafiih', 'mansour', 250000)
emp4 = Employee.from_string(emp1_string)

# test static method
import datetime
my_date = datetime.date(2022, 5, 30)
print(Employee.is_workdays(my_date))

# write a function to add two number
def add(a, b):
    pass