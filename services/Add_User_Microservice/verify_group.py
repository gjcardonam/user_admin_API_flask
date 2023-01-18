# Funcion para verificar el Id del grupo
import xml.etree.ElementTree as ET  # For parsing XML responses
import requests
from services.Add_User_Microservice.api_version import api_version
from services.Add_User_Microservice.disable_warning_ssl import disable_warning_ssl, verify
from services.Add_User_Microservice.user_model import user
from services.Add_User_Microservice.group_error_handler import group_error_handler


def get_group_request(group, serverName, siteId, tokenSession):

    version = api_version(serverName)
    filterExpression = 'name:eq:{groupId}'.format(groupId=group)
    uri = "https://{server}/api/{version}/sites/{site}/groups?filter={filterExpression}".format(
        server=serverName, version=version, site=siteId, filterExpression=filterExpression)

    # Solicitud API
    disable_warning_ssl(serverName)
    req = requests.get(
        uri, headers={'X-Tableau-Auth': tokenSession}, verify=verify(serverName))

    response_xml = ET.fromstring(req.content)

    groupVer = response_xml.find('.//t:group',
                                 namespaces={'t': "http://tableau.com/api"})

    err = group_error_handler(groupVer)

    if err:
        groupId = None
        print('Grupo no existe:', group)
    else:
        groupId = response_xml.find('.//t:group',
                                    namespaces={'t': "http://tableau.com/api"}).attrib['id']

    return (groupId, err)


def verify_group(user_in_process: user, tokenSession):

    (groupId, err) = get_group_request(user_in_process.group,
                                       user_in_process.server, user_in_process.site_id, tokenSession)

    user_in_process.group_id = groupId

    return (groupId, err)
