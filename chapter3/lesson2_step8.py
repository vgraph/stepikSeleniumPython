"""
Задание: составные сообщения об ошибках
Для закрепления материала реализуйте проверку самостоятельно.

Вам дана функция test_input_text , которая принимает два значения: expected_result - ожидаемый результат, и actual_result - фактический результат.

Функция должна проверить совпадение значений с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.

Важно! Формат ошибки должен точно совпадать с приведенным в примере, чтобы его засчитала проверяющая система!
"""


def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'


if __name__ == '__main__':
    test_input_text(8, 11)
