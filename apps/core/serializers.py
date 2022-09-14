import json
from collections import OrderedDict

import bleach
from rest_framework import serializers


class SanitizeData(serializers.ModelSerializer):
    class Meta:
        abstract = True

    def validate(self, data):
        clean_data = OrderedDict()
        for k, v in data.items():
            try:
                v = bleach.clean(json.dumps(v))
                clean_data[k] = json.loads(v)
            except TypeError:
                clean_data[k] = v

        return super(SanitizeData, self).validate(clean_data)