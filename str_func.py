def to_uppercase(string):
    """Строка с заглавными буквами"""
    """
    Функция возврата строки с заглавными буквами
    """
    return string.upper()


def capitalize_first_letters(string):
    """Строка с первыми заглавными буквами"""
    return ' '.join(word.capitalize() for word in string.split())
