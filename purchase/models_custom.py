from sqlalchemy import types

class CurrencyType(types.TypeDecorator):
    impl = types.String

    def __init__(self, *args, **kwargs):
        super(CurrencyType, self).__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        # Validate and process the value before storing it
        if value is None:
            return None
        value = str(value).upper()
        if value not in ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'AUD', 'CAD', 'IDR']:
            raise ValueError(f"Invalid currency code: {value}")
        return value

    def process_result_value(self, value, dialect):
        # Process the value when retrieving it from the database
        return value
