from import_export import resources
from .models import PaymentModes, UserOwnedModes

class PaymentModesResource(resources.ModelResource):
    class Meta:
        model = PaymentModes
        fields = '__all__'

class UserOwnedModesResource(resources.ModelResource):
    class Meta:
        model = UserOwnedModes
        fields = '__all__'
