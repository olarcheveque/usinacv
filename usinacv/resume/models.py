# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from django_countries import CountryField

from cms.models import CMSPlugin


class IdentityPlugin(CMSPlugin):
    """
    Plugin to store personal infos.
    """

    first_name = models.CharField(
            verbose_name=_('First Name'),
            max_length=30)

    last_name = models.CharField(
            verbose_name=_('Last Name'),
            max_length=30)

    email = models.EmailField(
            verbose_name=_('Email'),
            max_length=255)

    city = models.CharField(
            verbose_name=_('City'),
            max_length=100)

    country = CountryField()

    phone = models.CharField(
            verbose_name=_('Phone'),
            max_length=20,
            blank=True,)

    job_title = models.CharField(
            verbose_name=_('Job Title'),
            max_length=100,
            blank=True,)

    description = models.TextField(
            verbose_name=_('Description'),
            help_text=_('use Markdown syntax'),
            blank=True,)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class SocialPlugin(CMSPlugin):
    """
    Plugin to store social links.
    """

    website = models.URLField(
            verbose_name=_('Website'),
            max_length=255,
            blank=True)

    linkedin = models.URLField(
            verbose_name=_('LinkedIn'),
            max_length=255,
            blank=True)

    github = models.URLField(
            verbose_name=_('Github'),
            max_length=255,
            blank=True)


class JobPlugin(CMSPlugin):
    """
    Plugin to store job.
    """

    date_start = models.DateField(
            verbose_name=_('Start Date'))

    date_end = models.DateField(
            verbose_name=_('End Date'),
            null=True)

    job_title = models.CharField(
            verbose_name=_('Job Title'),
            max_length=100)

    job_description = models.TextField(
            verbose_name=_('Job Description'),
            blank=True)

    company_name = models.CharField(
            verbose_name=_('Company name'),
            max_length=255)

    company_website = models.URLField(
            verbose_name=_('Company Website'),
            max_length=255,
            blank=True)

    def __unicode__(self):
        return u" %s (%s)" % (self.company_name, self.date_start, )


class ProjectPlugin(CMSPlugin):
    """
    Plugin to store project.
    """

    title = models.CharField(
            verbose_name=_('Title'),
            max_length=100)

    description = models.TextField(
            verbose_name=_('Description'),
            help_text=_('use Markdown syntax'))

    job = models.ForeignKey('JobPlugin',
            verbose_name=_('Job'),
            related_name='project_plugins',
            null=True)


class EducationPlugin(CMSPlugin):
    """
    Plugin to store education infos.
    """

    date_start = models.DateField(
            verbose_name=_('Start Date'))

    date_end = models.DateField(
            verbose_name=_('End Date'),
            null=True)

    diploma_title = models.CharField(
            verbose_name=_('Diploma'),
            max_length=100)

    diploma_description = models.TextField(
            verbose_name=_('Diploma Description'),
            help_text=_('use Markdown syntax'),
            blank=True)

    university = models.CharField(
            verbose_name=_('University'),
            max_length=255)


class TitlePlugin(CMSPlugin):
    """
    Plugin to store title (as a legend for others plugins).
    """
    title = models.CharField(
            verbose_name=_('Title'),
            max_length=100)


class FreeTextPlugin(CMSPlugin):
    """
    Plugin to store free text with mardown markup.
    """
    text = models.TextField(
            verbose_name=_('Text'),
            help_text=_('use Markdown syntax'))
