# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

from abc import ABC, abstractmethod


class Table(ABC):

    def __init__(self, material: str, legs: int):
        if legs < 1:
            raise ValueError("Количество ножек должно быть не меньше 1.")
        self.material = material
        self.legs = legs

    @abstractmethod
    def clean(self) -> None:
        ...

    @abstractmethod
    def move(self, location: str) -> None:
        ...


class Tree(ABC):

    def __init__(self, height: float, age: int):

        if height <= 0:
            raise ValueError("Высота должна быть положительной.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.height = height
        self.age = age

    @abstractmethod
    def grow(self) -> None:

        ...

    @abstractmethod
    def shed_leaves(self) -> None:

        ...


class SocialNetwork(ABC):

    def __init__(self, name: str, users: int):

        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.name = name
        self.users = users

    @abstractmethod
    def add_post(self, content: str) -> None:
        ...

    @abstractmethod
    def delete_post(self, post_id: int) -> None:
        ...