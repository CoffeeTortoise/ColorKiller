from typing import Any


class SaveLoad:
    
    @staticmethod
    def save_file(path: str, value: Any) -> None:
        with open(path, 'w') as file:
            item: str = str(value)
            file.write(item)
    
    @staticmethod
    def load_file(path: str) -> str:
        with open(path, 'r') as file:
            value: str = file.read()
        return value
    