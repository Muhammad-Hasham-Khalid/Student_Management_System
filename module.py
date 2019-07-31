import json

def menu():
    print("\t\t\t\t      ___________________________")
    print("\t\t\t\t     |   |                       |")
    print("\t\t\t\t     | 1 | Add a Student         |")
    print("\t\t\t\t     | 2 | Delete a Student      |")
    print("\t\t\t\t     | 3 | Update data           |")
    print("\t\t\t\t     | 4 | View data             |")
    print("\t\t\t\t     | 5 | Exit                  |")
    print("\t\t\t\t     |___|_______________________|")

def choices(choice):
    if choice == 1:
        add()
    elif choice == 2:
        delete()
        pass
    elif choice == 3:
        update()
    elif choice == 4:
        view()
        pass

def add():
    name = input("Enter your name : ").lower()
    try:
        for char in name:
            if (char>="a" and char<="z"):
                continue
            else:
                raise Exception("Invalid Input")
    except Exception as e:
        print(e)
    else:
        fatherName = input("Enter your Father's name : ").lower()
        try:
            for char in fatherName:
                if (char>="a" and char<="z"):
                    continue
                else:
                    raise Exception("Invalid Input")
        except Exception as e:
            print(e)
        else:
            try:
                Class = int(input("In which class do you want to study : "))
                if Class<1 or Class>10:
                    raise Exception("Invalid input")
            except Exception as e:
                print(e)
            else:
                try:
                    Class = str(Class)
                    roll = int(input("Enter your roll number : "))
                    if roll<0 or roll>100:
                        raise Exception("Invalid Input")
                except Exception as e:
                    print(e)
                else:
                    subjects = []
                    print("Enter subjects you want to study : ")
                    try:
                        for loop in range(5):
                            subject = input().lower()
                            for char in subject:
                                if (char>="a" and char<="z"):
                                    continue
                                else:
                                    raise Exception("Invalid Input")
                            subjects.append(subject[:3])
                    except Exception as e:
                        print(e)
                    else:
                        addToFile(name,fatherName,Class,roll,subjects)
                        

def addToFile(name,fatherName,Class,roll,subjects):
    studentData = {
        "name" : name,
        "fatherName" : fatherName,
        "roll" : roll,
        "subjects" : subjects,
    }
    classData = list()
    try:
        try:
            with open("data.json","r") as f:
                dataFromJson = json.load(f)
        except Exception:
            dataFromJson = {}
        finally:
            for k in dataFromJson.keys():
                if k == Class:
                    classData = dataFromJson[k]
                    break
            if len(classData)!=0:
                for each in classData:
                    if each["roll"] == roll:
                            raise Exception("Roll number cannot be repeated")
            if len(classData)!=0:
                dataFromJson[Class].append(studentData)
            else:
                dataFromJson[Class] = [studentData]
            with open("data.json", "w") as f:
                json.dump(dataFromJson,f)
    except Exception as e:
        print(e)
    else:
        print(" _________________________")
        print("|                         |")
        print("| Data Successfully Added |")
        print("|_________________________|")

def view():
    try:
        classData = []
        Class = int(input("Enter which class data you want to view : "))
        if Class>10 or Class<1:
            raise Exception("Invalid Input")
    except Exception as e:
        print(e)
    else:
        Class = str(Class)
        try:
            with open("data.json","r") as f:
                dataFromJson = json.load(f)
        except Exception:
            dataFromJson = {}
        finally:
            for k in dataFromJson.keys():
                if k == Class:
                    classData = dataFromJson[k]
            if len(classData)!=0:
                print(" _________________________\n")
                print("     Class   : "+Class)
                print(" _________________________")
                print(" ___________________________________________________________________________________________")
                print("|    |          |                 |                                                         |")
                print("|Roll|   Name   |  Father's Name  |                        Subjects                         |")
                print("|____|__________|_________________|_________________________________________________________|")
                for each in classData:
                    print("  {0}    {1}       {2}                  {3}".format(each["roll"],each["name"].title(),each["fatherName"].title(),each["subjects"]))
            else:
                print(" _________________________\n")
                print("     Class   : "+Class)
                print(" _________________________\n")
                print("No Students added yet !")
        
            print("\n")
            
            
def update():
    try:
        Class = int(input("In which class do you study : "))
        if Class<1 or Class>10:
            raise Exception("Invalid input")
    except Exception as e:
        print(e)
    else:
        try:
            Class = str(Class)
            roll = int(input("Enter your roll number : "))
            if roll<0 or roll>100:
                raise Exception("Invalid Input")
        except Exception as e:
            print(e)
        else:
            try:
                classData = []
                with open("data.json","r") as f:
                    dataFromJson = json.load(f)
            except Exception:
                dataFromJson = {}
                print("No data present yet !")
                return 0
            else:
                for k in dataFromJson.keys():
                    if k == Class:
                        classData = dataFromJson[k]
                if len(classData)==0:
                    print("No data present yet !")
                    return 0
                else:
                    for each in classData:
                        if each["roll"] == roll:
                            index = classData.index(each)
                            dataFromJson[k][index]["name"] = input("Enter your updated name : ").lower()
                            try:
                                for char in dataFromJson[k][index]["name"]:
                                    if (char>="a" and char<="z"):
                                        continue
                                    else:
                                        raise Exception("Invalid Input")
                            except Exception as e:
                                print(e)
                            else:
                                dataFromJson[k][index]["fatherName"] = input("Enter your Father's name : ").lower()
                                try:
                                    for char in dataFromJson[k][index]["fatherName"]:
                                        if (char>="a" and char<="z"):
                                            continue
                                        else:
                                            raise Exception("Invalid Input")
                                except Exception as e:
                                    print(e)
                                else:
                                    print("Enter subjects you want to study : ")
                                    try:
                                        for loop in range(5):
                                            subject = input().lower()
                                            for char in subject:
                                                if (char>="a" and char<="z"):
                                                    continue
                                                else:
                                                    raise Exception("Invalid Input")
                                            subject = subject[:3]
                                            dataFromJson[k][index]["subjects"][loop] = subject 
                                    except Exception as e:
                                        print(e)
                                    else:
                                        with open("data.json" , "w") as f:
                                            json.dump(dataFromJson,f)
                                            print(" ___________________________")
                                            print("|                           |")
                                            print("| Data Successfully Updated |")
                                            print("|___________________________|")
                                            
                                            
def delete():
    try:
        Class = int(input("In which class do you study : "))
        if Class<1 or Class>10:
            raise Exception("Invalid input")
    except Exception as e:
        print(e)
    else:
        try:
            Class = str(Class)
            roll = int(input("Enter your roll number : "))
            if roll<0 or roll>100:
                raise Exception("Invalid Input")
        except Exception as e:
            print(e)
        else:
            try:
                classData = []
                with open("data.json","r") as f:
                    dataFromJson = json.load(f)
            except Exception:
                dataFromJson = {}
                print("No data present yet !")
                return 0
            else:
                for k in dataFromJson.keys():
                    if k == Class:
                        classData = dataFromJson[k]
                if len(classData)==0:
                    print("No data present yet !")
                    return 0
                else:
                    for each in classData:
                        if each["roll"] == roll:
                            dataFromJson[k].remove(each)
                            with open("data.json" , "w") as f:
                                json.dump(dataFromJson,f)
                                print(" ___________________________")
                                print("|                           |")
                                print("| Data Successfully Removed |")
                                print("|___________________________|")