from django.template import Library

register = Library()

@register.filter
def deletable(page_item, user):
    return page_item.can_user_delete(user)
