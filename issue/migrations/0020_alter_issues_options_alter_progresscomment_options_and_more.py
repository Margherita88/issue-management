# Generated by Django 4.2.18 on 2025-05-28 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("issue", "0019_remove_uploadfile_description_uploadfile_file_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="issues",
            options={"verbose_name": "課題", "verbose_name_plural": "課題一覧"},
        ),
        migrations.AlterModelOptions(
            name="progresscomment",
            options={
                "ordering": ["-create_date"],
                "verbose_name": "コメント",
                "verbose_name_plural": "コメント一覧",
            },
        ),
        migrations.AlterModelOptions(
            name="uploadfile",
            options={"verbose_name": "添付ファイル", "verbose_name_plural": "添付ファイル一覧"},
        ),
        migrations.AlterField(
            model_name="issues",
            name="budget",
            field=models.IntegerField(blank=True, null=True, verbose_name="予算"),
        ),
        migrations.AlterField(
            model_name="issues",
            name="contents",
            field=models.TextField(blank=True, null=True, verbose_name="内容"),
        ),
        migrations.AlterField(
            model_name="issues",
            name="create_date",
            field=models.DateField(auto_now_add=True, verbose_name="作成日"),
        ),
        migrations.AlterField(
            model_name="issues",
            name="deadline",
            field=models.DateField(blank=True, null=True, verbose_name="期限日"),
        ),
        migrations.AlterField(
            model_name="issues",
            name="person",
            field=models.ForeignKey(
                limit_choices_to={"is_superuser": False},
                on_delete=django.db.models.deletion.PROTECT,
                related_name="person_user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="担当者",
            ),
        ),
        migrations.AlterField(
            model_name="issues",
            name="progress",
            field=models.IntegerField(
                choices=[(0, "完了"), (1, "進行中"), (2, "未対応"), (3, "保留"), (4, "対応不要")],
                verbose_name="進捗状況",
            ),
        ),
        migrations.AlterField(
            model_name="issues",
            name="title",
            field=models.CharField(max_length=50, verbose_name="タイトル"),
        ),
        migrations.AlterField(
            model_name="issues",
            name="type",
            field=models.IntegerField(
                choices=[(0, "不具合"), (1, "タスク"), (2, "要望"), (3, "その他")],
                verbose_name="タイプ",
            ),
        ),
        migrations.AlterField(
            model_name="issues",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="作成者/loginユーザー",
            ),
        ),
        migrations.AlterField(
            model_name="progresscomment",
            name="comment",
            field=models.TextField(verbose_name="コメント"),
        ),
        migrations.AlterField(
            model_name="progresscomment",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="作成日"),
        ),
        migrations.AlterField(
            model_name="progresscomment",
            name="issues",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="issue.issues",
                verbose_name="対象課題",
            ),
        ),
        migrations.AlterField(
            model_name="progresscomment",
            name="update_date",
            field=models.DateTimeField(auto_now=True, verbose_name="更新日"),
        ),
        migrations.AlterField(
            model_name="progresscomment",
            name="user",
            field=models.ForeignKey(
                limit_choices_to={"is_superuser": False},
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="作成者/loginユーザー",
            ),
        ),
        migrations.AlterField(
            model_name="uploadfile",
            name="file",
            field=models.FileField(upload_to="uploads/", verbose_name="ファイル"),
        ),
        migrations.AlterField(
            model_name="uploadfile",
            name="issue",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="uploaded_files",
                to="issue.issues",
                verbose_name="対象課題",
            ),
        ),
        migrations.AlterField(
            model_name="uploadfile",
            name="uploaded_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="アップロード日時"),
        ),
    ]
