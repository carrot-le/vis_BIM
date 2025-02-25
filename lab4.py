from abc import ABC, abstractmethod


class Rosneft(ABC):
    """
    Базовый класс для компании Роснефть.
    """

    def init(self, branch: str, production_capacity: int) -> None:
        """
        Конструктор инициализирует филиал и производственную мощность.

        :param branch: Название филиала.
        :param production_capacity: Производственная мощность в баррелях в день.
        """
        self._branch = branch  # Защищенный атрибут, так как филиал не должен изменяться извне
        self.production_capacity = production_capacity

    def str(self) -> str:
        return f"{self._branch} Branch with {self.production_capacity} barrels/day"

    def repr(self) -> str:
        return f"Rosneft(branch={self._branch}, production_capacity={self.production_capacity})"

    @abstractmethod
    def gas_data(self) -> str:
        """
        Абстрактный метод для получения данных о добыче газа. Должен быть реализован в дочерних классах.
        """
        pass

    def oil_production(self, amount: int) -> None:
        """
        Метод добычи нефти.

        :param amount: Количество нефти для добычи в баррелях.
        """
        print(f"Producing {amount} barrels of oil")


class Tymenneftegas(Rosneft):
    """
    Класс Тюменнефтегаз, унаследованный от Rosneft.
    """

    def init(self, branch: str, production_capacity: int, gas_output: int) -> None:
        """
        Конструктор расширяет базовый класс, добавляя объем добычи газа.

        :param branch: Название филиала.
        :param production_capacity: Производственная мощность в баррелях в день.
        :param gas_output: Объем добычи газа в кубометрах.
        """
        super().init(branch, production_capacity)
        self.gas_output = gas_output

    def str(self) -> str:
        return f"{self._branch} Tymenneftegas {self.production_capacity} barrels/day, {self.gas_output} m3 gas output"

    def repr(self) -> str:
        return f"Tymenneftegas(branch={self._branch}, production_capacity={self.production_capacity}, gas_output={self.gas_output})"

    def gas_data(self) -> str:
        """
        Реализация метода получения данных о добыче газа, уникальная для Тюменнефтегаза.
        """
        return f"Gas production: {self.gas_output} cubic meters per day"

    def oil_production(self, amount: int) -> None:
        """
        Перегруженный метод добычи нефти. В Тюменнефтегазе особые условия добычи.

        :param amount: Количество нефти для добычи в баррелях.
        """
        print(f"Producing oil under special conditions: {amount} barrels")