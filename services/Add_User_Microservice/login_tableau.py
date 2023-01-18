
# Use the REST API to sign in to Tableau Server and get back an authentication token
# The code use HTTPS requests when working with Tableau Server that is configured to use SSL
# The code creates and parses the XML block in the response body using the built-in ElementTree method

import xml.etree.ElementTree as ET  # For parsing XML responses
import requests  # API Request
from services.Add_User_Microservice.api_version import api_version
from services.Add_User_Microservice.disable_warning_ssl import disable_warning_ssl, verify
from services.Add_User_Microservice.token_admin import token_name, token_user
from services.Add_User_Microservice.user_model import user


def login_request(TokenUser, TokenName, serverName, siteName):

    version = api_version(serverName)

    # True = use personal access token for sign in, False = use username and password for sign in
    use_pat_flag = True

    server_name = serverName
    site_url_id = siteName

    # For username and password sign in
    user_name = ""  # User name to sign in
    password = ""

    personal_access_token_name = TokenName
    personal_access_token_secret = TokenUser

    signin_url = "https://{server}/api/{version}/auth/signin".format(
        server=server_name, version=version)

    if use_pat_flag:
        request_xml = ET.Element('tsRequest')
        credentials = ET.SubElement(request_xml, 'credentials',
                                    personalAccessTokenName=personal_access_token_name,
                                    personalAccessTokenSecret=personal_access_token_secret)
        site_element = ET.SubElement(
            credentials, 'site', contentUrl=site_url_id)

    else:
        request_xml = ET.Element('tsRequest')
        credentials = ET.SubElement(request_xml, 'credentials',
                                    name=user_name, password=password)
        site_element = ET.SubElement(
            credentials, 'site', contentUrl=site_url_id)

    request_data = ET.tostring(request_xml)

    # Send the request to the server and responsd get back in XML
    disable_warning_ssl(serverName)
    req = requests.post(signin_url, request_data, verify=verify(serverName))

    response_xml = ET.fromstring(req.content)

    # Get the authentication token from the <credentials> element
    tokenSession = response_xml.find('.//t:credentials',
                                     namespaces={'t': "http://tableau.com/api"}).attrib['token']

    # Get the site ID from the <site> element
    site_id = response_xml.find('.//t:site',
                                namespaces={'t': "http://tableau.com/api"}).attrib['id']

    return (site_id, tokenSession)


def login_tableau(user_in_process: user):

    personal_access_token_secret = token_user(user_in_process.server)
    personal_access_token_name = token_name(user_in_process.server)

    (site_id, tokenSession) = login_request(personal_access_token_secret,
                                            personal_access_token_name, user_in_process.server, user_in_process.site_name)

    return (tokenSession, site_id)
