from django.db import models

# Create your models here.
class Request(models.Model):
    name = models.CharField("имя", max_length=15)
    description = models.TextField("способ связи")
    resume = models.BooleanField("заявка-резюме", default=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

class Region(models.Model):
    name = models.CharField("название", max_length=30)
    description = models.TextField("описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Округ"
        verbose_name_plural = "Округи"



class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True)
    guide_name = models.CharField("имя гида", max_length=30, blank=True)
    guide_avatar = models.ImageField("аватарка экскурсовода", upload_to="avatars/", blank=True)
    guide_description = models.TextField("описание экскурсовода", blank=True)
    map = models.FileField("карта района", upload_to="maps/", blank=True)
    name = models.CharField("название", max_length=30)
    image1 = models.ImageField("картинка1", upload_to="district_images/", blank=True)
    image2 = models.ImageField("картинка2", upload_to="district_images/", blank=True)
    image3 = models.ImageField("картинка3", upload_to="district_images/", blank=True)
    image4 = models.ImageField("картинка4", upload_to="district_images/", blank=True)
    image5 = models.ImageField("картинка5", upload_to="district_images/", blank=True)
    image6 = models.ImageField("картинка6", upload_to="district_images/", blank=True)
    image7 = models.ImageField("картинка7", upload_to="district_images/", blank=True)
    text1 = models.TextField("текст1", blank=True)
    text2 = models.TextField("текст2", blank=True)
    text3 = models.TextField("текст3", blank=True)
    text4 = models.TextField("текст4", blank=True)
    text5 = models.TextField("текст5", blank=True)
    text6 = models.TextField("текст6", blank=True)
    text7 = models.TextField("текст7", blank=True)
    title1 = models.CharField("заголовок1", max_length=50, blank=True)
    title2 = models.CharField("заголовок2", max_length=50, blank=True)
    title3 = models.CharField("заголовок3", max_length=50, blank=True)
    title4 = models.CharField("заголовок4", max_length=50, blank=True)
    title5 = models.CharField("заголовок5", max_length=50, blank=True)
    title6 = models.CharField("заголовок6", max_length=50, blank=True)
    title7 = models.CharField("заголовок7", max_length=50, blank=True)




    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"