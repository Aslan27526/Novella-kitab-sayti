# Generated by Django 2.1.7 on 2019-09-02 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20190903_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitablar',
            name='shekil',
            field=models.ImageField(
                default='', upload_to='', verbose_name='Şəkil'),
        ),
    ]
