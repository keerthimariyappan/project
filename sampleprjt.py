import json

def add_data():

        intern_id = input("Enter Intern Id :")
        intern_name = input("Enter Intern Name :")
        project = input("Enter Project :")
        dic = {
            "INTERN_ID :": intern_id,
            "INTERN_NAME :": intern_name,
            "PROJECT :": project
        }
        with open("interns.json", "r") as getdata:
            data = json.load(getdata)
            data[intern_id] = dic
            with open("interns.json", "w") as save:
                json.dump(data, save)
                print("Successfully Added")

def view_data():

    with open("interns.json", "r") as view:
        data = json.load(view)

        for i, m in data.items():
            for x, n in m.items():
                print(x, n)
            print("\n")
            print("Successfully Viewed")

def delete_data():
    intern_id = input("Enter Intern Id : ")

    with open("interns.json", "r") as getdata:
        data = json.load(getdata)

        if intern_id in data:
            data.pop(intern_id)

            with open("interns.json", "w") as delete:
                data1 = json.dump(data, delete)
            print("Successfully Deleted")

def update_data():
    intern_id = input("Enter Intern Id : ")

    with open("interns.json", "r") as getdata:
        data = json.load(getdata)

        if intern_id in data:
            intern_id = input("Enter Intern Id")
            intern_name = input("Enter Intern Name : ")
            project = input("Enter New Project : ")

            dic = {
                "INTERN_ID :": intern_id,
                "INTERN_NAME :": intern_name,
                "PROJECT :": project

            }

            data[intern_id] = dic
            with open("interns.json", "w") as update:
                json.dump(data, update)
                print("Successfully Updated")


def main():

    print("\n1.Add Data")
    print("\n2.View Data")
    print("\n3.Delete Data")
    print("\n4.Update Data")
    print("\n5.Exit")

    enter = int(input("Choose your Option : "))

    if enter == 1:
        add_data()
        main()
    elif enter == 2:
        view_data()
        main()
    elif enter == 3:
        delete_data()
        main()
    elif enter == 4:
        update_data()
        main()
    else:
        print("Invalid Entry")
        enter = int(input("Enter 1 to Continue : "))

main()





