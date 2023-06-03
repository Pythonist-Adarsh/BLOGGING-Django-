# Generated by Django 3.1.1 on 2021-02-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20210108_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blogid', models.IntegerField(max_length=50)),
                ('comment', models.CharField(max_length=15)),
                ('commentDate', models.DateField(max_length=20)),
            ],
        ),
    ]
