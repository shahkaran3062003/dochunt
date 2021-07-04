# Generated by Django 3.1.7 on 2021-04-09 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='collage',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('coll_type', models.CharField(default='', max_length=7)),
                ('user_name', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
