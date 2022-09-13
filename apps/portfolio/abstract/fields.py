import os

from django.core.files.storage import FileSystemStorage
from django.core.files.utils import validate_file_name
from django.db.models import ImageField

from project import settings


class OverwriteStorage(FileSystemStorage):
    def check_file(self, name):
        file_dirname = '/'.join(name.split('/')[:-1])
        prefix = '/'.join(name.split('/')[-1:]).split('.')[0]
        dirname = os.path.join(settings.MEDIA_ROOT, file_dirname)

        for s in os.listdir(dirname):
            if os.path.splitext(s)[0] == prefix and os.path.isfile(os.path.join(dirname, s)):
                return os.path.join(dirname, s)
        return None

    def generate_filename(self, name):
        exist = self.check_file(name)
        if exist:
            os.remove(exist)
        return name


class CustomImageField(ImageField):
    storage = OverwriteStorage

    def __init__(self, verbose_name=None, name=None, **kwargs):
        self.width_field, self.height_field = 100, 100
        kwargs['storage'] = self.storage
        super().__init__(verbose_name, name, **kwargs)

    def check_old_file(self, instance):
        image_path = getattr(instance, self.name+'_path')
        if image_path:
            os.remove(settings.MEDIA_ROOT + image_path)

    def set_filename(self, instance, filename):
        setattr(instance, self.name+'_path', filename)

    def generate_filename(self, instance, filename):
        self.check_old_file(instance)

        dirs = self.upload_to.split('/')
        for i in range(len(dirs)):
            path = settings.MEDIA_ROOT + '/'.join(dirs[:i])
            if not os.path.isdir(path):
                os.mkdir(path)
        ext = filename.split('.')[-1]
        name = self.upload_to + instance.get_slug
        filename = '.'.join([name, ext])
        filename = validate_file_name(filename, allow_relative_path=True)
        self.set_filename(instance, filename)
        return self.storage.generate_filename(filename)



