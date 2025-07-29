from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_instructions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instructions',
            new_name='Instruction',
        ),
    ]
