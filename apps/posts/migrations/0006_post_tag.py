# Generated by Django 3.2.3 on 2021-06-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_remove_tag_post'),
        ('posts', '0005_alter_postimage_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='tags.Tag', verbose_name='Тег'),
        ),
    ]
