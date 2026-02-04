import os
from django.core.management import call_command
from django.core.management.base import BaseCommand
from home.models import Church, Event


class Command(BaseCommand):
    help = "Seed demo data (churches + sample events) if DB is empty."

    def handle(self, *args, **options):
        # Guard: only seed when explicitly enabled (avoid accidental prod wipes)
        if os.environ.get("SEED_DEMO_DATA", "").lower() not in {"1", "true", "yes", "on"}:
            self.stdout.write("SEED_DEMO_DATA not enabled; skipping seed.")
            return

        churches_count = Church.objects.count()
        events_count = Event.objects.count()

        if churches_count == 0:
            call_command("import_churches")
            self.stdout.write(self.style.SUCCESS("Seeded churches."))
        else:
            self.stdout.write(f"Churches already present ({churches_count}); skipping import.")

        if events_count == 0:
            call_command("create_sample_events")
            self.stdout.write(self.style.SUCCESS("Seeded sample events."))
        else:
            self.stdout.write(f"Events already present ({events_count}); skipping sample events.")
