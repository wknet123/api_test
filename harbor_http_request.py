import requests
import time

__author__ = 'xiahao'

BASE_URL = "http://127.0.0.1"

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


# project api

# Post()
def create_project(project_name, session_id):
    cookies = dict(beegosessionID=session_id)
    request_payload = dict(project_name=project_name)
    r = requests.post(BASE_URL + "/api/projects", cookies=cookies, json=request_payload)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


# Head()
def check_project_exist(project_name, session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(project_name=project_name)
    r = requests.head(BASE_URL + "/api/projects", cookies=cookies, params=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response

# Get()
def list_project(project_name, is_public, session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(public=is_public, project_name=project_name)
    r = requests.get(BASE_URL + "/api/projects", cookies=cookies, params=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


# Put() toggle publicity of a project.
def update_project(project_id, is_public, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/projects/" + str(project_id)
    params = dict(public=is_public)
    r = requests.put(request_url, cookies=cookies, json=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


# repositories api
def list_repositories(project_id, query_str, session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(project_id=project_id, q=query_str)
    request_url = BASE_URL + "/api/repositories"
    r = requests.get(request_url, cookies=cookies, params=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def list_tags(repo_name, session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(repo_name=repo_name)
    request_url = BASE_URL + "/api/repositories/tags"
    r = requests.get(request_url, cookies=cookies, params=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def get_manifests(repo_name, tag, session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(repo_name=repo_name, tag=tag)
    request_url = BASE_URL + "/api/repositories/manifests"
    r = requests.get(request_url, cookies=cookies, params=params)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


# project members
def list_members(project_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/projects/" + str(project_id) + "/members"
    r = requests.get(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def get_member_of_project(project_id, user_name, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/projects/" + str(project_id) + "/members"
    params = dict(username=user_name)
    r = requests.get(request_url, params=params, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def check_project_current_member(project_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/projects/" + str(project_id) + "/members/current"
    r = requests.get(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def add_project_member(project_id, username, roles, session_id):
    cookies = dict(beegosessionID=session_id)
    request_payload = dict(user_name=username, roles=roles)
    request_url = BASE_URL + "/api/projects/" + str(project_id) + "/members"
    r = requests.post(request_url, json=request_payload, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def update_project_member(project_id, user_id, update_role_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_payload = dict(roles=update_role_id)
    request_url = BASE_URL + "/api/projects/" + str(project_id) + "/members/" + str(user_id)
    r = requests.put(request_url, json=request_payload, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def delete_project_member(project_id, user_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/projects/" + str(project_id) + "/members/" + str(user_id)
    r = requests.delete(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


# project access logs
def filter_logs(preject_id, username, keywords, begin_timestamp, end_timestamp, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/projects/" + str(preject_id) + "/logs/filter"
    request_payload = dict(username=username, preject_id=preject_id, keywords=keywords, beginTimestamp=begin_timestamp,
                           endTimestamp=end_timestamp)
    r = requests.post(request_url, json=request_payload, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


# api for user which has admin role
def list_user(username, session_id):
    cookies = dict(beegosessionID=session_id)
    params = dict(username=username)
    request_url = BASE_URL + "/api/users"
    r = requests.get(request_url, params=params, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def get_user_detail(user_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/users/" + str(user_id)
    r = requests.get(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def get_current_user(session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/users/current"
    r = requests.get(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def update_user(user_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/users/" + str(user_id)
    r = requests.put(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


def delete_user(user_id, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/users/" + str(user_id)
    r = requests.delete(request_url, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response


#Search API
def search(query_str, session_id):
    cookies = dict(beegosessionID=session_id)
    request_url = BASE_URL + "/api/search"
    params = dict(q=query_str)
    r = requests.get(request_url, params=params, cookies=cookies)
    response = dict(status_code=r.status_code, response_payload=r.text, response_cookies=r.cookies)
    return response