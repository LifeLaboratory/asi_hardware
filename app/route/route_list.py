from app.route.route_auth import Auth
from app.route.route_profile import Profile
from app.route.route_register import Register
from app.route.route_info_user import InfoUser
from app.route.route_lunch import Lunch, LunchAll
from app.route.route_event import Event, EventAll, EventAdd

ROUTES = {
    Register: '/register',
    Auth: '/auth',
    Profile: '/user/<int:user_id>',
   # InfoUser: '/info/<int:id_nom>/<string:id_user>',
    Lunch: '/lunch',
    LunchAll: '/lunch/all',
    Event: '/event',
    EventAll: '/event/all',
    EventAdd: '/event/add',
    # EventActive: '/event/active',
}
