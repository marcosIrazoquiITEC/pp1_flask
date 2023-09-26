from app import ma
from marshmallow import fields

class UserBasicSchema(ma.Schema):
    username = fields.String()

class UserAdminSchema(UserBasicSchema):
    id = fields.Integer(dump_only=True)
    password_hash = fields.String()
    hi_username = fields.Method('get_username')

    def get_username(self,obj):
        return f'hi {obj.username}'

class PaisSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    nombre = fields.String()

class ProvinciaSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    nombre = fields.String()
    pais_obj = fields.Nested(PaisSchema,)

class LocalidadSchema(ma.Schema):
    id = fields.Integer(dump_only = True)
    nombre = fields.String()
    provincia_obj = fields.Nested(ProvinciaSchema,)