# Generated by Django 3.0.2 on 2020-06-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0002_customerdetails_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_details',
            name='qrcode',
            field=models.ImageField(blank=True, default='', upload_to=None),
        ),
    ]
