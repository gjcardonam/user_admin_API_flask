# Funcion para agregar usuario a grupo de usuarios
import xml.etree.ElementTree as ET  # For parsing XML responses
import requests
from services.Add_User_Microservice.api_version import api_version
from services.Add_User_Microservice.disable_warning_ssl import disable_warning_ssl, verify
from services.Add_User_Microservice.user_model import user


def post_group_request(userId, groupId, siteId, serverName, tokenSession):

    version = api_version(serverName)
    # Agregar usuario al grupo de usuarios
    uri = "https://{server}/api/{version}/sites/{site}/groups/{groupId}/users/".format(
        server=serverName, version=version, site=siteId, groupId=groupId)

    request_xml = ET.Element('tsRequest')
    ET.SubElement(request_xml, 'user', id=userId)
    dataRequest = ET.tostring(request_xml)
    # Solicitud API
    disable_warning_ssl(serverName)
    req = requests.post(uri, dataRequest, headers={
                        'X-Tableau-Auth': tokenSession}, verify=verify(serverName))

    return userId


def add_user_to_group(user_in_process: user, tokenSession):

    userId = post_group_request(user_in_process.user_id, user_in_process.group_id,
                                user_in_process.site_id, user_in_process.server, tokenSession)

    return userId
