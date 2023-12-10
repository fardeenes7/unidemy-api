# Generated by Django 4.1.3 on 2023-12-10 18:28

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nid',
            fields=[
                ('id', models.CharField(blank=True, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10)),
                ('present_address', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='nid_photo')),
                ('signature', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='nid_signature')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='father_child', to='nid.nid')),
                ('mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mother_child', to='nid.nid')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]