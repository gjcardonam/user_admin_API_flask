class user():
    
    user_id = None
    site_id = None
    group_id = None
    
    def __init__(self,user_name,full_name,user_rol,server,site_name,group):
        self.user_name = user_name
        self.full_name = full_name
        self.user_rol = user_rol
        self.server = server
        self.site_name = site_name
        self.group = group
        
    def __str__(self):
        
        cadena = ('User: ' + self.user_name + '\n'
        + 'Full name: ' + self.full_name + '\n'
        + 'Rol: ' + self.user_rol + '\n'
        + 'Server: ' + self.server + '\n'
        + 'Site: ' + self.site_name + '\n'
        + 'Group: ' + self.group + '\n')
        
        return cadena
        
class admin():
    
    tokenSession = None

def user_model(iter):
    
    user_name = iter.find('Usuario').text # Correo
    full_name = iter.find('Nombre').text  # Nombre del usuario
    user_rol = iter.find('Rol').text # Tipo de licencia
    server = iter.find('Servidor').text # Servidor
    site_name = iter.find('Sitio').text # Sitio
    group = iter.find('Grupo').text # Sitio
    
    user_in_process = user(user_name,full_name,user_rol,server,site_name,group)
      
    return (user_in_process)