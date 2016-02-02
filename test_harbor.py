__author__ = 'shawnxia'
import harbor_http_request
import pytest
import json


class TestLogin:
    def test_projectadmin_login(self):
        response = harbor_http_request.login("userA","Pass@123")
        assert response["status_code"] == 200

    def test_invalid_username_password_login(self):
        response = harbor_http_request.login("Dmfe95gffdd","#$cvdrtaser")
        assert response["status_code"] == 401

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