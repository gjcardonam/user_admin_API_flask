from services.Add_User_Microservice.user_model import user


def save_temps(user_in_process: user):

    user_temp = user(None, None, None, None, None, None)
    user_temp = user_in_process

    return user_temp
