"""Serializadores da aplicação core."""

from rest_framework import serializers


class DisableSignupSerializer(serializers.Serializer):
    """Serializador customizado."""

    def validate(self, data):
        """Desativa a criação de novas contas."""
        raise serializers.ValidationError('Registro de novas contas temporariamente suspenso.')
