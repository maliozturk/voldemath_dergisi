# Generated by Django 2.2.7 on 2019-12-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voldemath', '0006_auto_20191214_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='makale',
            name='yazarin_bagli_oldugu_yer',
            field=models.CharField(default='Galatasaray Üniversitesi Matematik Bölümü', max_length=150),
        ),
    ]
