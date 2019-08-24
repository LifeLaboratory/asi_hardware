WARNING = "Warning"
ERROR = "Error"
OK = "Ok"
SUCCESS = "Success"
ANSWER = "Answer"
SESSION = 'session'

DESCRIPTION = "description"
DATA = "data"
COMPANY = "Company"
LOGIN = "login"
PASSWORD = "password"
TYPE = "type"
QUERY = "query"
FIELD = "field"
ID_NAME = "id_nom"
ID_USER = "user_id"
ID_NOM = "id_nom"
ID_SALES = "id_sales"
CODE = "code"
CATEGORY = "category"
INTERVAL = "interval"
ID_USER_NOM = "id_user_nom"
EXPIRED_START = 'expired_start'
EXPIRED_END = 'expired_end'
NAME = "name"
SURNAME = "surname"
EMAIL = "email"
SEX = "sex"
CITY = "city"
EDUCATION = "educational"
LOGO_NAME = "logo_name"
LOGO = "logo"
UUID = "UUID"
PAGE = "page"
ID_NEWS = "id_news"
HEADER = "http_"

ERROR_EXECUTE_DATABASE = "Fatal error: execute database"
ERROR_CONNECT_DATABASE = "Error connect database"

STATUS_OK = 200
STATUS_PARSE_DATA = 102
STATUS_CONVERTER = 103
STATUS_CHECK_DATA = 104
STATUS_SQL_ERROR = 105
STATUS_AUTH_FAILED = 106

front_user_id = "User_Id"
front_event_id = "Event_Id"


base_user = {
    'firstName':None,
    'lastName':None,
    'last_name':None,
    'role':None,
    'birhDate':None,
    'company':None,
    'about':None,
    'photo':None,
    'city':None,
    'contacts':None
}

base_cors = {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }

status_to_name = {
    0: "pending" ,
    1: "approved" ,
    2: "declined" ,
    3: "finished"

}

name_to_status = {
    "pending":0,
    "approved":1,
    "declined":2,
    "finished":3
}

STATUS = "status"

TITTLE = 'title'
PLACE = 'place'
PHOTO = 'photo'
DATE = 'date'
CREATOR = 'creator'
MAX_PERSON = 'maxPerson'

PERSON_ID = 'personId'
