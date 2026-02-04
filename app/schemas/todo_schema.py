from marshmallow import Schema, fields, validate

class TaskSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(required=False)
    is_completed = fields.Bool(required=False)
