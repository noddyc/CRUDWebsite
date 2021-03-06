# Generated by Django 3.2.10 on 2022-04-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseApp', '0002_apis_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='mashs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('apiId', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('summary', models.CharField(max_length=500)),
                ('rating', models.FloatField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=500)),
                ('label', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=500)),
                ('downloads', models.CharField(max_length=500)),
                ('useCount', models.CharField(max_length=500)),
                ('sampleUrl', models.CharField(max_length=500)),
                ('dateModified', models.CharField(max_length=500)),
                ('numComments', models.CharField(max_length=500)),
                ('commentsUrl', models.CharField(max_length=500)),
                ('Tags', models.CharField(max_length=500)),
                ('APIs', models.CharField(max_length=500)),
                ('updated', models.CharField(max_length=500)),
            ],
        ),
    ]
