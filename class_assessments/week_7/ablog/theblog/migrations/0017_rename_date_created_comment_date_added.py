# Generated by Django 4.0.6 on 2022-08-05 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0016_remove_post_likes_alter_post_title_tag_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date_created',
            new_name='date_added',
        ),
    ]
