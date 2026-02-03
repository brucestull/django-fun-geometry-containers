# containers/management/commands/seed_containers.py

from django.core.management.base import BaseCommand
from django.db import transaction

from containers.models import Box, Cylinder, Sphere, Pyramid, Cone, Bottle, Container


class Command(BaseCommand):
    help = "Seed the containers app with fun sample data."

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete existing Container records before seeding.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options["reset"]:
            # Deleting the base class deletes subclasses (multi-table inheritance).
            Container.objects.all().delete()
            self.stdout.write(self.style.WARNING("Deleted all existing containers."))

        # -------------------
        # Boxes (cm)
        # -------------------
        boxes = [
            dict(
                name="Snack Vault of Regret",
                description="Holds chips. Also holds shame.",
                length=30,
                width=20,
                height=12,
            ),
            dict(
                name="Cable Goblin Crate",
                description="Where stray cables go to become a nest.",
                length=40,
                width=30,
                height=15,
            ),
            dict(
                name="Tiny Treasure Chest",
                description="For coins, dice, and mysterious screws.",
                length=18,
                width=12,
                height=10,
            ),
            dict(
                name="The Cardboard Cosmos",
                description="Bigger on the inside (emotionally).",
                length=60,
                width=40,
                height=35,
            ),
            dict(
                name="Lunchbox of Destiny",
                description="May contain a sandwich. May contain fate.",
                length=25,
                width=18,
                height=10,
            ),
        ]

        for item in boxes:
            obj, created = Box.objects.get_or_create(name=item["name"], defaults=item)
            if not created:
                for k, v in item.items():
                    setattr(obj, k, v)
                obj.save()
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(boxes)} boxes."))

        # -------------------
        # Cylinders (cm)
        # -------------------
        cylinders = [
            dict(
                name="Pringles of Power",
                description="Stackable victory tube.",
                radius=4,
                height=26,
            ),
            dict(
                name="The Scroll Canister",
                description="Holds ancient knowledge (or receipts).",
                radius=3,
                height=30,
            ),
            dict(
                name="Soup Can of Suspicion",
                description="It says 'tomato'. You cannot be sure.",
                radius=4.5,
                height=10,
            ),
            dict(
                name="Rocket Booster (Budget)",
                description="For pretend launches only.",
                radius=6,
                height=18,
            ),
            dict(
                name="Thermos of Eternal Coffee",
                description="Coffee that outlives your optimism.",
                radius=3.8,
                height=22,
            ),
        ]

        for item in cylinders:
            obj, created = Cylinder.objects.get_or_create(
                name=item["name"], defaults=item
            )
            if not created:
                for k, v in item.items():
                    setattr(obj, k, v)
                obj.save()
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(cylinders)} cylinders."))

        # -------------------
        # Spheres (cm)
        # -------------------
        spheres = [
            dict(
                name="Orb of Mild Concern",
                description="Gazes back, but politely.",
                radius=6,
            ),
            dict(
                name="Wizard’s Stress Ball",
                description="Squeeze to cast 'Calm-ish'.",
                radius=4,
            ),
            dict(
                name="Planet Snackos",
                description="A whole world of crunchy dreams.",
                radius=8,
            ),
            dict(
                name="Crystal Ball (Unclear Forecast)",
                description="Future: 'maybe'.",
                radius=5,
            ),
            dict(name="Marble of Chaos", description="Tiny, but dramatic.", radius=2.2),
        ]

        for item in spheres:
            obj, created = Sphere.objects.get_or_create(
                name=item["name"], defaults=item
            )
            if not created:
                for k, v in item.items():
                    setattr(obj, k, v)
                obj.save()
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(spheres)} spheres."))

        # -------------------
        # Pyramids (cm)
        # -------------------
        pyramids = [
            dict(
                name="Pharaoh’s Paperweight",
                description="Keeps your docs from escaping.",
                base_length=12,
                base_width=12,
                height=10,
            ),
            dict(
                name="Mini Monument to Procrastination",
                description="Built slowly. Admired rarely.",
                base_length=20,
                base_width=15,
                height=18,
            ),
            dict(
                name="The Pointy Reminder",
                description="Reminder: don't bump it.",
                base_length=10,
                base_width=8,
                height=12,
            ),
            dict(
                name="Desk Obelisk of Focus",
                description="Stares at you until you work.",
                base_length=14,
                base_width=14,
                height=22,
            ),
            dict(
                name="Ancient Snack Shrine",
                description="Offerings: cookies.",
                base_length=16,
                base_width=16,
                height=9,
            ),
        ]

        for item in pyramids:
            obj, created = Pyramid.objects.get_or_create(
                name=item["name"], defaults=item
            )
            if not created:
                for k, v in item.items():
                    setattr(obj, k, v)
                obj.save()
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(pyramids)} pyramids."))

        # -------------------
        # Cones (cm)
        # -------------------
        cones = [
            dict(
                name="Ice Cream Cone of Truth",
                description="Truth is sticky and delicious.",
                radius=4,
                height=12,
            ),
            dict(
                name="Traffic Cone of Doom",
                description="Blocks your path. Silently judges.",
                radius=10,
                height=32,
            ),
            dict(
                name="Wizard Hat (Prototype)",
                description="May increase intelligence by +0.2.",
                radius=6,
                height=25,
            ),
            dict(
                name="Megaphone of Petty Victory",
                description="For announcing tiny wins.",
                radius=7,
                height=20,
            ),
            dict(
                name="Funnel of Many Mistakes",
                description="Helps… but not enough.",
                radius=5,
                height=15,
            ),
        ]

        for item in cones:
            obj, created = Cone.objects.get_or_create(name=item["name"], defaults=item)
            if not created:
                for k, v in item.items():
                    setattr(obj, k, v)
                obj.save()
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(cones)} cones."))

        # -------------------
        # Bottles (cm) - cylinder body + cylinder neck
        # -------------------
        bottles = [
            dict(
                name="Potion Bottle: Slightly Braver",
                description="Side effects: confidence, mild swagger.",
                radius=3.5,
                height=14,
                neck_radius=1.2,
                neck_height=5,
            ),
            dict(
                name="Elixir Flask of Debugging",
                description="Fixes 1 bug, spawns 2 more.",
                radius=4.0,
                height=16,
                neck_radius=1.5,
                neck_height=6,
            ),
            dict(
                name="Sports Drink of Questionable Science",
                description="Electrolytes? Probably.",
                radius=3.8,
                height=18,
                neck_radius=1.4,
                neck_height=7,
            ),
            dict(
                name="Tiny Ship-in-a-Bottle (No Ship)",
                description="It's mostly vibes in there.",
                radius=2.5,
                height=10,
                neck_radius=0.9,
                neck_height=4,
            ),
            dict(
                name="Coffee Syrup Bottle: Maximum Decisions",
                description="One pump away from destiny.",
                radius=3.2,
                height=12,
                neck_radius=1.0,
                neck_height=5,
            ),
        ]

        for item in bottles:
            obj, created = Bottle.objects.get_or_create(
                name=item["name"], defaults=item
            )
            if not created:
                for k, v in item.items():
                    setattr(obj, k, v)
                obj.save()
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(bottles)} bottles."))

        self.stdout.write(self.style.SUCCESS("Seeding complete."))
