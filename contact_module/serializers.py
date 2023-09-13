from rest_framework import serializers
from contact_module.models import ContactUs, AboutUs


class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        exclude = ["is_read_by_admin", "created_data", "response", "user"]
        extra_kwargs = {
            "ip": {"write_only": True, "required": False},
        }


class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        # exclude = ''
        fields = "__all__"
