import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from home.models import Church


class Command(BaseCommand):
    help = "Import churches from csv"

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(
            settings.BASE_DIR,
            "docs",
            "NorthCarnmarthDeaneryLocations.csv",
        )

        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV not found: {csv_path}")

        count = 0
        with open(csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lat = row.get("Latitude")
                lon = row.get("Longitude")
                latitude = float(lat.strip().rstrip(",")) if lat else None
                longitude = float(lon.strip().rstrip(",")) if lon else None

                Church.objects.update_or_create(
                    name=(row.get("Name") or "").strip(),
                    postcode=(row.get("Postcode") or "").strip(),
                    defaults={
                        "address": (row.get("Address") or "").strip(),
                        "contact": (row.get("Contact") or "").strip(),
                        "contact_email": (row.get("Contact Email") or "").strip(),
                        "website": (row.get("Website") or "").strip(),
                        "latitude": latitude,
                        "longitude": longitude,
                    },
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f"Imported Churches: {count}"))
