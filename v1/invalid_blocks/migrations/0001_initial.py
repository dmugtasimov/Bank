# Generated by Django 3.0.6 on 2020-07-14 02:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blocks', '0001_initial'),
        ('validators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvalidBlock',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('block_identifier', models.CharField(max_length=64)),
                ('block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invalid_blocks', to='blocks.Block')),
                ('confirmation_validator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirmation_validator_invalid_blocks', to='validators.Validator')),
                ('primary_validator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_validator_invalid_blocks', to='validators.Validator')),
            ],
            options={
                'default_related_name': 'invalid_blocks',
            },
        ),
        migrations.AddConstraint(
            model_name='invalidblock',
            constraint=models.UniqueConstraint(fields=('confirmation_validator', 'primary_validator'), name='unique_confirmation_validator_primary_validator'),
        ),
    ]