### method that returns a dictionary of DVX200 menu settings with default values assigned

def get_default_settings():
    s = {}
    s['customize_scene'] = {
        'description': "Recall scene files",
        'value': 1,
    }
    
    s['vfr_mode'] = {
        'description': "Turn ON/OFF variable frame record mode",
        'value': "OFF"
    }
    
    ### TODO:
    ### fill up with all the other menu settings according to manual in the link:
    ### https://www.manualslib.com/manual/1914724/Panasonic-Ag-Dvx200.html?page=14#manual
    
    return s