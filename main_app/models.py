from django.db import models

# Create your models here.
class HomeWelcome(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    button_title = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "1. Kirish oynasi"

class HomeYonalishlar(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    button_title = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "2. Yo'nalishlar | Chap tomon"

class HomeYonalishlarDivs(models.Model):
    svg = models.FileField(upload_to='svglar')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "3. Yo'nalishlar | O'ng tomon"

class HomeMavjudYonalishlar(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    cap_title = models.CharField(max_length=255)
    cap_color = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    letter = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "4. Mavjud yo'nalishlar"

class HomeAboutMe(models.Model):
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    title = models.CharField(max_length=255)
    cap_title = models.CharField(max_length=255)
    body = models.TextField()
    button_title = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "5. Men haqimda"

class HomeMehnatFaoliyatim(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    button_title = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "6. Mehnat faoliyatim | Chap tomon"

class HomeMehnatFaoliyatiDivs(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    year = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "7. Mehnat faoliyatim | O'ng tomon"

class HomeApp(models.Model):
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    title = models.CharField(max_length=255)
    body = models.TextField()

    app_store_title = models.CharField(max_length=255)
    app_store_link = models.CharField(max_length=255)

    google_play_title = models.CharField(max_length=255)
    google_play_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "8. Mobil ilova"

class HomeTelegramGroup(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    button_title = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "9. Telegram guruh"

class HomeQuestion(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    button_title = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "9. Savollar bormi?"

class File(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "10. Tizimga fayl yuklash"