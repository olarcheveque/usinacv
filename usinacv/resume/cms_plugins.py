# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import IdentityPlugin as IdentityPluginModel
from .models import SocialPlugin as SocialPluginModel
from .models import JobPlugin as JobPluginModel
from .models import ProjectPlugin as ProjectPluginModel
from .models import EducationPlugin as EducationPluginModel
from .models import TitlePlugin as TitlePluginModel
from .models import FreeTextPlugin as FreeTextPluginModel


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
    model = JobPluginModel
    name = _("Job Plugin")
    render_template = "resume/job_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(JobPlugin)


class ProjectPlugin(CMSPluginBase):
    """
    Django CMS plugin for project model.
    """
    model = ProjectPluginModel
    name = _("Project Plugin")
    render_template = "resume/project_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(ProjectPlugin)


class EducationPlugin(CMSPluginBase):
    """
    Django CMS plugin for education model.
    """
    model = EducationPluginModel
    name = _("Education Plugin")
    render_template = "resume/education_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(EducationPlugin)


class TitlePlugin(CMSPluginBase):
    """
    Django CMS plugin for title model.
    """
    model = TitlePluginModel
    name = _("Title Plugin")
    render_template = "resume/title_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(TitlePlugin)


class FreeTextPlugin(CMSPluginBase):
    """
    Django CMS plugin for free text model.
    """
    model = FreeTextPluginModel
    name = _("Free Text Plugin")
    render_template = "resume/freetext_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(FreeTextPlugin)
