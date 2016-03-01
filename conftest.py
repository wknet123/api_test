import pytest
import harbor_http_request
import json
import time
import subprocess
import os


def get_session_id(response):
    return response["response_cookies"]["beegosessionID"]


def get_value_from_response(response, key):
    r = json.loads(response["response_payload"])
    if len(r) > 0:
        return r[0][key]
    return ""


@pytest.fixture(scope="session", params=["admin"])
def admin_user_name(request):
    return request.param


@pytest.fixture(scope="session", params=["user1"])
def user_name(request):
    return request.param


@pytest.fixture(scope="session", params=["user2"])
def another_user_name(request):
    return request.param


@pytest.fixture(scope="function", params=["user0"])
def nonexists_user_name(request):
    return request.param


@pytest.fixture(scope="function", params=["user1@vmware.com"])
def email(request):
    return request.param


@pytest.fixture(scope="function", params=["user0@vmware.com"])
def nonexists_email(request):
    return request.param


@pytest.fixture(scope="session", params=["user1", "user2"])
def sign_up(request):
    return harbor_http_request.signup(request.param, "Abc1234", request.param + "@vmware.com", request.param, "no comments")


@pytest.fixture(scope="session")
def login_as_admin(admin_user_name):
    return get_session_id(harbor_http_request.login(admin_user_name, "Harbor12345"))


@pytest.fixture(scope="session")
def login_as_user(user_name):
    return get_session_id(harbor_http_request.login(user_name, "Abc1234"))


@pytest.fixture(scope="session")
def login_as_another_user(another_user_name):
    return get_session_id(harbor_http_request.login(another_user_name, "Abc1234"))


@pytest.fixture(scope="function")
def query_str():
    return "targe"


@pytest.fixture(scope="function")
def project_name():
    return "myrepo1"


@pytest.fixture(scope="function")
def another_project_name():
    return "target1"


@pytest.fixture(scope="function")
def too_short_project_name():
    return "m"


@pytest.fixture(scope="function")
def too_long_project_name():
    return "A too long word for project name is not available for our program. 123456"


@pytest.fixture(scope="session", params=["myrepo1", "target1"])
def create_project(request, login_as_user, login_as_another_user):
    if request.param == "myrepo1":
        return harbor_http_request.create_project(request.param, login_as_user)
    elif request.param == "target1":
        return harbor_http_request.create_project(request.param, login_as_another_user)


@pytest.fixture(scope="session", params=["myrepo1"])
def project_id(request, login_as_user):
    response = harbor_http_request.list_project(request.param, False, login_as_user)
    return get_value_from_response(response, "ProjectId")


@pytest.fixture(scope="session", params=["target1"])
def another_project_id(request, login_as_another_user):
    response = harbor_http_request.list_project(request.param, False, login_as_another_user)
    return get_value_from_response(response, "ProjectId")


@pytest.fixture(scope="function", params=["unknown"])
def nonexistent_user_name(request):
    return request.param


@pytest.fixture(scope="function", params=[[3]])
def role_id(request):
    return request.param


@pytest.fixture(scope="function", params=[[2]])
def higher_privilege_role_id(request):
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


def get_status(response):
    return response["status_code"]

SERVER_IP = os.getenv("SERVER_IP", "")

@pytest.fixture(scope="function", params=["docker login -u user1 -p Abc1234 -e user1@vmware.com " + SERVER_IP,
        "docker tag alpine " + SERVER_IP + "/myrepo1/alpine",
        "docker push " + SERVER_IP + "/myrepo1/alpine", "repo", "image"])
def repository_related(request, project_name, repository_name, image_tag, login_as_user):
    if request.param == "repo":
        assert get_status(harbor_http_request.list_tags(project_name, repository_name, login_as_user)) == 200
    elif request.param == "image":
        assert get_status(harbor_http_request.get_manifests(project_name, repository_name, image_tag, login_as_user)) == 200
    else:
        assert subprocess.call(request.param.split(" ")) == 0


@pytest.fixture(scope="function", params=["alpine"])
def repository_name(request):
    return request.param


@pytest.fixture(scope="function", params=["latest"])
def image_tag(request):
    return request.param


@pytest.fixture(scope="function", params=["Incorrect password"])
def incorrect_password(request):
    return request.param


@pytest.fixture(scope="function", params=["Abc1234"])
def correct_password(request):
    return request.param


@pytest.fixture(scope="function", params=["Newpassword"])
def new_password(request):
    return request.param