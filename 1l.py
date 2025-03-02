from abc import ABC, abstractmethod

class Table(ABC):
    """
    Класс, представляющий стол.
    """

    def __init__(self, material: str, legs: int):
        """
        :param material: Материал стола (например, дерево, металл).
        :param legs: Количество ножек. Должно быть не менее 1.
        :raises ValueError: Если количество ножек меньше 1.
        """
        if legs < 1:
            raise ValueError("Количество ножек должно быть не меньше 1.")
        self.material = material
        self.legs = legs

    @abstractmethod
    def clean(self) -> None:
        """
        Очистить поверхность стола.
        """
        ...

    @abstractmethod
    def move(self, location: str) -> None:
        """
        Переместить стол в указанное место.

        :param location: Место, куда нужно переместить стол.
        """
        ...

class Tree(ABC):
    """
    Класс, представляющий дерево.
    """

    def __init__(self, height: float, age: int):
        """
        :param height: Высота дерева в метрах. Должна быть положительной.
        :param age: Возраст дерева в годах. Должен быть неотрицательным.
        :raises ValueError: Если высота или возраст указаны некорректно.
        """
        if height <= 0:
            raise ValueError("Высота должна быть положительной.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.height = height
        self.age = age

    @abstractmethod
    def grow(self) -> None:
        """
        Увеличить высоту дерева.
        """
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Сбрасывание листьев.
        """
        ...

class SocialNetwork(ABC):
    """
    Класс, представляющий социальную сеть.
    """

    def __init__(self, name: str, users: int):
        """
        :param name: Название социальной сети.
        :param users: Количество пользователей. Должно быть неотрицательным.
        :raises ValueError: Если количество пользователей меньше 0.
        """
        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.name = name
        self.users = users

    @abstractmethod
    def add_post(self, content: str) -> None:
        """
        Добавить пост в социальную сеть.

        :param content: Текст поста.
        """
        ...

    @abstractmethod
    def delete_post(self, post_id: int) -> None:
        """
        Удалить пост по его идентификатору.

        :param post_id: Идентификатор поста.
        """
        ...
