# Generated by Django 4.0.5 on 2022-07-06 09:36

import django.db.models.deletion
import wagtail.images.blocks as image_blocks
from django.db import migrations, models
from wagtail import blocks, fields

import tests.testapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PageWithNestedStreamBlock",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    fields.StreamField(
                        [
                            (
                                "inner_stream",
                                blocks.StreamBlock(
                                    [
                                        (
                                            "struct_block",
                                            blocks.StructBlock(
                                                [
                                                    (
                                                        "title",
                                                        blocks.CharBlock(
                                                            max_length=100
                                                        ),
                                                    ),
                                                    (
                                                        "item",
                                                        blocks.StructBlock(
                                                            [
                                                                (
                                                                    "label",
                                                                    blocks.CharBlock(),
                                                                ),
                                                                (
                                                                    "value",
                                                                    blocks.IntegerBlock(),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    (
                                                        "items",
                                                        blocks.ListBlock(
                                                            tests.testapp.models.MyBlockItem
                                                        ),
                                                    ),
                                                    (
                                                        "image",
                                                        image_blocks.ImageChooserBlock(),
                                                    ),
                                                ]
                                            ),
                                        ),
                                        ("char_block", blocks.CharBlock()),
                                    ]
                                ),
                            )
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="PageWithSimpleStructBlockNested",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    fields.StreamField(
                        [
                            (
                                "inner_stream",
                                blocks.StreamBlock(
                                    [
                                        (
                                            "simple_struct_block",
                                            blocks.StructBlock(
                                                [
                                                    (
                                                        "text",
                                                        blocks.CharBlock(),
                                                    ),
                                                    (
                                                        "number",
                                                        blocks.IntegerBlock(),
                                                    ),
                                                    (
                                                        "boolean",
                                                        blocks.BooleanBlock(),
                                                    ),
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="PageWithStreamBlock",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    fields.StreamField(
                        [
                            (
                                "struct_block",
                                blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            blocks.CharBlock(max_length=100),
                                        ),
                                        (
                                            "item",
                                            blocks.StructBlock(
                                                [
                                                    (
                                                        "label",
                                                        blocks.CharBlock(),
                                                    ),
                                                    (
                                                        "value",
                                                        blocks.IntegerBlock(),
                                                    ),
                                                ]
                                            ),
                                        ),
                                        (
                                            "items",
                                            blocks.ListBlock(
                                                tests.testapp.models.MyBlockItem
                                            ),
                                        ),
                                        (
                                            "image",
                                            image_blocks.ImageChooserBlock(),
                                        ),
                                    ]
                                ),
                            ),
                            ("char_block", blocks.CharBlock()),
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="PageWithStreamBlockInListBlock",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    fields.StreamField(
                        [
                            (
                                "list_block",
                                blocks.ListBlock(
                                    blocks.StreamBlock(
                                        [
                                            (
                                                "struct_block",
                                                blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            blocks.CharBlock(
                                                                max_length=100
                                                            ),
                                                        ),
                                                        (
                                                            "item",
                                                            blocks.StructBlock(
                                                                [
                                                                    (
                                                                        "label",
                                                                        blocks.CharBlock(),
                                                                    ),
                                                                    (
                                                                        "value",
                                                                        blocks.IntegerBlock(),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                        (
                                                            "items",
                                                            blocks.ListBlock(
                                                                tests.testapp.models.MyBlockItem
                                                            ),
                                                        ),
                                                        (
                                                            "image",
                                                            image_blocks.ImageChooserBlock(),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            ("char_block", blocks.CharBlock()),
                                        ]
                                    )
                                ),
                            )
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="PageWithStreamBlockInStructBlock",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    fields.StreamField(
                        [
                            (
                                "struct_block",
                                blocks.StructBlock(
                                    [
                                        (
                                            "inner_stream",
                                            blocks.StreamBlock(
                                                [
                                                    (
                                                        "struct_block",
                                                        blocks.StructBlock(
                                                            [
                                                                (
                                                                    "title",
                                                                    blocks.CharBlock(
                                                                        max_length=100
                                                                    ),
                                                                ),
                                                                (
                                                                    "item",
                                                                    blocks.StructBlock(
                                                                        [
                                                                            (
                                                                                "label",
                                                                                blocks.CharBlock(),
                                                                            ),
                                                                            (
                                                                                "value",
                                                                                blocks.IntegerBlock(),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                                (
                                                                    "items",
                                                                    blocks.ListBlock(
                                                                        tests.testapp.models.MyBlockItem
                                                                    ),
                                                                ),
                                                                (
                                                                    "image",
                                                                    image_blocks.ImageChooserBlock(),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    (
                                                        "char_block",
                                                        blocks.CharBlock(),
                                                    ),
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            )
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.AlterField(
            model_name="mytestpage",
            name="body",
            field=fields.StreamField(
                [
                    (
                        "char_array",
                        blocks.ListBlock(blocks.CharBlock()),
                    ),
                    (
                        "int_array",
                        blocks.ListBlock(blocks.IntegerBlock()),
                    ),
                    (
                        "struct",
                        blocks.StructBlock(
                            [
                                ("title", blocks.CharBlock(max_length=100)),
                                (
                                    "item",
                                    blocks.StructBlock(
                                        [
                                            ("label", blocks.CharBlock()),
                                            ("value", blocks.IntegerBlock()),
                                        ]
                                    ),
                                ),
                                (
                                    "items",
                                    blocks.ListBlock(tests.testapp.models.MyBlockItem),
                                ),
                                ("image", image_blocks.ImageChooserBlock()),
                            ]
                        ),
                    ),
                    ("image", image_blocks.ImageChooserBlock()),
                ],
            ),
        ),
    ]
