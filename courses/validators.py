from django.core.exceptions import ValidationError
from urllib.parse import urlparse

def youtube_url_validator(value):
    """Валидатор для проверки ссылки на YouTube."""
    parsed_url = urlparse(value)
    if parsed_url.netloc not in ["www.youtube.com", "youtube.com"]:
        raise ValidationError("Ссылка должна вести на youtube.com")