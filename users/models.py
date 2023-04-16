from django.db import models
from django.contrib.auth.models import User
from webcampicture.fields import WebcamPictureField


# Create your models here.

class AmazonImageVerify(models.Model):
    user = models.ForeignKey(User,null=True,on_delete= models.CASCADE)
    a_image = models.ImageField(upload_to = 'amazon_images', verbose_name = "Image slot")
    picture = WebcamPictureField(
        "Picture", upload_to="amazon_images", blank=True
    )
    
    def __str__(self):
        return str(self.a_image)
 
class FlipcartImageVerify(models.Model):
    user = models.ForeignKey(User,null=True,on_delete= models.CASCADE)
    f_image = models.ImageField(upload_to = 'flipcart_images',verbose_name = "Image slot")

    def __str__(self):
        return str(self.f_image)

    