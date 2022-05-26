class RaiseExp():
    def valid_age(self, num):
        #try:
        if(num < 18):
           raise ValueError("age is not valid")
        else: 
           print("valid age")
        
        #except ValueError as e:
            #print(e)                