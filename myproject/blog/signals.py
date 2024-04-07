from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Post, Comment


@receiver(post_save, sender=Post)
def create_initial_comment(sender, instance, created, **kwargs):
    if created:
        Comment.objects.create(post=instance, author=instance.author, text="Initial comment")


@receiver(pre_delete, sender=Post)
def delete_related_comments(sender, instance, **kwargs):
    instance.comments.all().delete()