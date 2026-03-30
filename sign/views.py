from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from news_portal.models import Author


@login_required
def author_upgrade(request):
    now_user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(now_user)
        Author.objects.create(user=now_user)
    return redirect('/')