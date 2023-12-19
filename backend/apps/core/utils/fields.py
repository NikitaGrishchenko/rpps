from drf_extra_fields.fields import Base64ImageField


class Base64Image(Base64ImageField):
    def to_representation(self, file):
        base64 = super(Base64Image, self).to_representation(file)
        return f"data:image;base64,{base64}" if base64 else base64
