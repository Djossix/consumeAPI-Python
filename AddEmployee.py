import urllib.request


class AddEmployee:
    def addNewEmployee(empNr, name, profession):
        newUrl = f"http://localhost:8080/UserManagement/rest/UserService/adduser{empNr}/{name}/{profession}"

        with urllib.request.urlopen(newUrl) as response:
            data = response.read()

        return data
