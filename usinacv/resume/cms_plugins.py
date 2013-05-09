# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import IdentityPlugin as IdentityPluginModel
from .models import SocialPlugin as SocialPluginModel
from .models import JobPlugin as JobPluginModel
from .models import EducationPlugin as EducationPluginModel


class IdentityPlugin(CMSPluginBase):
    """
    Django CMS plugin for identity model.
    """
    model = IdentityPluginModel
    name = _("Identity Plugin")
    render_template = "resume/identity_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(IdentityPlugin)


class SocialPlugin(CMSPluginBase):
    """
    Django CMS plugin for social model.
    """
    model = SocialPluginModel
    name = _("Social Plugin")
    render_template = "resume/social_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(SocialPlugin)


class JobPlugin(CMSPluginBase):
    """
    Django CMS plugin for job model.
    """
    model = SocialPluginModel
    name = _("Job Plugin")
    render_template = "resume/job_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(JobPlugin)


class EducationPlugin(CMSPluginBase):
    """
    Django CMS plugin for education model.
    """
    model = SocialPluginModel
    name = _("Education Plugin")
    render_template = "resume/education_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(EducationPlugin)
