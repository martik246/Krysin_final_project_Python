from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage() # Хранилище картинок


class ProfessionInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)

    def __str__(self):
        return self.name


class ProfessionInfoImage(models.Model):
    professionInfo = models.ForeignKey(ProfessionInfo, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(storage=fs, upload_to="profession_info_images")

    def __str__(self):
        return self.professionInfo.name + " картинка номер " + str(self.id)

class Page(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)

    def __str__(self):
        return self.name
class Graph(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="graphs") #This field response on which page graph will be displayed
    image = models.ImageField(storage=fs, upload_to="graphs")

    def __str__(self):
        return self.name
