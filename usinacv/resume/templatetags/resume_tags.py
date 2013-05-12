# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.filter
def who(page):
    """Get title from root page"""
    if page.parent is not None:
        return who(page.parent)
    else:
        return page.title
