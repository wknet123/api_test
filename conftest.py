import pytest
import harbor_http_request
import json
import time


def get_session_id(response):
    return response["response_cookies"]["beegosessionID"]


def get_value_from_response(response, key):
    r = json.loads(response["response_payload"])
    value = ""
    if len(r) > 0:
        value = r[0][key]
    return value


@pytest.fixture(scope="session")
def login_as_admin():
    return get_session_id(harbor_http_request.login("admin", "Harbor12345"))


@pytest.fixture(scope="session")
def login_as_user():
    return get_session_id(harbor_http_request.login("user1", "Abc1234"))


@pytest.fixture(scope="session")
def login_as_another_user():
    return get_session_id(harbor_http_request.login("user2", "Abc1234"))


@pytest.fixture(scope="function")
def query_str():
    return "targe"


@pytest.fixture(scope="function")
def project_name():
    return "myrepo1"

@pytest.fixture(scope="function")
def too_short_project_name():
    return "m"


@pytest.fixture(scope="function")
def too_long_project_name():
    return "A too long word for project name is not available to our program. 123456"


@pytest.fixture(scope="function", params=["myrepo1"])
def project_id(request, login_as_user):
    response = harbor_http_request.list_project(request.param, False, login_as_user)
    return get_value_from_response(response, "ProjectId")


@pytest.fixture(scope="function", params=["target1"])
def another_project_id(request, login_as_another_user):
    response = harbor_http_request.list_project(request.param, False, login_as_another_user)
    return get_value_from_response(response, "ProjectId")


@pytest.fixture(scope="function", params=["user1"])
def user_name(request):
    return request.param


@pytest.fixture(scope="function", params=["user2"])
def another_user_name(request):
    return request.param


@pytest.fixture(scope="function", params=["unknown"])
def inexistent_user_name(request):
    return request.param


@pytest.fixture(scope="function", params=[[3]])
def role_id(request):
    return request.param


@pytest.fixture(scope="function", params=[[2]])
def lower_privilege_role_id(request):
    return request.param


@pytest.fixture(scope="function", params=[[4]])
def update_role_id(request):
    return request.param


@pytest.fixture(scope="function", params=["user1"])
def user_id_by_name(request, login_as_admin):
    response = harbor_http_request.list_user(request.param, login_as_admin)
    return get_value_from_response(response, "UserId")


@pytest.fixture(scope="function", params=["user3"])
def temp_user_id_by_name(request, login_as_admin):
    response = harbor_http_request.list_user(request.param, login_as_admin)
    return get_value_from_response(response, "UserId")


@pytest.fixture(scope="function")
def user_of_project_member(project_id, another_user_name, login_as_user):
    response = harbor_http_request.get_member_of_project(project_id, another_user_name, login_as_user)
    return json.loads(response["response_payload"])[0]


@pytest.fixture(scope="function", params=["create"])
def log_filter_keywords(request):
    return request.param


@pytest.fixture(scope="function", params=["2016-02-26 00:00:00"])
def log_filter_start_timestamp(request):
    return int(time.mktime(time.strptime(request.param, "%Y-%m-%d %H:%M:%S")))


@pytest.fixture(scope="function", params=["2016-02-26 23:59:59"])
def log_filter_end_timestamp(request):
    return int(time.mktime(time.strptime(request.param, "%Y-%m-%d %H:%M:%S")))

