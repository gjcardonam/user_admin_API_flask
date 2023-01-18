from services.Add_User_Microservice.user_model import user


def re_login(user_in_process: user, user_temp: user):

    if (user_temp.site_name == user_in_process.site_name
            and user_temp.server == user_in_process.server):
        return False
    else:
        return True
