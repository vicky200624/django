from blog.models import Category
from typing import Any
from django.core.management.base import BaseCommand
  
class Command(BaseCommand):
    help = 'This command populates the database with sample category data for the Post model.'

    def handle(self, *args, **kwargs):
        
        Category.objects.all().delete()  # Clear existing data to avoid duplicates
        
        category_names = [
            "Technology",
            "Science",
            "Health",
            "Education",
            "Business"
        ]

        for name in category_names:
            Category.objects.create(name=name)

        
        
        self.stdout.write(self.style.SUCCESS('Database has been populated with sample category data.'))