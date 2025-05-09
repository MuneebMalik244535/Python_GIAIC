class Employee:
    def __init__(self):
        self.name = "Ahsan"
        self._salary = 50000
        self.__ssn = "123-45-6789"

e = Employee()
print(e.name)       # Public
print(e._salary)    # Protected (accessible but should be treated as protected)
# print(e.__ssn)    # Private (will cause error)
print(e._Employee__ssn)  # Accessing private via name mangling
