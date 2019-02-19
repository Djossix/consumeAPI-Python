import urllib.request
import json

class GetEmployees:
    def getEmployees(self):
        newUrl = "http://localhost:8080/UserManagement/rest/UserService/getuser"

        with urllib.request.urlopen(newUrl) as response:
            data = json.loads(response.read())
            for user in data:
                print(f'Employee-number: {user["name"]}\nName: {data["name"]}\nJob title: {data["profession"]}')

        return
