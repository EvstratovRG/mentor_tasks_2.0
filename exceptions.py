from builtins import BaseException


class WrongHttpMethodError(BaseException):
    """Не верный HTTP метод."""
    pass


class ValidationError(BaseException):
    """Ошибка валидации url."""
    pass


class AmountError(BaseException):
    """Недопустимое количество значений."""
    pass
