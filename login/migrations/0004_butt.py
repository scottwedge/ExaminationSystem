# Generated by Django 2.2.5 on 2019-10-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_login_last_login_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Butt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('butter', models.CharField(blank=True, max_length=40)),
            ],
        ),
    ]