from rest_framework.serializers import Serializer

from .typing import Any

__all__ = [
    "MockSerializer",
]


class MockSerializer(Serializer):  # pragma: no cover
    # Serializer that simply passes initial data to output.

    def to_internal_value(self, data: Any) -> dict[str, Any]:  # noqa: ARG002
        return self.initial_data

    def to_representation(self, instance: Any) -> dict[str, Any]:  # noqa: ARG002
        return self.initial_data
