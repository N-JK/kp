# Generated by Django 4.2.7 on 2025-03-22 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0014_alter_deliveryboy_options_remove_deliveryboy_rating_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restockrequest',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='restockrequest',
            name='requested_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restock_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='restockrequest',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AlterField(
            model_name='restockrequest',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.supplier'),
        ),
    ]
