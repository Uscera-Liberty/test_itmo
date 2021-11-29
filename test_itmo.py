class PhoneBook:
    def __init__(self, name, contactNumber , note):
        self.name = name
        self.contactNumber = contactNumber
        self.note = note

    def outputdata(self):
        print('I am', self.name , "My number is :", self.contactNumber , "Note :", self.note)

result = PhoneBook("Julia" , "891526354758" ,"note")
result.outputdata()