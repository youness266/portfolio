import csv
from django.core.management.base import BaseCommand
from veloria_app.models import Story, Content

class Command(BaseCommand):
    help = "Import stories and sentences from CSV files"

    def handle(self, *args, **kwargs):
        # Import stories
        with open("data/stories.csv", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                Story.objects.get_or_create(
                    id=row["id"],
                    defaults={"title": row["title"], "level": row["level"]}
                )

        # Import sentences
        with open("data/sentences.csv", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                story_id = Story.objects.get(id=row["story_id"])
                Content.objects.get_or_create(
                    id=row["id"],
                    defaults={
                        "story_id": story_id,
                        "sentence": row["sentence"],
                        "translation": row["translation"],
                    }
                )
