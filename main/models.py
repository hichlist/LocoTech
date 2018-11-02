from django.db import models


class Branch(models.Model):
    name = models.CharField('Филиал', max_length=50, unique=True)

    def __str__(self):
        return '%s' % self.name


class Locomotive(models.Model):
    series = models.CharField('Серия', max_length=50, unique=True)
    rate = models.DecimalField('Ставка', max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s' % self.series


class Year(models.Model):
    year = models.PositiveSmallIntegerField('Год', default=2018, unique=True)

    def __str__(self):
        return '%s' % self.year


class Run(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,
                               verbose_name='Филиал')
    locomotive = models.ForeignKey(Locomotive, on_delete=models.CASCADE,
                                   verbose_name='Локомотив')
    km = models.IntegerField('Километраж')
    year = models.ForeignKey(Year, on_delete=models.CASCADE,
                             verbose_name='Год')

    def __str__(self):
        return '%s / %s km / %s year' % (
            self.locomotive, self.km, self.year)
