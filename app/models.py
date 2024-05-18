from tortoise import fields, models

class File(models.Model):
    id = fields.IntField(pk=True)
    filename = fields.CharField(max_length=255)
    file_path = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    
