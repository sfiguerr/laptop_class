#Sydnie Figuerrews
#Assignment 10.1: Your Own Class

#creates a laptop as a class
class Laptop:

    #init function to initialize variables within the class
    def __init__(self,battery,status):
        #checks if battery level is between 0 and 100
        if battery < 0:
            print("Laptop cannot have negative battery.")
            #raises an error if input is invalid
            raise ValueError
        if battery > 100:
            print("Laptop cannot be charged over 100%")
            raise ValueError
        else:
            self._battery = battery
        self._status = status
        #sets time as zero
        self._time = 0

    #function to set the battery
    def set_battery(self,battery):
        if battery < 0:
            print("Laptop cannot have negative battery.")
            raise ValueError
        else:
            self._battery = battery

    #function to get battery input
    def get_battery(self):
        return self._battery

    #function to calculate charging time
    #laptop charges half as fast if it is on
    def get_chargingtime(self):
        #checks that user input is either "on" or "off"
        if self._status == "on":
            self._time = (100 - self._battery) * 2
            return self._time
        elif self._status == "off":
            self._time = 100 - self._battery
            return self._time
        else:
            print("Invalid laptop status.")
            #raises value error if status input is invalid 
            raise ValueError
            
    #magic method to organize data within a string
    def __str__(self):
        return(f"Laptop is {self._battery}% charged and is {self._status}. Will be fully charged in {self._time} min.")

#main function that prompts user input
def main():
    battery = int(input("How much battery does your laptop have? "))
    status = str(input("Is your laptop on or off? "))
    #calls the class
    sample_laptop = Laptop(battery,status)
    #calls function to change tinme from zero
    sample_laptop.get_chargingtime()
    #prints string of information
    print(sample_laptop)

#runs main function
if __name__ == "__main__":
    main()
