def token_user(serverName):
    if serverName == "tableau.falabella.com" :
        # For Personal Access Token sign in server tabelau.falabella.com
        personal_access_token_secret = "ELSRKK2NTLyzrpC4M3h+ZQ==:j4hdhKnrtFeD53ia8SnfR9MWGH6aTToB"  # Este es el token para el usuario usr_prd_tableau_01@falabella.cl 
            
    elif serverName == "tableau2.falabella.cl" :
        # For Personal Access Token sign in server tabelau2.falabella.cl
        personal_access_token_secret = "cnFsfNHdQS2hk1/USwaDhQ==:xUtrZmLu7xcqfXVEozksO3rTzsZuGjaM"
    return personal_access_token_secret
 
def token_name(serverName):
    if serverName == "tableau.falabella.com" :
        # For Personal Access Token sign in server tabelau.falabella.com
        personal_access_token_name = "api_token" # Este es el token para el usuario usr_prd_tableau_01@falabella.cl 
        
    elif serverName == "tableau2.falabella.cl" :
        # For Personal Access Token sign in server tabelau2.falabella.cl
        personal_access_token_name = "api_token"
    return personal_access_token_name