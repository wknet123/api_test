import pytest
import harbor_http_request


@pytest.fixture(scope = "function")
def before(request):
    print("this is the before function")
    admin_response = harbor_http_request.login("admin", "Harbor12345")
    userA_response = harbor_http_request.login("kunw", "Abc1234")

    admin_sessionID = admin_response["response_cookies"]["beegosessionID"]
    userA_sessionID = userA_response["response_cookies"]["beegosessionID"]
    sessionId = dict(admin_sessionID=admin_sessionID, userA_sessionID=userA_sessionID)
    return sessionId
