from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    
    #função para validar o nome 
    def validate_nome(self, nome):
        #se eu não tiver só caracteres alfabéticos
        if not nome.isalpha():
            raise serializers.ValidationError('O nome deve ter apenas caracteres alfabéticos!')
        return nome
    
    #função para validar a quantidade de dígitos do rg
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError('O RG deve ter 9 dígitos')
        return rg
    
    #função para validar
    def validate_celula(self, celular):
        if len(celular) < 11: 
            raise serializers.ValidationError('O celular deve ter 11 dígitos no mínimo')
        return celular