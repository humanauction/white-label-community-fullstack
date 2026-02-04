from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model
from home.models import Event, Church
import datetime


class Command(BaseCommand):
    help = "Create sample events for Deanery Management System"

    def handle(self, *args, **options):
        User = get_user_model()

        # Get a staff user or superuser to assign as event creator;
        # create one if missing
        user = (
            User.objects.filter(is_superuser=True).first()
            or User.objects.filter(is_staff=True).first()
        )
        if not user:
            user = User.objects.create_user(
                username="demo_staff",
                password="change-me"
            )
            user.is_staff = True
            user.save(update_fields=["is_staff"])
            self.stdout.write(
                self.style.WARNING("Created demo staff user: demo_staff")
            )

        churches = list(Church.objects.all()[:5])
        now = timezone.now()

        # Ensure Christmas is always in the future
        year = now.year
        christmas_start = datetime.datetime(year, 12, 24, 23, 30)
        christmas_start = timezone.make_aware(
            christmas_start,
            timezone.get_current_timezone()
        )
        if christmas_start <= now:
            christmas_start = timezone.make_aware(
                datetime.datetime(year + 1, 12, 24, 23, 30),
                timezone.get_current_timezone(),
            )
        christmas_end = (
            christmas_start + datetime.timedelta(hours=1, minutes=30)
        )

        events = [
            {
                "title": "Christmas Midnight Mass",
                "description": (
                    "Join us for our annual Christmas Midnight Mass. /"
                    "The service will feature traditional carols, /"
                    "scripture readings, and Holy Communion. "
                    "All are welcome to attend this special celebration."
                ),
                "church": churches[0] if churches else None,
                "location": (
                    "St. Martin and St. Meriadoc Church"
                    if not churches else ""
                ),
                "start_time": christmas_start,
                "end_time": christmas_end,
                "is_featured": True,
            },
            {
                "title": "Easter Sunday Service",
                "description": (
                    "Celebrate the resurrection of Jesus Christ with our "
                    "Easter Sunday service, Egg hunt and special music. "
                    "Families are encouraged to attend together."
                ),
                "church": churches[1] if len(churches) > 1 else None,
                "location": (
                    "Holy Trinity Church" if len(churches) <= 1 else ""
                ),
                "start_time": datetime.datetime(
                    now.year + 1, 4, 9, 10, 0,
                    tzinfo=timezone.get_current_timezone()
                ),
                "end_time": datetime.datetime(
                    now.year + 1, 4, 9, 12, 0,
                    tzinfo=timezone.get_current_timezone()
                ),
                "is_featured": True
            },
            {
                "title": "Halloween Graveyard Scavenger Hunt",
                "description": (
                    (
                        "A family-friendly event exploring the /"
                        "historic graveyard. "
                        "Learn about local history while solving puzzles and /"
                        "finding clues. "
                        "Prizes for all participants. "
                        "Suitable for ages 7+. /"
                        "Please bring a torch/flashlight."
                    )
                ),
                "church": churches[2] if len(churches) > 2 else None,
                "location": (
                    "St. Illogan Church Graveyard"
                    if len(churches) <= 2 else ""
                ),
                "start_time": datetime.datetime(
                    now.year + 1, 10, 31, 18, 0,
                    tzinfo=timezone.get_current_timezone()
                ),
                "end_time": datetime.datetime(
                    now.year + 1, 10, 31, 20, 0,
                    tzinfo=timezone.get_current_timezone()
                ),
                "is_featured": False
            },
            {
                "title": "Community Coffee Morning",
                "description": (
                    "Join us for coffee, cake and conversation."
                    "Everyone welcome!"

                ),
                "church": churches[3] if len(churches) > 3 else None,
                "location": "Church Hall" if len(churches) <= 3 else "",
                "start_time": now + datetime.timedelta(days=7),
                "end_time": now + datetime.timedelta(days=7, hours=2),
                "is_featured": False
            },
            {
                "title": "Choir Practice",
                "description": (
                    "Weekly practice for the church choir."
                    "No experience necessary!"
                ),
                "church": churches[4] if len(churches) > 4 else None,
                "location": "Church Choir Room" if len(churches) <= 4 else "",
                "start_time": now + datetime.timedelta(days=3, hours=18),
                "end_time": now + datetime.timedelta(days=3, hours=20),
                "is_featured": False
            }
        ]

        count = 0
        for event_data in events:
            Event.objects.get_or_create(
                title=event_data["title"],
                start_time=event_data["start_time"],
                defaults={
                    "description": event_data["description"],
                    "church": event_data["church"],
                    "location": event_data["location"],
                    "end_time": event_data["end_time"],
                    "created_by": user,
                    "is_featured": event_data["is_featured"],
                },
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(
                    f"{count} sample events created."))
