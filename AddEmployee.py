import http.client


class AddEmployee:
    def addNewEmployee(empNr, name, profession):
        newUrl = f"http://localhost:8080/UserManagement/rest/UserService/adduser{empNr}/{name}/{profession}"

        con = http.client.HTTPConnection(newUrl)
        con.request("GET", "/")

        con.close()
        return
