#import needed modules 
import requests #liabry for GET and POST API calls
import os       #libary for OS intractions. used to clear terminal 
import pprint   #libary used to make JSON display easer to read
import json     #liabry used for intracting with json objects 

#post funciton 
def pushFun():
    def getMenuFun():
        print('MENU', '\n1.Enter Another Value','\n2. Return to Menu','\n3. Exit')
        userInputFun()
    def userInputFun():
        userinput = int(input('Please make a selection: '))
        if(userinput == 1 or userinput == 2 or userinput == 3):
            if(userinput == 1):
                if(os.name == 'nt'):
                    os.system('cls')
                else:
                    os.system('clear')
                pushFun()
            elif(userinput == 2):
                if(os.name == 'nt'):
                    os.system('cls')
                else:
                    os.system('clear')
                main()
            elif(userinput == 3):
                exitFun()
    print('Enter the key and value below.')
    #headervalue = {"Authorization": "Token"}
    url = 'https://api.github.com/users/zachstac'
    jsonKey = str(input('Please enter the JSON key: '))
    jsonValue = str(input('Please enter the JSON value: '))
    jsonData ={jsonKey : jsonValue}
    response = requests.post(url, json=jsonData)
    print(response)
    getMenuFun()

#get function 
def getFun():
    #displays the get menu
    def getMenuFun():
        print('========MENU========', '\n1.Refresh','\n2.Return to Menu','\n3.Exit')
        userInputFun()

    #checks the menu input
    def userInputFun():
        userinput = int(input('Please make a selection: '))
        if(userinput == 1 or userinput == 2 or userinput == 3):
            if(userinput == 1):
                if(os.name == 'nt'):
                    os.system('cls')
                else:
                    os.system('clear')
                getFun()
            elif(userinput == 2):
                if(os.name == 'nt'):
                    os.system('cls')
                else:
                    os.system('clear')
                main()
            elif(userinput == 3):
                exitFun() 
    #headervalue = {"Authorization": "Token"}
    url = 'https://api.github.com/users/zachstac'
    response = requests.get(url)
    repcode = response
    sid=response.json() 
    print('Response Code: ',repcode)
    pprint.pprint(response.json())

    responsestr = str(response.text)
    jsonfont = json.loads(responsestr)
    
    getMenuFun()

    #jsonDict = json.loads(sid)
    #print(jsonDict)


#main call. fucntion used for the use of user input and menu disply.
def main():

    #displays menu
    def menuFun():
        print('========MENU========', '\n1.Pull API Data','\n2.Make a PUSH Request', '\n3.Exit')
        userInputFun()

    #checks user input
    def userInputFun():
        userinput = int(input('Please make a selection: '))
        if(userinput == 1 or userinput == 2 or userinput == 3):
            if(userinput == 1):
                if(os.name == 'nt'):
                    os.system('cls')
                else:
                    os.system('clear')
                getFun()
            elif(userinput == 2):
                if(os.name == 'nt'):
                    os.system('cls')
                else:
                    os.system('clear')
                pushFun()
            elif(userinput == 3):
                exitFun()
        else:
            print('Please make a valid selection.')
            userInputFun()     
    menuFun()

#exits terminal window 
def exitFun():
    exit()

main()
