# Generated by Django 3.0.6 on 2020-07-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conselho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedagogo', models.CharField(max_length=20)),
                ('dia', models.DateField()),
                ('classe', models.CharField(max_length=20)),
                ('ata', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Conselhoes',
            },
        ),
    ]