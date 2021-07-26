# Generated by Django 3.2.5 on 2021-07-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kryptoapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('deleted', 'deleted'), ('triggered', 'triggered')], default='created', max_length=15),
        ),
    ]