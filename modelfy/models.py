from modelfy.exceptions import ModelfyException


class ModelMeta(type):
    def __call__(cls, **kwargs):
        instance = super().__call__()

        annotations = cls.__annotations__

        for attribute, value in kwargs.items():
            attribute_type = annotations.get(attribute)

            # if provided attribute not in defined annotations -> do not create instance
            if not attribute_type:
                raise ModelfyException(f"Class '{cls.__name__}' does no have attribute '{attribute}' defined.")

            # if provided attribute not of desired type -> do not create instance
            if type(value) is not attribute_type:
                raise ModelfyException(f"Expected value of type {attribute_type} for '{attribute}', got '{value}' of type {type(value)}") # noqa

            setattr(instance, attribute, value)

        return instance


class BaseModel(metaclass=ModelMeta):
    def __str__(self) -> str:
        formatted_attributes = [f'{attr}={value}' for attr, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(formatted_attributes)})"

    def __repr__(self):
        return str(self)