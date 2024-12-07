import hashlib
import common_functions

users = r"Tables\users.json"

#Internal functions DONT USE THIS 
def __find_by_nickname(data, nickname):
    for user in data:
        if user["nickname"] == nickname:
            return user
        
    return
    
def __maximum_id_json(data):
    maximum = 0
    for user in data:
        if user["id"] > maximum:
            maximum = user["id"]

    return maximum + 1

def __maximum_id_csv(data):
    maximum = 0
    for user in data:
        if int(user[0]) > maximum:
            maximum = int(user[0])

    return maximum + 1


def __hash_password(password):
    password_bytes = password.encode('utf-8')
    
    hash_object = hashlib.sha256()
    
    hash_object.update(password_bytes)
    
    hashed_password = hash_object.hexdigest()
    
    return hashed_password


def __check_if_instructor(instructor_code):
    return instructor_code == "aua_bocavik"

#External Functions
def modify(nickname, firstname, lastname, password):
    data = common_functions.__read_file_json(users)
    user = __find_by_nickname(data, nickname)

    if user:
        data.remove(user)
        user["firstname"] = user["firstname"] if user["firstname"] == firstname else firstname
        user["lastname"] = user["lastname"] if user["lastname"] == lastname else lastname

        new_password = __hash_password(password)
        user["password"] = user["password"] if user["password"] == new_password else new_password

        data.append(user)
        common_functions.__add_json(data, users)


def register(nickname, firstname, lastname, password, status = "student", instructor_code = None):
    data = common_functions.__read_file_json(users)
    if __find_by_nickname(data, nickname):
        return False
    
    if instructor_code and not __check_if_instructor(instructor_code):
        return False
    
    password = __hash_password(password)
    new_user = {
        "id":__maximum_id_json(data), 
        "nickname":nickname, 
        "firstname":firstname, 
        "lastname":lastname, 
        "status":status, 
        "grades":[],
        "questions":[], 
        "password":password,
        }

    
    data.append(new_user)
    common_functions.__add_json(data, users)

    return True


def login(nickname, password):
    data = common_functions.__read_file_json(users)
    current_user = __find_by_nickname(data, nickname)
    if not current_user:
        return False
    
    current_password = __hash_password(password)
    original_password = current_user["password"] 

    return current_password == original_password


def remove(nickname):
    data = common_functions.__read_file_json(users)
    current_user = __find_by_nickname(data, nickname)

    if not current_user:
        return False
    
    data.remove(current_user)

    common_functions.__add_json(data, users)

    return True

# Example usages:
#register("lav_txa777", "Grno","Petrsyan","lavtxaemes")
#login("lav_txa777","lavtxaemes")
#remove("lav_txa777")
#modify("AceCoder", "Aced", "Coder", "AceCoder123")