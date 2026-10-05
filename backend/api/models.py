from django.db import models


class Profile(models.Model):
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveIntegerField("Возраст")
    status = models.CharField("Статус", max_length=100)
    city = models.CharField("Город", max_length=100)
    height = models.CharField("Рост", max_length=50)
    nation = models.CharField("Кто она", max_length=100)
    vibe = models.CharField("Вайб", max_length=100)

    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural = "Анкеты"

    def __str__(self):
        return self.name


class Service(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="services", verbose_name="Анкета"
    )
    title = models.CharField("Услуга", max_length=200)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class Price(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="prices", verbose_name="Анкета"
    )
    service = models.CharField("Услуга", max_length=200)
    price = models.CharField("Цена", max_length=200)

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

    def __str__(self):
        return f"{self.service} — {self.price}"


class Note(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="notes", verbose_name="Анкета"
    )
    text = models.CharField("Заметка", max_length=300)

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return self.text
