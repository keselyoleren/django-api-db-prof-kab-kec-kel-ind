from rest_framework import serializers, generics, mixins, viewsets
from rest_framework.response import Response
from api.models import Districts, Provinces, Regencies, Villages

# serializer
class ProvinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Provinces
        fields = "__all__"


class KabupatenSerialize(serializers.ModelSerializer):
    class Meta:
        model = Regencies
        fields = "__all__"

class KecamatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = "__all__"

class KelurahanSerialize(serializers.ModelSerializer):
    class Meta:
        model = Villages
        fields = "__all__"

# apiview
class ProvinsiApiVview(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ProvinsiSerializer
    queryset = Provinces.objects.all()


class KabupatenApiView(generics.ListAPIView):
    serializer_class = KabupatenSerialize
    def get_queryset(self):
        provinsi = Provinces.objects.get(name=self.kwargs['provinsi'])
        return Regencies.objects.filter(province=provinsi)

class KecamatanApiView(generics.ListAPIView):
    serializer_class = KecamatanSerializer
    def get_queryset(self):
        kabupaten = Regencies.objects.get(name=self.kwargs['kabupaten'])
        return Districts.objects.filter(regency=kabupaten)

class KelurahanApiView(generics.ListAPIView):
    serializer_class = KelurahanSerialize
    def get_queryset(self):
        kecamatan = Districts.objects.get(name=self.kwargs['kecamatan'])
        return Villages.objects.filter(district=kecamatan)




    