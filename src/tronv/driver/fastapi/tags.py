from enum import Enum


class Tag(Enum):
    address = "Address"
    monitoring = "Monitoring"


tags_metadata = [
    {
        "name": Tag.address.value,
        "description": "Tron address endpoints.",
    },
    {
        "name": Tag.monitoring.value,
        "description": "Monitoring endpoints.",
    },
]
