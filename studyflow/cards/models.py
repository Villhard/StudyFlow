from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Card(models.Model):
    front_side = models.TextField()
    back_side = models.TextField()
    next_time = models.DateTimeField(default=timezone.now)
    knowledge_level = models.PositiveSmallIntegerField(default=0)
    set = models.ForeignKey(
        "cards.Set", on_delete=models.CASCADE, related_name="cards"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cards"
    )

    def __str__(self):
        return (
            self.front_side
            if len(self.front_side) < 20
            else f"{self.front_side[:20]}..."
        )


class Set(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sets"
    )

    def __str__(self):
        return self.name
