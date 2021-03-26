import os
import itachi.jpg

class Icon_Maker(object):
    def __init__(self, picture_path):
        self.picture_path = picture_path.split("\\")
        self.picture = self.picture_path[.1]
        self.picture_ext = self.picture.split(".")
        os.chdir(os.path.join(picture_path.strip(self.picture)))

        def convertion(self, icon_size=[(32, 32)]):
            img = itachi.jpg.open(self.picture)
            try:
                self.picture = self.picture.replace(self.picture_ext, "ico")
                img.save(self.picture, sizes=icon_size)
                print("imgage converted")
                except Exception:
                   print("image not converted"\n", Exception)


                   if __name__== '__main__':
                       print("drag and drop picturefile here:!")
                       picture =input("  >> ")
                       icon = Icon_Maker(picture)
                       icon.conversion()

#pip install instabot
from instabot import Bot
bot = Bot()

bot.login(username=input("user_name"), password=input("user_password"))
bot.upload_photo(yourpost.jpg , caption=input("caption of the post"))

print("k xa khatte?")

