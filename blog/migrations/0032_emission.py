# Generated by Django 3.2.5 on 2021-07-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20210414_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('date_time', models.DateTimeField(verbose_name='Date de l!emission')),
                ('audio', models.FileField(upload_to='emissions-file/')),
                ('image', models.ImageField(upload_to='emissions-images/')),
            ],
            options={
                'verbose_name': 'Listes des Emissions',
                'verbose_name_plural': 'Listes des Emissions',
                'ordering': ('-date_time',),
            },
        ),
    ]
