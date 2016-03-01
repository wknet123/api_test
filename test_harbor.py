import harbor_http_request

__author__ = 'shawnxia'


def get_status(response):
    return response["status_code"]

def get_payload(response):
    return response["response_payload"]

class TestAllHandling:

    def test_sign_up(self, sign_up):
        assert get_status(sign_up) == 200

    def test_login_status(self, login_as_user):
        response = harbor_http_request.get_current_user(login_as_user)
        assert get_status(response) == 200

    def test_search_logined(self, query_str, login_as_user):
        response = harbor_http_request.search(query_str, login_as_user)
        assert get_status(response) == 200

    def test_search_unlogined(self, query_str):
        response = harbor_http_request.search(query_str, "")
        assert get_status(response) == 200

    def test_list_user(self, login_as_admin):
        response = harbor_http_request.list_user("", login_as_admin)
        assert get_status(response) == 200

    def test_toggle_admin_option(self, user_id_by_name, login_as_admin, login_as_user):
        response = harbor_http_request.update_user(user_id_by_name, login_as_user)
        assert get_status(response) == 403

        response = harbor_http_request.update_user(user_id_by_name, login_as_admin)
        assert get_status(response) == 200

        response = harbor_http_request.update_user(user_id_by_name, login_as_admin)
        assert get_status(response) == 200

    def test_delete_user(self, temp_user_id_by_name, login_as_admin, login_as_user):
        response = harbor_http_request.delete_user(temp_user_id_by_name, login_as_user)
        assert get_status(response) == 403

        response = harbor_http_request.delete_user(temp_user_id_by_name, login_as_admin)
        assert get_status(response) == 200

    def test_create_project(self, create_project):
        assert get_status(create_project) == 200
        # assert get_status(response) == 409

    def test_create_project_illegal(self, too_short_project_name, too_long_project_name, login_as_user):
        response = harbor_http_request.create_project(too_short_project_name, login_as_user)
        assert get_status(response) == 500

        response = harbor_http_request.create_project(too_long_project_name, login_as_user)
        assert get_status(response) == 400

    def test_project_exists(self, project_name, login_as_user):
        response = harbor_http_request.check_project_exist(project_name, login_as_user)
        assert get_status(response) == 200

    def test_list_project(self, login_as_user):
        response = harbor_http_request.list_project("", False, login_as_user)
        assert get_status(response) == 200

    def test_toggle_project_publicity(self, project_id, login_as_user):
        response = harbor_http_request.update_project(project_id, True, login_as_user)
        assert get_status(response) == 200

        response = harbor_http_request.update_project(project_id, False, login_as_user)
        assert get_status(response) == 200

    def test_repository_related(self, repository_related):
        pass

    def test_project_current_member(self, project_id, login_as_user):
        response = harbor_http_request.check_project_current_member(project_id, login_as_user)
        assert get_status(response) == 200

    def test_project_not_current_member(self, another_project_id, login_as_user):
        response = harbor_http_request.check_project_current_member(another_project_id, login_as_user)
        assert get_status(response) == 403

    def test_list_project_members(self, project_id, login_as_user):
        response = harbor_http_request.list_members(project_id, login_as_user)
        assert get_status(response) == 200

    def test_add_project_member(self, project_id, another_user_name, role_id, login_as_user):
        response = harbor_http_request.add_project_member(project_id, another_user_name, role_id, login_as_user)
        assert get_status(response) == 200

    def test_add_project_member_by_another(self, another_project_id, user_name, higher_privilege_role_id, login_as_another_user):
        response = harbor_http_request.add_project_member(another_project_id, user_name, higher_privilege_role_id, login_as_another_user)
        assert get_status(response) == 200
        # assert get_status(response) == 409

    def test_add_project_member_insufficient_privileges(self, another_project_id, another_user_name, role_id, login_as_user):
        response = harbor_http_request.add_project_member(another_project_id, another_user_name, role_id, login_as_user)
        assert get_status(response) == 409

    def test_add_project_member_nonexistent(self, project_id, nonexistent_user_name, role_id, login_as_user):
        response = harbor_http_request.add_project_member(project_id, nonexistent_user_name, role_id, login_as_user)
        assert get_status(response) == 404

    def test_update_project_member(self, project_id, user_of_project_member, update_role_id, login_as_user):
        response = harbor_http_request.update_project_member(project_id, user_of_project_member["UserId"], update_role_id, login_as_user)
        assert get_status(response) == 200

    def test_delete_project_member(self, project_id, user_of_project_member, login_as_user):
        response = harbor_http_request.delete_project_member(project_id, user_of_project_member["UserId"], login_as_user)
        assert get_status(response) == 200

    def test_filter_access_log(self, project_id, user_name, log_filter_keywords, log_filter_start_timestamp, log_filter_end_timestamp, login_as_user):
        response = harbor_http_request.filter_logs(project_id, user_name, log_filter_keywords, log_filter_start_timestamp, log_filter_end_timestamp, login_as_user)
        assert get_status(response) == 200

    def test_user_exists_username(self, user_name, nonexists_user_name):
        response = harbor_http_request.username_exists(user_name)
        assert get_status(response) == 200

        response = harbor_http_request.username_exists(nonexists_user_name)
        assert get_status(response) == 200

    def test_user_exists_email(self, email, nonexists_email):
        response = harbor_http_request.email_exists(email)
        assert get_status(response) == 200

        response = harbor_http_request.email_exists(nonexists_email)
        assert get_status(response) == 200

    def test_change_password(self, correct_password, incorrect_password, new_password, login_as_user):
        response = harbor_http_request.change_password(incorrect_password, new_password, login_as_user)
        assert get_status(response) == 403

        response = harbor_http_request.change_password(correct_password, new_password, login_as_user)
        assert get_status(response) == 200