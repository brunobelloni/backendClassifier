from django.db import models

class Trap(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    class Meta():
        verbose_name = 'Trap'
        verbose_name_plural = 'Traps'

class Trap_Image(models.Model):
    date = models.DateField(auto_now=True)
    trap = models.ForeignKey(Trap, on_delete=models.CASCADE)
    image = models.TextField(max_length=None)

    def __str__(self):
        return str(self.id)

    class Meta():
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

class Insect(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    class Meta():
        verbose_name = 'Insect'
        verbose_name_plural = 'Insects'

class Variable(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    class Meta():
        verbose_name = 'Variable'
        verbose_name_plural = 'Variables'

class Trap_Image_Data(models.Model):
    image = models.ForeignKey(Trap_Image, on_delete=models.CASCADE)
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE)
    insect = models.ForeignKey(Insect, null=True, blank=True, on_delete=models.CASCADE)
    value = models.FloatField()
    cordX = models.IntegerField()
    cordY = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta():
        verbose_name = 'Insect_Data'
        verbose_name_plural = 'Insect_Data'
