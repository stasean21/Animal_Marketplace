# signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone  # Убедитесь, что вы добавили этот импорт

from .models import Animal

@receiver(pre_save, sender=Animal)
def set_created_at(sender, instance, **kwargs):
    if not instance.created_at:
        instance.created_at = timezone.now()
