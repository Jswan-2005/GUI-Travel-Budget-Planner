## Author: Jonathan Swan
## Date Created 12/04/2024
##Date Last Changed 25/04/2024
'''This a GUI program allowing users to plan overseas or domestic travel. The program allows them to enter a maximum budget and then subsuequent costs for travel, accomoodation
activites and other costs. Additonally, the program includes a currency converter program which converts USD to the local currency of supported countries local currencies'''
##Input: CountryDataDictionary.txt, Output: None
from tkinter import *
def readFile(): #This functions read data from a text file and converts it into a dictionary including country, currency value reltive to the US dollar and currency sign
    COUNTRY_INFO_DICTIONARY = {}

    filename = 'CountryDataDictionary.txt'

    infile = open(filename, 'r')

    for line in infile:
        country, value, sign = line.strip().split(',')

        COUNTRY_INFO_DICTIONARY[country] = {'value': value, 'sign': sign}
    return COUNTRY_INFO_DICTIONARY


COUNTRY_INFO_DICTIONARY = readFile() #This creates a dictionary variable as the readFile() function is called and assigned to variable COUNTRY_INFO_DICTIONARY

def insertCosts(): #This function inserts a value of zero into all entry widgets. This means no valueErrors at the start of the program.
    entTravel.insert(0, '0')
    entFoodAndDrink.insert(0, '0')
    entAccommodation.insert(0, '0')
    entActivities.insert(0, '0')
    entOther.insert(0, '0')
    entMaxBudget.insert(0, '0')


def insertCountries(): #This inserts all country names from the country info dictionary into the listbox
    countries = COUNTRY_INFO_DICTIONARY.keys()
    for country in countries:
        lstCountries.insert(END, country)

def updateBudget(): #This function is called when the calculate button is pressed. It updates the current entries into the costs entry widgets and compares them to the set max budget
    travelCost = float(entTravel.get())

    accommodationCost = float(entAccommodation.get())

    foodAndDrinkCost = float(entFoodAndDrink.get())

    activitiesCost = float(entActivities.get())

    otherCost = float(entOther.get())

    maxBudgetValue = float(entMaxBudget.get())

    userBudget = travelCost + accommodationCost + activitiesCost + otherCost + foodAndDrinkCost

    if userBudget > maxBudgetValue:
            currentBudgetString.set(f'Your are ${userBudget - maxBudgetValue} over the max budget')
    else:
            currentBudgetString.set(f'${str(userBudget)}')


def listboxEvent(event): #This function binds two functions to when an item in the listbox is selected
    selectedCountry(event)
    Conversion(event)

def Conversion(event): #This function converts the inputted amount in USD from the user to the local currency of the selected country
    selectedListItem = lstCountries.curselection()

    countryList = list(COUNTRY_INFO_DICTIONARY.keys())

    if selectedListItem:
        selectedIndex = selectedListItem[0]

        countryName = countryList[selectedIndex]

        currencyInfo = COUNTRY_INFO_DICTIONARY[countryName]

        if currencyInfo:
            amountUSD = float(entCurrencyConversion.get())

            convertedAmount = amountUSD * float(currencyInfo['value'])

            sign = COUNTRY_INFO_DICTIONARY[countryName]['sign']

            conversion.set(f'{convertedAmount} {sign}')

def selectedCountry(event): #This functions inserts a string into the currentCountry variable whenever a country is selected from the listbox
    for i in lstCountries.curselection():
        currentCountry.set(f'The current budget for {lstCountries.get(i)} trip is')


def main():
    # These two functions must be called at the start of the program
    insertCountries()  # Allows all country names to be inserted into the listbox
    insertCosts()  # Allows values to be entered into the entry widgets, preventing value errors
    window.mainloop()


#GUI Code
window = Tk()
window.title('Travel Budget Planner')

#Welcome label
lblWelcome = Label(window, text = 'Travel Budget Planner', font = 26, bg = 'lightgrey', highlightbackground="black", highlightthickness=4)
lblWelcome.grid(row = 0, column = 0, pady = 20)

#Country listbox
lstCountries = Listbox(window, width = 20, height = 10, font = 26, highlightbackground="black", highlightthickness=1)
lstCountries.grid(row = 1, column = 0, rowspan = 5, padx = 20)

#Scrollbar
yscroll = Scrollbar(window, command = lstCountries.yview, orient=VERTICAL)
lstCountries.configure(yscrollcommand = yscroll.set)
yscroll.grid(row = 1, column = 0, rowspan = 5, sticky = 'nse')

