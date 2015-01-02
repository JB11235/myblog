from django.contrib.syndication.views import Feed
from .models import Entry


class LatestPosts(Feed):
    title ="myblog"
    link = "/feed/"
    description = "My Latest Posts"

    def items(self):
        return Entry.objects.published()[:5]
