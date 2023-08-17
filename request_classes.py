from exceptions import AmountError, ValidationError, WrongHttpMethodError
from enams import HttpMethodEnum
from validators import is_valid


HTTP_METHODS = ['GET', 'POST']


class BaseRequest:
    def __init__(
            self,
            url_address: str,
            method: str,
            params: dict | None = None,
            body: dict | None = None
    ):
        self.url_address = url_address
        self.method = method.upper()
        self.query_params = params
        self.query_body = body

    @property
    def body(self: 'BaseRequest') -> str:
        query_str_body = ''
        for key, value in self.query_body.items():
            query_str_body += f'{key}={value}&'
        return query_str_body[:-1]

    @property
    def params(self: 'BaseRequest') -> str:
        query_str_params = ''
        for key, value in self.query_params.items():
            query_str_params += f'{key}={value}&'
        return query_str_params[:-1]

    def method(self: 'BaseRequest', method: str) -> str:
        if self.method in HTTP_METHODS:
            self.method = method
            return method
        else:
            raise WrongHttpMethodError

    @property
    def url(self: 'BaseRequest') -> str:
        if self.method == 'GET' and is_valid(self.url_address):
            return self.url_address + '?' + self.params
        if self.method == 'POST' and is_valid(self.url_address):
            return self.url_address + '?' + self.params + '&' + self.body
        else:
            raise ValidationError


class Request(BaseRequest):
    MAX_PARAMS_AMOUNT = 5

    def __init__(self: 'Request', url: str, method: str, params: dict, body: dict):
        if len(params) > self.MAX_PARAMS_AMOUNT:
            raise AmountError('Недопустимое количество параметров.')
        super().__init__(url, method, params, body)

    def method(self: 'Request', method: str) -> str:
        if self.method in [
            HttpMethodEnum.GET.value,
            HttpMethodEnum.POST.value,
            HttpMethodEnum.PUT.value,
            HttpMethodEnum.PATCH.value
        ]:
            self.method = method
            return method
        else:
            raise WrongHttpMethodError

    @property
    def url(self: 'Request') -> str:
        if self.method == HttpMethodEnum('GET').value and is_valid(self.url_address):
            return self.url_address + '?' + self.params

        if (self.method == HttpMethodEnum('POST').value or
                self.method == HttpMethodEnum('PUT').value or
                self.method == HttpMethodEnum('PATCH').value and
                is_valid(self.url_address)):
            return self.url_address + '?' + self.params + '&' + self.body
        else:
            raise WrongHttpMethodError