#Travel costs label and entry widget
lblTravel = Label(window, text = 'Enter Travel Cost: ', font = 26, bg = 'lightgrey', highlightbackground="black", highlightthickness=2)
lblTravel.grid(row = 1, column = 1)

entTravel = Entry(window)
entTravel.grid(row = 1, column = 2, sticky = W)

#Accommodation costs label and entry widget
lblAccommodation = Label(window, text = 'Enter Accommodation Cost: ', font = 26, bg = 'lightgrey', highlightbackground="black", highlightthickness=2)
lblAccommodation.grid(row = 2, column = 1, padx = 25)

entAccommodation = Entry(window)
entAccommodation.grid(row = 2, column = 2, sticky = W)

#Food and drink costs label and entry widget
lblFoodAndDrink = Label(window, text = 'Enter Food and Drinks Cost: ', font = 26, bg = 'lightgrey', highlightbackground="black", highlightthickness=2)
lblFoodAndDrink.grid(row = 3, column = 1)

entFoodAndDrink = Entry(window)
entFoodAndDrink.grid(row = 3, column = 2, sticky = W)

#Activities costs label and entry widget
lblActivities = Label(window, text = 'Enter Activities Cost: ', font = 26, bg = 'lightgrey', highlightbackground="black", highlightthickness=2)
lblActivities.grid(row = 4, column = 1)

entActivities = Entry(window)
entActivities.grid(row = 4, column = 2, sticky = W)

#Other costs label and entry widget
lblOther = Label(window, text = 'Enter Other Expenses: ', font = 26, bg = 'lightgrey', highlightbackground="black", highlightthickness=2)
lblOther.grid(row = 5, column = 1, pady = 10    )

entOther = Entry(window)
entOther.grid(row = 5, column = 2, sticky = W)

#Max budget label and entry widget
lblMaxBudget = Label(window, text = 'Enter Max Budget: ', font = 26, bg = 'lightgrey', highlightbackground="black", highlightthickness=2)
lblMaxBudget.grid(row = 6, column = 0, pady = 10,)

entMaxBudget = Entry(window)
entMaxBudget.grid(row = 7, column = 0)

#Calculate button, which calculates the current budget based on user inputs
btnCalculate = Button(window, text = 'Calculate Total', command = updateBudget, width = 15, height = 2, bg = 'lightblue', highlightbackground="black", highlightthickness=2)
btnCalculate.grid(row = 8, column = 0, sticky = W, padx = 70, pady = 10)

#Insert Quit Button
btnQuit = Button(window, text = 'Quit', command = window.destroy, width = 10, height = 2, bg = 'lightblue', highlightbackground="black", highlightthickness=2)
btnQuit.grid(row = 9, column = 0, sticky = W, padx = 85, pady = 10)

#Output entry widget to insert a string of text including the selected country
currentCountry = StringVar()
entOutputCurrentCountry = Entry(window, textvariable = currentCountry, state = 'readonly', width = 50, bg = 'lightblue', font = 26)
entOutputCurrentCountry.grid(row = 7, column = 1, columnspan = 2)

#Output entry widget to insert the current budget when the calculate is pressed
currentBudgetString = StringVar()
entOutputCurrentBudget = Entry(window, width = 50, state = 'readonly', textvariable = currentBudgetString, font = 26, bg = 'lightblue')
entOutputCurrentBudget.grid(row = 8, column = 1, columnspan = 2)

#Currency conversion label and entry widget
lblCurrencyConversion1 = Label(window, text = 'USD Currency Converter \n Enter Amount in USD', font = 26, bg = 'lightgrey', highlightbackground="black", highlightthickness=2)
lblCurrencyConversion1.grid(row = 1, column = 3, padx = 100)

entCurrencyConversion = Entry(window)
entCurrencyConversion.grid(row = 2, column = 3)

lblCurrencyConversion2 = Label(window, text = 'Returned in Local Currency of \n Selected Currency', font = 26, bg = 'lightgrey', highlightbackground="black", highlightthickness=2)
lblCurrencyConversion2.grid(row = 3, column = 3, padx = 100)

#Output entry widget inserting teh converted amount
conversion = StringVar()
entOutputConvertedAmount = Entry(window, state = 'readonly', textvariable = conversion)
entOutputConvertedAmount.grid(row = 4, column = 3)
lstCountries.bind('<<ListboxSelect>>', listboxEvent)

main()
