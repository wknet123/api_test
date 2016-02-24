__author__ = 'xiahao'

import requests
import time
import json



BASE_URL = "http://127.0.0.1"
REPOSITORIE_BASE_URL = BASE_URL + "/api/repositories"
PROJECT_BASE_URL = BASE_URL + "/api/projects"
USER_BASE_URL = BASE_URL + "/api/users"

PROJECT_ADMIN_USERNAME = "xiahadfdo"
PROJECT_USER_PASSWORD = "drgswrtfewrge"
PROJECT_NAME = "PROJECT45"


PROJECT_ADMIN_COOKIES = ""
ADMIN_COOKIES = ""

timestamp = lambda: int(round(time.time() * 1000))

def signup(username, password, email, realname, comment):
    request_url = BASE_URL + "/signUp"
    payload = dict(username=username, password=password, email=email, realname=realname, comment=comment)
    r = requests.post(url=request_url, data=payload)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def login(username, password):
    request_url = BASE_URL + "/login"
    payload = dict(principal=username, password=password)
    r = requests.post(url=request_url, data=payload)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

#project api
def list_project(session_id, is_public=False):
    request_url = PROJECT_BASE_URL
    cookies = dict(beegosessionID=session_id)
    params = dict(is_public=is_public, project_name='', timestamp=str(timestamp()))
    r = requests.get(request_url, cookies=cookies, params=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def create_project(project_name, session_id, is_public):
    cookies = dict(beegosessionID=session_id)
    request_payload = dict(project_name=project_name, public=is_public, timestamp=timestamp())
    r = requests.post(PROJECT_BASE_URL, cookies=cookies, json=request_payload)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def get_project_by_id(project_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_payload = dict(project_id=project_id)
    r = requests.get(PROJECT_BASE_URL + "/" + project_id, cookies=cookies)
    return r

def check_project_exist(project_name, session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(project_name=project_name, timestamp=timestamp())
    r = requests.get(PROJECT_BASE_URL, cookies=cookies, params=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def update_project(project_id, session_id, public=True):
    cookies = dict(beegosessionID=session_id)
    params = dict(timestamp=timestamp())
    request_url = BASE_URL + "/api/projects/" + str(project_id)
    request_payload = dict(public=public)
    r = requests.put(request_url,json=request_payload, params=params, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

#repositories api
def list_repositories(project_id, query_str, session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(project_id=project_id, q=query_str)
    request_url = REPOSITORIE_BASE_URL
    r = requests.get(request_url, cookies=cookies, params=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def list_tags(repo_name, session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(repo_name=repo_name)
    request_url = REPOSITORIE_BASE_URL + "/" + "tags"
    r = requests.get(request_url, cookies=cookies, params=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def get_manifests(repo_name, tag, session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(repo_name=repo_name, tag=tag)
    request_url = REPOSITORIE_BASE_URL + "manifests"
    r = requests.get(request_url, cookies=cookies, params=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

#project members
def list_members(project_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = PROJECT_BASE_URL + "/" + project_id + "/members/list"
    r = requests.get(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def view_roles_of_current_member(project_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = PROJECT_BASE_URL + "/" + str(project_id) + "/members/current"
    r = requests.get(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def view_roles_of_member(project_id, user_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = PROJECT_BASE_URL + "/" + project_id + user_id
    r = requests.get(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def add_project_member(project_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_payload = dict(user_name="xiahao", roles="[3]")
    request_url = PROJECT_BASE_URL + "/" + project_id + "/members/list"
    r = requests.post(request_url, json=request_payload, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def update_role_of_member(project_id, user_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_payload = dict(roles="[2]")
    request_url = PROJECT_BASE_URL + "/" + project_id + "/members" + "/" + user_id
    r =requests.put(request_url, data=request_payload, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def delete_member(project_id, user_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = PROJECT_BASE_URL + "/" + project_id + "/members" + "/" + user_id
    r =requests.delete(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


#project access logs
def list_logs(preject_id, session_id):
    cookies = dict(beegosessionID=session_id)

    request_url = PROJECT_BASE_URL + "/" + str(preject_id)+  "/" + "logs"
    r = requests.get(request_url, cookies=cookies,)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def filter_logs(preject_id, session_id, username, keywords, beginTime, endTime):
    cookies = dict(beegosessionID=session_id)
    request_url = PROJECT_BASE_URL + "/" + str(preject_id)+  "/" + "logs" + "/" + "filter"
    request_payload=dict(username=username, preject_id=preject_id, keywords=keywords, beginTime=beginTime, endTime=endTime)
    r = requests.post(request_url, json=request_payload, cookies=cookies,)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

#api for user which has admin role
def list_user(session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(username="")
    request_url = USER_BASE_URL
    r = requests.get(request_url, params=params, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def get_user_detail(user_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = USER_BASE_URL + "/" + user_id
    r = requests.get(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def get_current_user(session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = USER_BASE_URL + "/" + "current"
    r = requests.get(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def update_user(user_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = USER_BASE_URL + "/" + user_id
    r = requests.put(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

def delete_user(user_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = USER_BASE_URL + "/" + user_id
    r = requests.delete(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

















