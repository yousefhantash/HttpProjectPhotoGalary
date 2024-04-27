import os
from definition import *


class Photos:

    def __init__(self):
        pass

   
    def get_all_gallery_photos(self, gallery_name):
        photos = [name for name in os.listdir(Gallery_Folder+gallery_name) if(name.split(".")[0] != "Thumbs")]
        return photos


    def delete_gallery_photos(self, gallery_name, photo_name):
        if os.path.exists(Gallery_Folder + gallery_name+"/"+photo_name) is True:
            if os.remove(Gallery_Folder+gallery_name+"/"+photo_name):
                return True
            else:
                return False
        else:
            return False

