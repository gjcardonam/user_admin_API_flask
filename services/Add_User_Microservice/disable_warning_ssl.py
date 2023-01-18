# Desactivar la verificacion de certificados SSL
import warnings

def disable_warning_ssl(serverName):
    disable = True # Quita el mensaje de advertencia
    if disable == True:
        warnings.filterwarnings("ignore", message="Unverified HTTPS request")

def verify(serverName):
    if serverName == 'tableau2.falabella.cl': #or serverName == 'tableau.falabella.com':
        verifySsl = False # Desactiva la verificacion de certificados SSL
        return verifySsl