# Define la version de la API Tableau segun el servidor
def api_version(serverName):
    
    if serverName == 'tableau.falabella.com':
        version = '3.14'
        
    elif serverName == 'tableau2.falabella.cl':
        version = '3.12'
        
    return version