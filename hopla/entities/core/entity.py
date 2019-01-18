from abc import ABC, abstractmethod
from ujson import dumps

from hopla.validation.validator import BaseValidator


class BaseEntity(ABC):
    @property
    @abstractmethod
    def entity_type(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def core_id(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def key(self):
        raise NotImplementedError

    @key.setter
    @abstractmethod
    def key(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def encoding(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @name.setter
    @abstractmethod
    def name(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def ttl(self):
        raise NotImplementedError

    @ttl.setter
    @abstractmethod
    def ttl(self, value):
        raise NotImplementedError

    @property
    @abstractmethod
    def options(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def validator(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def graph(self):
        raise NotImplementedError

    @abstractmethod
    def set_data(self, data):
        raise NotImplementedError

    @abstractmethod
    def get_data(self):
        raise NotImplementedError

    def validate(self):
        try:
            if not issubclass(type(self.validator), BaseValidator):
                return True
            return self.validator.validate(self.get_data())
        except NameError:
            return True

    @staticmethod
    def serialize_to_string(d):
        return dumps(d, **(dict(indent=4, sort_keys=True)))

    @staticmethod
    def clone(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __hash__(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def create_date(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def update_date(self):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def from_str(string_value, clone=None):
        raise NotImplementedError

    @abstractmethod
    def toDict(self):
        """
        Support for custom serialization with ujson
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def children(self):
        raise NotImplementedError

    @abstractmethod
    def __init__(self, *args, entity_type=None, core_id=None, encoding=None, key=None, name=None, data=None, ttl=-1,
                 validator=None, options=None, raise_event=None):
        raise NotImplementedError

    # relationships operators

    # creates relationship [self - other] without any direction
    @abstractmethod
    def __sub__(self, other):
        raise NotImplementedError

    # creates relationship [self > other] Left to Right direction
    @abstractmethod
    def __gt__(self, other):
        raise NotImplementedError

    # creates relationship [self < other] Right to Left direction
    @abstractmethod
    def __lt__(self, other):
        raise NotImplementedError