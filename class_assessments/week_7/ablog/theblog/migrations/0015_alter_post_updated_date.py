# Generated by Django 4.0.6 on 2022-08-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]