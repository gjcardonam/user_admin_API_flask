# Modulo para converir el archivo .CSV a XML
import xml.etree.ElementTree as ET  # For parsing XML responses - elemntpath
import csv


def read_data(file):

    binary_data = file.read()
    str_data = binary_data.decode('ascii')
    arr_str_data = str_data.split('\n')

    ls = list()

    for item in arr_str_data:
        ls.append(item.split(','))

    headers = ls[0]
    xml_str = '<data>\n'
    ls.pop(0)

# Creación XML en str
    def convert_row(headers, row):
        s = f'<row id="{row[0]}">\n'
        for header, item in zip(headers, row):
            s += f'    <{header}>' + f'{item}' + f'</{header}>\n'
        return s + '</row>'

    for row in ls:
        xml_str += convert_row(headers, row) + '\n'
    xml_str += '</data>'

    return xml_str


def generate_xml(xml_str):

    xml_csv = ET.fromstring(xml_str)
    ls_csv = xml_str.split()  # convertir str del csv a lista del csv

    # Creación del XML para añadrir usuarios al sitio 'NoWorking'
    ls_no_working = list()
    for field in ls_csv:
        if 'tableau.falabella.com' in field:
            field = '<Servidor>tableau2.falabella.cl</Servidor>'
            ls_no_working.append(field)
        elif 'tableau2.falabella.cl' in field:
            field = '<Servidor>tableau.falabella.com</Servidor>'
            ls_no_working.append(field)
        elif '<Sitio>' in field:
            field = '<Sitio>NoWorking</Sitio>'
            ls_no_working.append(field)
        elif '<Grupo>' in field:
            field = '<Grupo>Data-NoWorking</Grupo>'
            ls_no_working.append(field)
        elif '</Grupo>' in field:
            continue
        elif 'tableau.falabella.com' or 'tableau2.falabella.cl' not in field:
            ls_no_working.append(field)

    xml_no_working_str = ' '.join(ls_no_working)
    xml_no_working = ET.fromstring(xml_no_working_str)

    # Creación del XML para añadrir usuarios al sitio 'People Analytics'
    ls_people_analytics = list()
    for field in ls_csv:
        if 'tableau2.falabella.cl' in field:
            field = '<Servidor>tableau.falabella.com</Servidor>'
            ls_people_analytics.append(field)
        elif '<Rol>' in field:
            field = '<Rol>Viewer</Rol>'
            ls_people_analytics.append(field)
        elif '<Sitio>' in field:
            field = '<Sitio>PeopleAnalytics</Sitio>'
            ls_people_analytics.append(field)
        elif '<Grupo>' in field:
            field = '<Grupo>Data-Consumer-General</Grupo>'
            ls_people_analytics.append(field)
        elif '</Grupo>' in field:
            continue
        elif 'tableau2.falabella.cl' not in field:
            ls_people_analytics.append(field)

    xml_people_analytics_str = ' '.join(ls_people_analytics)
    xml_people_analytics = ET.fromstring(xml_people_analytics_str)

    return (xml_csv, xml_no_working, xml_people_analytics)


def input_treatment(file):

    xml_str = read_data(file)
    (xml_csv, xml_no_working, xml_people_analytics) = generate_xml(xml_str)

    return (xml_csv, xml_no_working, xml_people_analytics)
