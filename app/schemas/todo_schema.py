from marshmallow import Schema, fields, validate

class TaskSchema(Schema):
    id = fields.UUID(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str()
    is_completed = fields.Bool()
    created_at = fields.DateTime(dump_only=True)
