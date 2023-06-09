#first i import the things that i need flask, request, json, dbhelpers
from flask import Flask, request
import json
import dbhelpers
#i set app = to the Flask(__name__)
app = Flask(__name__)
#i make the check_endpoint_info to check for errors
def check_endpoint_info(sent_data, expected_data):
    for data in expected_data:
        if(sent_data.get(data) == None):
            return f"The {data} paramter is required!"
#the first get is the all item get, this is done by a procedure in the data base called get_all_items i call upon that   
@app.get("/api/item")
def get_item():
    results = dbhelpers.run_procedures('CALL get_all_items()')
    if(type(results) == list):
        item_json = json.dumps(results, defualt=str)
        return item_json
    else:
        return "sorry, something went wrong"

#the first post will insert a new tiem based off what is given to it. i will do a valid check and a results if else that runs a procedure in the data base called select_item
@app.post("/api/item")
def post_item():
    valid_check = check_endpoint_info(request.json, ['name', 'description', 'price'])
    if(type(valid_check) == str):
        return valid_check
    results = dbhelpers.run_procedures('CALL select_item(?,?,?)', [request.json.get("name"), request.json.get("description"), request.json.get("price")])
    if(type(results) == list):
        return json.dump(results, default=str)
    else:
        return "sorry, something went wrong"
#the first patch request will update an item price based off of its id i have a endpoint check. it calls upon the update_all_items    
@app.patch("/api/client")
def client_patch():
    error = check_endpoint_info(request.json, ["price" , "id"])
    if(error != None):
        return error
    results = dbhelpers.run_procedure("call update_all_items(?,?)" , [request.json.get("price"), request.json.get("id")])
    if(type(results) == list):
        return json.dump(results, default=str)
    else:
        return "sorry, something went wrong"
#the first delete has the endpoint check it calls upon delete_item it needs an id 
@app.delete("/api/client")
def delete_client():
    error = check_endpoint_info(request.json, ["id"])
    if(error != None):
        return error
    results = dbhelpers.run_procedures("CALL delete_item(?)" ,[request.json.get("id")])
    if(type(results) == list):
        return json.dump(results, default=str)
    else:
        return "sorry, something went wrong"
# the second get will rend back an employees information and it requires an id aswell
@app.get("/api/employee")
def get_employee():
    valid_check = check_endpoint_info(request.args, ['id'])
    if(type(valid_check) == str):
        return valid_check
    results = dbhelpers.run_procedures('CALL insert_employee()')
    if(type(results) == list):
        item_json = json.dumps(results, defualt=str)
        return item_json
    else:
        return "sorry, something went wrong"

#the second post requires the name position and hourly_wage it triggers the get_employee_by_id and it also has a valid check
@app.post("/api/employee")
def post_employee():
    valid_check = check_endpoint_info(request.json, ['name', 'position', 'hourly_wage'])
    if(type(valid_check) == str):
        return valid_check
    results = dbhelpers.run_procedures('CALL get_employee_by_id(?,?,?)', [request.json.get("name"), request.json.get("position"), request.json.get("hourly_wage")])
    if(type(results) == list):
        return json.dump(results, default=str)
    else:
        return "sorry, something went wrong"
#the second patch has its valid check it requires the name and hourly wage and it will trigger the update_hourly_wage
@app.patch("/api/employee")
def patch_employee():
    error = dbhelpers.check_endpoint_info(request.json, ["name" , "hourly_wage"])
    if(error != None):
        return error
    results = dbhelpers.run_procedure("call update_hourly_wage(?,?)" , [request.json.get("name"), request.json.get("hourly_wage")])
    if(type(results) == list):
        return json.dump(results, default=str)
    else:
        return "sorry, something went wrong"
#the second delete has its endpoint check and it requires an id that will trigger the delete_employee in the sql
@app.delete("/api/employee")
def delete_employee():
    error = check_endpoint_info(request.json, ["id"])
    if(error != None):
        return error
    results = dbhelpers.run_procedures("CALL delete_employee(?)" ,[request.json.get("id")])
    if(type(results) == list):
        return json.dump(results, default=str)
    else:
        return "sorry, something went wrong"
#last but not least there is the app.run
app.run(debug=True)