# Funcion para verificar si el usuario existe
import xml.etree.ElementTree as ET  # For parsing XML responses
import requests
from services.Add_User_Microservice.api_version import api_version
from services.Add_User_Microservice.disable_warning_ssl import disable_warning_ssl, verify
from services.Add_User_Microservice.user_model import user


def get_user_request(userName, siteId, serverName, tokenSession):

    version = api_version(serverName)

    if serverName == 'tableau.falabella.com':
        filterExpression = 'name:eq:{userName}'.format(userName=userName)
        uri = "https://{server}/api/{version}/sites/{site}/users?filter={filterExpression}".format(
            server=serverName, version=version, site=siteId, filterExpression=filterExpression)
    elif serverName == 'tableau2.falabella.cl':
        userName = str(userName).split('@')[0]
        filterExpression = 'name:eq:{userName}'.format(userName=userName)
        uri = "https://{server}/api/{version}/sites/{site}/users?filter={filterExpression}".format(
            server=serverName, version=version, site=siteId, filterExpression=filterExpression)
    # Solicitud API
    disable_warning_ssl(serverName)
    req = requests.get(
        uri, headers={'X-Tableau-Auth': tokenSession}, verify=verify(serverName))

    response_xml = ET.fromstring(req.content)

    return response_xml


def verify_user(user_in_process: user, tokenSession):

    response_xml = get_user_request(
        user_in_process.user_name, user_in_process.site_id, user_in_process.server, tokenSession)

    user_check = response_xml.find('.//t:user',
                                   namespaces={'t': "http://tableau.com/api"})

    if user_check == None:
        user_exist = False
        return user_exist

    else:
        user_exist = True
        user_id = response_xml.find('.//t:user',
                                    namespaces={'t': "http://tableau.com/api"}).attrib['id']

        user_in_process.user_id = user_id

        return user_exist
