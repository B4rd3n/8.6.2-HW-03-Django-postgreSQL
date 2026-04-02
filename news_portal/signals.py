from datetime import datetime

from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError

from .models import Post


@receiver(m2m_changed, sender=Post.post_category.through)
def notify_subscribers(sender, instance, action, **kwargs):
    if action == 'post_add' and instance.is_notified == False:
        categories = instance.post_category.all()

        if not categories.exists():
            return

        subscribers = User.objects.filter(
            subscribed_categories__in=categories
        ).distinct()

        for user in subscribers:
            if not user.email:
                continue

            html_content = render_to_string(
                'post_created.html',
                {
                    'post': instance,
                    'user': user,
                }
            )

            msg = EmailMultiAlternatives(
                subject=f'Новая статья: {instance.title}',
                body=instance.preview(),
                from_email='B4rd3n20250@yandex.ru',
                to=[user.email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        instance.is_notified = True
        instance.save(update_fields=['is_notified'])

@receiver(pre_save, sender=Post)
def is_reach_limit(sender, instance, **kwargs):
    if not instance.id:
        today = datetime.now().date()
        posts_count = Post.objects.filter(posted_by=instance.posted_by, creation_time__date = today).count()

        if posts_count >= 3:
            raise ValidationError("Вы не можете публиковать более 3 постов в день.")




