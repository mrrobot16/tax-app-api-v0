from models import Item
openapi_extra_item = {
    "requestBody": {
            "content": {
                "application/json": {
                    "schema": {
                        "required": ["name", "price"],
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "price": {"type": "number"},
                            "description": {"type": "string"},
                            "other_property": "some_property_value"
                        },
                    }
                },
                "application/x-yaml": {"schema": Item.model_json_schema()}
            },
            "required": True,
        },
    }