# Copyright (c) 2014, Djaodjin Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from django.db import models
from . import settings
import hashlib

def file_name(instance, filename):
    split = filename.split('.')
    filename = hashlib.sha1(instance.img.read()).hexdigest() + '.' + split[1]
    path = settings.IMG_PATH
    if instance.account:
        return path + instance.account.slug + '/' + filename
    else:
        return path + filename

class PageElement(models.Model):
    """
    Elements of an editable HTML page.
    """

    slug = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    account = models.ForeignKey(
        settings.ACCOUNT_MODEL, related_name='account_page_element', null=True)

    def __unicode__(self):
        return unicode(self.slug)

class UploadedImage(models.Model):
    """
   	Image uploaded
    """

    img = models.ImageField(upload_to=file_name)
    account = models.ForeignKey(
        settings.ACCOUNT_MODEL, related_name='account_image', null=True)

    def __unicode__(self):
        return unicode(self.img)


