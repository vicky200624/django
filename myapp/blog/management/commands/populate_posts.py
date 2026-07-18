from blog.models import Post,Category
from typing import Any
from django.core.management.base import BaseCommand
import random
class Command(BaseCommand):
    help = 'This command populates the database with sample data for the Post model.'

    def handle(self, *args, **kwargs):
        
        Post.objects.all().delete()  # Clear existing data to avoid duplicates
        
        titles = [
    "First Post",
    "Second Post",
    "Third Post",
    "Fourth Post",
    "Fifth Post",
    "Sixth Post",
    "Seventh Post",
    "Eighth Post",
    "Ninth Post",
    "Tenth Post",
]

        content = [
            "This is the content for the first post.",
            "This is the content for the second post.",
            "This is the content for the third post.",
            "This is the content for the fourth post.",
            "This is the content for the fifth post.",
            "This is the content for the sixth post.",
            "This is the content for the seventh post.",
            "This is the content for the eighth post.",
            "This is the content for the ninth post.",
            "This is the content for the tenth post."
        ]

        img_urls = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400"
        ]
        categories = Category.objects.all()
        for title,content,img_url in zip(titles,content,img_urls):
            Post.objects.create(title=title,content=content,img_url=img_url, category=random.choice(categories))
        
        self.stdout.write(self.style.SUCCESS('Database has been populated with sample data.'))