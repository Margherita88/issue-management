# Generated by Django 4.2.18 on 2025-04-05 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("issue", "0005_rename_record_issues_progress_details"),
    ]

    operations = [
        migrations.RenameField(
            model_name="issues",
            old_name="progress_details",
            new_name="progress_comment",
        ),
        migrations.RemoveField(
            model_name="issues",
            name="date_of_update",
        ),
        migrations.AddField(
            model_name="issues",
            name="create_date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="issues",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="ProgressComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField()),
                ("create_date", models.DateField(auto_now_add=True)),
                ("update_date", models.DateField(auto_now=True)),
                (
                    "issues",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="issue.issues"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
