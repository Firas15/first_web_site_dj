from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=50, verbose_name= "Название изделия")
    img = models.ImageField(upload_to="portfolio_img", verbose_name="Фотография")
    description = models.TextField(verbose_name='Описание')
    dead_line = models.IntegerField(verbose_name="Сроки изготовления в днях")

    def __str__(self):
        return self.title