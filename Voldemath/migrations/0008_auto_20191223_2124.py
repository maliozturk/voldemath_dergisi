# Generated by Django 2.2.7 on 2019-12-23 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Voldemath', '0007_makale_yazarin_bagli_oldugu_yer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Announcements',
        ),
        migrations.DeleteModel(
            name='Egitmen',
        ),
    ]