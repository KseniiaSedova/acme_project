from django.db import models
from django.db.models import UniqueConstraint

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=20)
    last_name = models.CharField(verbose_name='Фамилия',
                                 max_length=20,
                                 blank=True, help_text='Необязательное поле')
    birthday = models.DateField(verbose_name='Дата рождения', validators=(
                                 real_age,))
    image = models.ImageField(verbose_name='Фото', 
                              upload_to='birthdays_images',
                              blank=True)

    class Meta:
        verbose_name = 'День рождения'
        verbose_name_plural = 'Дни рождения'
        constraints = [
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='unique_person_constraint'
            )
        ]
          
    def __str__(self) -> str:
        return self.first_name
