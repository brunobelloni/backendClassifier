# Generated by Django 2.0.6 on 2018-07-11 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_auto_20180706_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trap_image_data',
            name='insect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classifier.Insect'),
        ),
    ]
