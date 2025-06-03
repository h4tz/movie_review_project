
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review 



@receiver(post_save, sender=Review)
def review_created_signal(sender, instance, created , **kwargs):
    
    if created:
        print(f"--- Signal Triggered: New Review Created! ---")
        print(f"Review ID: {instance.md_id}")
        print(f"Rating: {instance.rating} stars")
        print(f"By User: {instance.user.username}")
        print(f"Comment: {instance.comment[:50]}...") 
        print(f"-------------------------------------------")
        