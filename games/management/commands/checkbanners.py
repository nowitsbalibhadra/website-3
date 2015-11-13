import os
from django.core.management.base import BaseCommand
from django.conf import settings
from games.models import Game


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        games = Game.objects.all()
        for game in games:
            icon_path = os.path.join(settings.MEDIA_ROOT, game.icon.name)
            if not os.path.exists(icon_path):
                print "%s is missing icon" % game
            banner_path = os.path.join(settings.MEDIA_ROOT,
                                       game.title_logo.name)
            if not os.path.exists(banner_path):
                print "%s is missing icon" % game