# Funcion para crear usuario
import xml.etree.ElementTree as ET  # For parsing XML responses
import requests
from services.Add_User_Microservice.api_version import api_version
from services.Add_User_Microservice.disable_warning_ssl import disable_warning_ssl, verify
from services.Add_User_Microservice.user_model import user
from services.Add_User_Microservice.ad_error_handler import ad_error_handler


def data_request(userName, userSiteRole, fullName, serverName):

    if serverName == 'tableau2.falabella.cl' and '@bancofalabella.cl' not in userName:
        userName = str(userName).split('@')[0]  # Quita el dominio al email

    # Cuerpo de la solicitud creación usuario XML
    request_xml = ET.Element('tsRequest')
    ET.SubElement(request_xml, 'user', name=userName,
                  siteRole=userSiteRole, fullName=fullName, email=userName)
    dataRequest = ET.tostring(request_xml)
    # Solicitud API
    disable_warning_ssl(serverName)

    return dataRequest


def post_user_request(userName, userSiteRole, fullName, siteId, serverName, tokenSession):

    version = api_version(serverName)
    # URI de la peticion
    uri = "https://{server}/api/{version}/sites/{site}/users/".format(
        server=serverName, version=version, site=siteId)

    dataRequest = data_request(userName, userSiteRole, fullName, serverName)

    req = requests.post(uri, dataRequest, headers={
                        'X-Tableau-Auth': tokenSession}, verify=verify(serverName))

    err = ad_error_handler(req.status_code)

    if err:
        userId = None
        print('Usuario: ', userName, 'no se encontró en AD')
        return (userId, err)

    # Respuesta de la solicitud
    response_xml = ET.fromstring(req.content)

    # Obtener el userId de la respuesta de la solicitud
    userId = response_xml.find('.//t:user',
                               namespaces={'t': "http://tableau.com/api"}).attrib['id']

    return (userId, err)


def put_user_request(userName, userSiteRole, fullName, group, siteId, serverName, userId, tokenSession):

    version = api_version(serverName)

    # Actualización del nuevo usuario añadiendo email y fullName
    if serverName == 'tableau.falabella.com':
        uri = "https://{server}/api/{version}/sites/{site}/users/{userid}".format(
            server=serverName, version=version, site=siteId, userid=userId)
        # Solicitud API

        dataRequest = data_request(
            userName, userSiteRole, fullName, serverName)

        req = requests.put(uri, dataRequest, headers={
                           'X-Tableau-Auth': tokenSession}, verify=verify(serverName))

    return userId


def create_user(user_in_process: user, tokenSession):

    (user_id, err) = post_user_request(user_in_process.user_name, user_in_process.user_rol,
                                       user_in_process.full_name, user_in_process.site_id, user_in_process.server, tokenSession)

    if not err:

        user_id = put_user_request(user_in_process.user_name, user_in_process.user_rol, user_in_process.full_name,
                                   user_in_process.group, user_in_process.site_id, user_in_process.server, user_id, tokenSession)
        print('Se creo el usuario:', user_in_process.user_name, '-', user_in_process.server, '-',
              user_in_process.site_name, '-', user_in_process.user_rol, '-', user_in_process.group)

    user_in_process.user_id = user_id

    return (user_id, err)
