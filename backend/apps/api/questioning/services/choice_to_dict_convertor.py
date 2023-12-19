class ChoiceToDictConvertor(object):
    """Конвертирует choice в dict"""

    @staticmethod
    def convert(items):
        """Конвертация"""
        for el in items:
            yield {"id": el[0], "name": el[1]}
