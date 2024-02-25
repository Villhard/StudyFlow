from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone

User = get_user_model()


class Card(models.Model):
    front_side = models.TextField()
    back_side = models.TextField()
    next_time = models.DateTimeField(default=timezone.now, blank=True, null=True)
    knowledge_level = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(13)]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")

    def __str__(self):
        return (
            self.front_side
            if len(self.front_side) < 20
            else f"{self.front_side[:20]}..."
        )
