from unittest import TestCase

from faker import Faker

from modelfy import BaseModel, ModelfyException


faker = Faker()


class TestClass(BaseModel):
    label: str
    value: int


class TestBaseModel(TestCase):
    def test_class_is_instantiated_properly(self):
        label = faker.name()
        value = faker.random.randint(1, 100)

        instance = TestClass(label=label, value=value)

        self.assertEqual(instance.label, label)
        self.assertEqual(instance.value, value)

    def test_multiple_instances_are_created(self):
        nummber_of_instances = faker.random.randint(1, 10)
        test_data = [(faker.name(), faker.random.randint(1, 100)) for _ in range(nummber_of_instances)]

        instances = [
            TestClass(label=label, value=value)
            for label, value in test_data
        ]

        for instance, test_sample in zip(instances, test_data):
            expected_label, expected_value = test_sample
            self.assertEqual(instance.label, expected_label)
            self.assertEqual(instance.value, expected_value)

    def test_if_provided_attribute_not_in_annotations_raise_modelfy_exception(self):
        with self.assertRaisesRegex(
            ModelfyException,
            f"Class '{TestClass.__name__}' does no have attribute 'other' defined."
        ):

            TestClass(
                label=faker.name(),
                value=faker.random.randint(1, 10),
                other=faker.name()
            )

    def test_if_provided_attribute_not_of_desired_type_raise_modelfy_exception(self):
        not_supported_value = faker.name()

        with self.assertRaisesRegex(
            ModelfyException,
            f"Expected value of type <class 'int'> for 'value', got '{not_supported_value}' of type {type(not_supported_value)}" # noqa
        ):
            TestClass(
                label=faker.name(),
                value=not_supported_value,
            )
