from typing import Any, Union


class Prop:
    """
    Basic Prop class.
    """

    def __str__(self) -> str:
        return f"{self.get()}"

    def __init__(self, val: Any) -> "Prop":
        self.value = val

    def get(self) -> Any:
        return self.value

    def update(self, val: Any) -> any:
        self.value = val

        return self.get()


class StrictProp(Prop):
    """
    Prop that have a strict value type.

    Will raise TypeError if the value is not of the expected type.
    """

    def __init__(self, data_type: Union[type, tuple[type]], val: Any) -> None:
        self._data_type = data_type
        self._validate_value(val)
        super().__init__(val)

    def _validate_value(self, val: Any) -> None:
        if not isinstance(val, self._data_type):
            raise TypeError(
                f"Expected {self._data_type} got {type(val)} ({val})"
            )

    def update(self, val: Any) -> Any:
        self._validate_value(val)

        return super().update(val)


class NumberProp(StrictProp):
    """
    Prop with strict `int | float` value type.
    """

    def __init__(
        self, val: Union[int, float], underflow_value: Union[int, float] = 0
    ) -> None:
        super().__init__((int, float), val)
        self.underflow = StrictProp((int, float), underflow_value)

    def update(self, val: Union[int, float]) -> Union[int, float]:
        old_val = self.get()
        new_val = super().update(val)

        return new_val - old_val

    def add(self, val: Union[int, float]) -> Union[int, float]:
        value_difference = self.update(self.get() + val)

        return value_difference

    def subtract(self, val: Union[int, float]) -> Union[int, float]:
        value_difference = self.update(self.get() - val)

        return value_difference

    def multiply(self, val: Union[int, float]) -> Union[int, float]:
        value_difference = self.update(self.get() * val)

        return value_difference

    def divide(self, val: Union[int, float]) -> Union[int, float]:
        value_difference = self.update(self.get() / val)

        return value_difference

    def is_underflow(self) -> bool:
        return self.get() < self.underflow.get()

    def fix_underflow(self) -> Union[int, float]:
        return self.update(self.underflow.get())


class PropWithMax(NumberProp):
    """
    A wrapper to use for a property that needs a max value.
    """

    def __str__(self) -> str:
        return f"{self.get()}/{self.max_value.get()}"

    def __init__(
        self,
        initial_value: Union[int, float],
        max_value: Union[int, float],
        underflow_value: Union[int, float] = 0,
        max_value_underflow_value: Union[int, float] = 0,
    ) -> "PropWithMax":
        super().__init__(initial_value, underflow_value)
        self.max_value = NumberProp(max_value, max_value_underflow_value)

    def current_percentage(self) -> float:
        return self.get() / self.max_value.get()

    def is_overflow(self) -> bool:
        return self.get() > self.max_value.get()

    def fix_overflow(self) -> Union[int, float]:
        return self.update(self.max_value.get())
