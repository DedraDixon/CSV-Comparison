import csv
from csv import writer
import pandas as pd
import datetime

def CreateCompExcel(numtry, ext, df1):

    # Uses current date and time so that the output file name can be dynamically named and easily identitifiable
    current_time = str(datetime.datetime.now())
    if ext == "1":
        ext = ".csv"
        filename= "comparison_"+ current_time + ext
        df1.to_csv(filename, index=False, header=["id", "attribute", "old value", "new value", "changes made"])
        print(f"The comparison csv file has been created as {filename}")
        
    elif ext == "2":
        ext = ".xlsx"
        filename= "comparison_"+ current_time + ext
        df1.to_excel(filename, index=False, header=["id", "attribute", "old value", "new value", "changes made"])
        print(f"The comparison excel file has been created as {filename}")

    elif ext == "3":
        ext = ".csv"
        filename= "comparison_"+ current_time + ext
        df1.to_csv(filename, index = False, header=["id", "attribute", "old value", "new value", "changes made"])
        print(f"The comparison csv file has been created as {filename}")
        ext = ".xlsx"
        filename= "comparison_"+ current_time + ext
        df1.to_excel(filename, index=False, header=["id", "attribute", "old value", "new value", "changes made"])
        print(f"The comparison excel file has been created as {filename}")
    else:
        try:
            raise Exception("The value entered must be 1, 2, or 3")
        except:
            if numtry == 0:
                print('''
                You must ensure that both of files you have provided are CSV files. Try making this change and running the program again.
                ''')
                return
            else:
                tryagain = input("INVALID - Please enter either 1, 2, or 3:")
                CreateCompExcel(numtry-1, tryagain, df1)


    

def CompareExcel(numtry, df1, df2):
    compare = input('''
    Type 'all' if you would like to compare all the attributes in both excel files. 
    If you would like to only compare select attributes enter them instead. Note that this field is case sensitive: 
    ''')

    if compare.lower() == "all":
        compare = list(df1)
    elif "," in compare:
        compare = compare.replace(" ", "")
        compare = compare.split(",")
    elif " " in compare:
        compare = compare.split(" ")
    else:
        ls =[]
        ls.append(str(compare))
        compare = ls

    changeRows = []

    for i, row1 in df1.iterrows():
        for j, row2 in df2.iterrows():
            if row1['id'] == row2['id']:
                for x in compare:
                    if x == id:
                        continue
                    if str(row1[x]).strip() != str(row2[x]).strip():
                        change = f"id:{row1['id']} value for {x} has changed from {row1[x]} to {row2[x]}"
                        changeRows.append([row1['id'], x, row1[x], row2[x], change])
        
    if len(changeRows) == 1:
        print("There was no change between the first and second csv file on the variables entered.")
        return

    
    df = pd.DataFrame(changeRows)
    sel = input('''
    Enter 1 if you would like the output to be a csv file
    Enter 2 if you would like it to be an excel file
    Enter 3 if you would both formats: 
    ''')
    filecreate = CreateCompExcel(2, sel, df)
                    
                        
                    


def runProg(num):
    f1 = input("Enter the path or the name of the first file followed by the enter button: ")
    f2 = input("Enter the path or the name of the second file followed by the enter button: ")
    d1 = ""
    d2 = ""
    try:
        d1 = pd.read_csv(f1)
        d2 = pd.read_csv(f2)
    except UnicodeDecodeError:
        num -= 1
        if num == 0:
            print('''
            You must ensure that both of files you have provided are CSV files. Try making this change and running the program again.
            ''')
            return
        else: 
            print(f'''
            Error - You have {num} more attempt(s) to correct the error below. After that, you must rerun the program.
                
            The files you provide must be csv files.
            ''')
            runProg(num)
    
    try:
        CompareExcel(3, d1, d2)
    except KeyError:
        num -= 1
        if num == 0:
            print('''
            You must ensure that both of files you have provided include the attribute you are trying to compare them on.
            This means that the attibute you are trying to compare must exist in the first row of the CSV file exactly the way that
            you type it. Try making these changes and running the program again.
            ''')
            return
        else:
            print(f'''
            Error - You have {num} more attempt(s) to correct the error below. After that, you must rerun the program.
            
            The variables you entered do not exist in one or more of the files you provided, so the program is unable to make a comparison. 
            Please either edit the files so that the variable exists in both files or choose different attributes to compare the files on.
            ''')
            runProg(num)
    except FileNotFoundError:
        num -= 1
        if num == 0:
            print('''
            You must ensure that both of CSV files you are trying access exist by the name/path you are providing. Ensure you have included 
            the extension in the name provided as well. To avoid providing a path, put the two files inside the same folder as the project.
            Try making these changes and running the program again.
            ''')
            return
        else:
            print(f'''
            Error - You have {num} more attempt(s) to correct the error below. After that, you must rerun the program.
            
            One or more of the file names/paths you provided do not exist. Please try again.
            ''')
            runProg(num)


if __name__=="__main__":
    print('''
    This is a CSV file comparison program. 
    Please ensure that the two CSV files you would like to compare are in the same folder as this project 
    or that you are able to get the path to the two files. You must also ensure that both of files you have provided 
    include the attribute you are trying to compare them on. File names must also include the ".csv" extension.
    ''')
    runProg(3) # Increase or decrease this number to limit the number of recursive calls allowed for the user to correct their errors