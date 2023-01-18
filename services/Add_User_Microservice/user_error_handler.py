from services.Add_User_Microservice.user_model import user


def user_error_handler(user_in_process: user):

    if (user_in_process.user_rol == 'Unlicensed'
        and user_in_process.user_name
        and user_in_process.full_name
        and user_in_process.server
            and user_in_process.site_name):

        licensed = False
        user_full_data = True

    elif not (user_in_process.user_name
              and user_in_process.full_name
              and user_in_process.user_rol
              and user_in_process.server
              and user_in_process.site_name
              and user_in_process.group):

        licensed = True
        user_full_data = False

    else:
        licensed = True
        user_full_data = True

    return (user_full_data, licensed)
