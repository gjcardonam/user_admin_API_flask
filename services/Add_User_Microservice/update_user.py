# Funcion para actualizar usuario
import xml.etree.ElementTree as ET  # For parsing XML responses
import requests
from services.Add_User_Microservice.api_version import api_version
from services.Add_User_Microservice.disable_warning_ssl import disable_warning_ssl, verify
from services.Add_User_Microservice.user_model import user
from services.Add_User_Microservice.ad_error_handler import ad_error_handler


def put_user_request(userName, userSiteRole, fullName, group, siteId, serverName, userId, tokenSession):

    version = api_version(serverName)

    # URI de la peticion
    uri = "https://{server}/api/{version}/sites/{site}/users/{userid}".format(
        server=serverName, version=version, site=siteId, userid=userId)

    # Cuerpo de la solicitud XML
    request_xml = ET.Element('tsRequest')
    ET.SubElement(request_xml, 'user', fullName=fullName,
                  email=userName, siteRole=userSiteRole)
    dataRequest = ET.tostring(request_xml)
    # Solicitud API
    disable_warning_ssl(serverName)
    req = requests.put(uri, dataRequest, headers={
                       'X-Tableau-Auth': tokenSession}, verify=verify(serverName))

    err = ad_error_handler(req.status_code)

    if err:
        userId = None
        print('Usuario: ', userName, 'no se encontró en AD')
        return (userId, err)

    return (userId, err)


def update_user(user_in_process: user, tokenSession):

    (user_id, err) = put_user_request(user_in_process.user_name, user_in_process.user_rol, user_in_process.full_name,
                                      user_in_process.group, user_in_process.site_id, user_in_process.server, user_in_process.user_id, tokenSession)
    user_in_process.user_id = user_id
    print('Se actualizo el usuario:', user_in_process.user_name, '-', user_in_process.server,
          '-', user_in_process.site_name, '-', user_in_process.user_rol, '-', user_in_process.group)

    return (user_id, err)
