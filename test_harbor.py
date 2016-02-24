__author__ = 'shawnxia'
import json

import harbor_http_request

'''
class TestLogin:
    def test_projectadmin_login(self):
        response = harbor_http_request.login("kunw","Abc1234")
        assert response["status_code"] == 200

    def test_invalid_username_password_login(self):
        response = harbor_http_request.login("Dmfe95gffdd","#$cvdrtaser")
        assert response["status_code"] == 401
'''

class TestSignUp:
    def test_sign_up(self):
        response = harbor_http_request.signup("user3", "Abc1234", "user3@vmware.com", "user3", "")
        assert response["status_code"] == 200

class TestCreateProject:
    def test_create_project(self, before):
        userA_sessionID = before["userA_sessionID"]
        response = harbor_http_request.create_project("myrepo_user3", userA_sessionID, True)
        assert response["status_code"] == 200
    def test_list_project(self, before):
        userA_sessionID = before["userA_sessionID"]
        response = harbor_http_request.list_project(userA_sessionID, True)
        assert len(response) == 1

    def test_add_project_member(self, before):
        userA_sessionID = before["userA_SessionID"]
        response1 = harbor_http_request.list_project(userA_sessionID, True)
        project_id = response1[0].project_id
        response = harbor_http_request.add_project_member(project_id, userA_sessionID)
'''
class TestListProject:
    def test_list_my_project(self, before):
        userA_sessionID = before["userA_sessionID"]
        response = harbor_http_request.list_project(userA_sessionID)
        assert response["status_code"] == 200
    def test_list_my_public_project(self, before):
        userA_sessionID = before["userA_sessionID"]
        response = harbor_http_request.list_project(userA_sessionID, is_public=True)
        assert response["status_code"] == 200
    def test_admin_list_my_project(self, before):
        admin_sessionID = before["admin_sessionID"]
        response = harbor_http_request.list_project(admin_sessionID)
        payload = json.loads(response["response_payload"])
        assert response["status_code"] == 200
        assert payload[-1]["ProjectId"] == 1
    def test_admin_list_public_project(self, before):
        admin_sessionID = before["admin_sessionID"]
        response = harbor_http_request.list_project(admin_sessionID, is_public=True)
        payload = json.loads(response["response_payload"])
        assert response["status_code"] == 200
        assert payload[-1]["ProjectId"] == 1
'''