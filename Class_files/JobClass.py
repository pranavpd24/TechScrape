









class Job:
    def __init__(self, name="Something Went Wrong", location="Something Went Wrong", skills ="Something Went Wrong", pay = "Something Went Wrong", next = "Something Went Wrong", href = "Something Went Wrong", description = "Something Went Wrong"):
        self.name = name
        self.location = location
        self.skills = skills
        self.pay = pay
        self.next = next
        self.href = href
        self.description = description

    def DispInfoCorrectly(self):
        print()
        
        print('############################################')
        print()
        print("Job Name: "+ self.name)
        print("Location: "+self.location)
        # print("skills: "+self.skills)
        # print("Pay: "+self.pay)
        print('Description: '+ self.description)
        print()
        print("Link to Apply: "+self.href)
        print()
        print('#############################################')
        print()



    
    