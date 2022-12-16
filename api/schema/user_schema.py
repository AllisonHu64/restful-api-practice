from marshmallow import Schema, fields

class UserSchema(Schema):
    """Helps serialize documents/row from Mongo Database's user 
    collection/table.
    """
    class Meta:
        """Contains Meta data for the Schema.

        Attributes:
            fields: Schema's fields.
        """

        fields = ["_id",
                  "id",
                  "name",
                  "age",
                  "createdInMS",
                  "updatedInMS",
                  "createdBy",
                  "updatedBy"]

    _id = fields.Str(required=True)
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)

    # Fields for audit.
    createdInMS = fields.Int(required=True)
    createdBy = fields.Str(required=True)
    updatedInMS = fields.Int(required=True)
    updatedBy = fields.Str(required=True)
