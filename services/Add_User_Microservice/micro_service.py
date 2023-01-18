from services.Add_User_Microservice.input_treatment import input_treatment
from services.Add_User_Microservice.login_tableau import login_tableau
from services.Add_User_Microservice.verify_user import verify_user
from services.Add_User_Microservice.create_user import create_user
from services.Add_User_Microservice.update_user import update_user
from services.Add_User_Microservice.verify_group import verify_group
from services.Add_User_Microservice.add_user_to_group import add_user_to_group
from services.Add_User_Microservice.user_model import user_model, user
from services.Add_User_Microservice.user_error_handler import user_error_handler
from services.Add_User_Microservice.re_login import re_login
from services.Add_User_Microservice.save_temps import save_temps

# Ubiacion del archivo .CSV


def add_user_micro_service(file):

    print('----- Iniciando Micro Servicio -----')

    (xml_csv, xml_no_working, xml_people_analytics) = input_treatment(file)
    '''

    user_temp = user(None, None, None, None, None, None)
    for xml in [xml_people_analytics, xml_csv, xml_no_working]:

        i = 0
        for iter in xml:

            print('--------------------------------------------')
            i += 1
            print(i)

            user_in_process = user_model(iter)

            re_login_check = re_login(user_in_process, user_temp)

            (user_full_data, licensed) = user_error_handler(user_in_process)

            if not user_full_data:
                print('Usuario:', user_in_process.user_name,
                      'no fue agregado, datos incompletos')
                continue

            if re_login_check:
                (tokenSession, site_id) = login_tableau(user_in_process)
                user_in_process.site_id = site_id
                print('Logeo necesario')
            else:
                user_in_process.site_id = user_temp.site_id

            user_exist = verify_user(user_in_process, tokenSession)

            if not user_exist:

                (user_id, err) = create_user(user_in_process, tokenSession)

            else:
                (user_id, err) = update_user(user_in_process, tokenSession)

            if licensed and not err:

                (groupId, err) = verify_group(user_in_process, tokenSession)

                if not err:

                    user_id = add_user_to_group(user_in_process, tokenSession)

            user_temp = save_temps(user_in_process)
'''
