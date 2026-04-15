class FileNotAvailableError(Exception):
    pass

class FileReader:
    def read(self, path: str) -> str:
        return f"Содержимое файла: {path}"

class NetworkFileReader(FileReader):
    def __init__(self, available: bool):
        self.available = available

    def read(self, path: str) -> str:
        if not self.available:
            raise FileNotAvailableError(f"Файл по сети недоступен: {path}")
        return f"Содержимое по сети: {path}"

def process(reader: FileReader, path: str):
    try:
        content = reader.read(path)
        print(content.upper())
    except FileNotAvailableError as e:
        print(e)

# Вызовы
process(FileReader(), "local.txt")
process(NetworkFileReader(available=False), "remote.txt")