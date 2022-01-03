### main class for getting and setting Panasonic DVX200 camcorder menu settings

### RESOURCES:
### https://www.manualslib.com/manual/1914724/Panasonic-Ag-Dvx200.html?page=14#manual
### https://www.youtube.com/watch?v=RwZS3p133PY

from settings import get_default_settings


class DVX200:
    def __init__(self):
        print("initialized DVX200")
        self.settings = get_default_settings()
        print("default settings initialized")
    
    def get_all_settings(self):
        print("DVX200 SETTINGS:")
        for key in self.settings:
            print("{}: {}".format(key, self.settings[key]['value']))


dvx200 = DVX200()
dvx200.get_all_settings()