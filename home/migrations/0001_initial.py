# Generated by Django 4.1.3 on 2023-01-10 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="admin",
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
                ("fname", models.CharField(max_length=255)),
                ("lname", models.CharField(max_length=255)),
                ("phone", models.PositiveBigIntegerField()),
                ("password", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="hostels",
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
                ("name", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="pics")),
            ],
        ),
        migrations.CreateModel(
            name="students",
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
                ("fname", models.CharField(max_length=255)),
                ("lanme", models.CharField(max_length=255)),
                ("phone", models.PositiveBigIntegerField()),
                (
                    "dept",
                    models.CharField(
                        choices=[
                            ("CSE", "CSE"),
                            ("ISE", "ISE"),
                            ("EC", "EC"),
                            ("EEE", "EEE"),
                            ("MECHANICAL", "MECHANICAL"),
                            ("CIVIL", "CIVIL"),
                        ],
                        max_length=50,
                        verbose_name="Department",
                    ),
                ),
                ("jyear", models.DateField()),
                ("room_no", models.PositiveIntegerField()),
                (
                    "hostel_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.hostels"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="visitors",
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
                ("name", models.CharField(max_length=255)),
                ("date", models.DateField()),
                (
                    "relationship",
                    models.CharField(
                        choices=[
                            ("Father", "Father"),
                            ("Mother", "Mother"),
                            ("Brother/Sister", "Brother/Sister"),
                            ("Guardian", "Guardian"),
                        ],
                        max_length=100,
                        verbose_name="Relationship",
                    ),
                ),
                ("in_time", models.TimeField()),
                ("out_time", models.TimeField()),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.students"
                    ),
                ),
            ],
        ),
    ]
