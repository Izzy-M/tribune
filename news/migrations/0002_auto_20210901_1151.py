# Generated by Django 3.2.6 on 2021-09-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['fname']},
        ),
    ]