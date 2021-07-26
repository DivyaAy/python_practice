class mobiles:
    def my_color(self,color):
        self.color = color
        print(self.color)
class nokia(mobiles):
    def applications(self,app):
        self.app = app
        print(self.app)

objmobiles = mobiles()
objnokia = nokia()
objmobiles.my_color("red")
objnokia.applications("video editor")
objnokia.my_color("black")