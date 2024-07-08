#função para validar que o cpf tem 11 dígitos 
def validate_cpf(self, cpf):
    if len(cpf) != 11:
        raise serializers.ValidationError('O cpf deve ter 11 dígitos!')
    #caso não ocorra erros de validação, a função devolve o cpf
    return cpf
