# Generated by Django 3.0.3 on 2022-09-02 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nonprofit', '0002_requestdonationbox_requestenvelope_subscriptiongroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestenvelope',
            old_name='address',
            new_name='eaddress',
        ),
        migrations.RenameField(
            model_name='requestenvelope',
            old_name='city',
            new_name='ecity',
        ),
        migrations.RenameField(
            model_name='requestenvelope',
            old_name='date',
            new_name='edate',
        ),
        migrations.RenameField(
            model_name='requestenvelope',
            old_name='email',
            new_name='eemail',
        ),
        migrations.RenameField(
            model_name='requestenvelope',
            old_name='name',
            new_name='ename',
        ),
        migrations.RenameField(
            model_name='requestenvelope',
            old_name='phone',
            new_name='ephone',
        ),
        migrations.RenameField(
            model_name='requestenvelope',
            old_name='state',
            new_name='estate',
        ),
    ]
