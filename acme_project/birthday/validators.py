from datetime import date

from django.core.exceptions import ValidationError

YEAR_DAYS = 365


def real_age(value: date) -> None:
    age = (date.today() - value).days / YEAR_DAYS
    if age < 1 or age > 120:
        raise ValidationError('Ожидается возраст от 1 года до 120 лет')
  
