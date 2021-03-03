from dataclasses import dataclass, fields
import typeguard
from ..ready_regex_exception import ReadyRegexException

@dataclass
class TypeHintValidationMixin:

    # Adapted from answer at https://stackoverflow.com/questions/51736938/how-to-validate-typing-attributes-in-python-3-7 by user 'Patrick Haugh'
    def _validate_types(self):
        type_errors = []
        for field in fields(self):
            print(field.name)
            attr = getattr(self, field.name)
            try:
                typeguard.check_type(field.name, attr, field.type)
            except TypeError as type_error:
                type_errors.append(type_error)
        if len(type_errors):
            raise ReadyRegexException(". ".join( ", ".join(map(str,type_error.args)) for type_error in type_errors))