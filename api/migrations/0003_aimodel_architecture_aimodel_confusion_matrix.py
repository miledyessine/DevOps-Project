# Generated by Django 4.2 on 2024-04-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_aimodel_accuracy_aimodel_f1_score_aimodel_macro_avg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aimodel',
            name='architecture',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='aimodel',
            name='confusion_matrix',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
