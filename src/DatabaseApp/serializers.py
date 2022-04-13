from rest_framework import serializers
from DatabaseApp.models import apis,mashs


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta: 
        model=apis
        fields=("id", "apiId","title","summary","rating",
"name", "label", "author", "description", "type", "downloads",
"useCount", "sampleUrl", "downloadUrl", "dateModified",
"remoteFeed", "numComments", "commentsUrl", "Tags", "category",
"protocols", "serviceEndpoint", "version", "wsdl", "data_formats",
"apigroups", "example", "clientInstall", "authentication", "ssl",
"readonly", "VendorApiKits", "CommunityApiKits", "blog", "forum",
"support", "accountReq", "commercial", "provider", "managedBy", 
"nonCommercial", "dataLicensing", "fees", "limits", "terms", "company",
"updated")

class MashSerializer(serializers.ModelSerializer):
    class Meta:
        model=mashs
        fields=("id", "apiId","title","summary","rating",
"name", "label", "author", "description", "type", "downloads",
"useCount", "sampleUrl",  "dateModified", "numComments", "commentsUrl", "Tags", "APIs",
"updated")