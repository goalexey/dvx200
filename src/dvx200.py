### main class for getting and setting Panasonic DVX200 camcorder menu settings

### RESOURCES:
### https://www.manualslib.com/manual/1914724/Panasonic-Ag-Dvx200.html?page=14#manual
### https://www.youtube.com/watch?v=RwZS3p133PY

### TODO:
### 

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
    
    def get_customize_scene(self):
        return "SCENE{}".format(self.settings['customize_scene']['value'])
    
    def set_customize_scene(self, scene_number):
        self.settings['customize_scene']['value'] = scene_number


dvx200 = DVX200()
dvx200.get_all_settings()

print("getting customize scene value...")
print(dvx200.get_customize_scene())
dvx200.set_customize_scene(2)
print(dvx200.get_customize_scene())