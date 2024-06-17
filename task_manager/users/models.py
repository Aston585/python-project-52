from django.contrib.auth.models import AbstractUser


# Create your models here.
class AppUser(AbstractUser):

    def __str__(self):
        """Represent an instance as a string."""
        return self.get_full_name()
