from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Tag(models.Model):
    name = models.CharField(
        verbose_name="название тэга",
        max_length=250, unique=True
    )
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "тэг"
        verbose_name_plural = "тэги"
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return self.name


class Book(models.Model):
    label = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=30)
    price = models.CharField(max_length=30, default=50)
    tags = models.ManyToManyField(
        Tag,
        verbose_name="тэги",
        related_name="recipes",
    )

    class Meta:
        db_table = 'books'
        managed = True


class Purchase(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="покупатели",
        related_name="purchases",
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="покупки",
        related_name="recipes_to_purchase",
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления",
    )

    class Meta:
        ordering = ("-date_added",)
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "book"], name="unique_purchase_user_book"
            )
        ]

    def __str__(self):
        return f"Книга {self.book} в списке покупок у {self.user}"


