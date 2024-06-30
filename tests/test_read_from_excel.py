import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.read_from_excel import read_from_excel


class TestReadFromExcel(unittest.TestCase):
    @patch("src.read_from_excel.pd.read_excel")
    @patch("builtins.open", new_callable=mock_open)
    def test_read_from_excel_success(self, mock_file, mock_read_excel):
        mock_df = pd.DataFrame(
            [
                {
                    "id": 650703,
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": 16210,
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                },
                {
                    "id": 3598919,
                    "state": "EXECUTED",
                    "date": "2020-12-06T23:00:58Z",
                    "amount": 29740,
                    "currency_name": "Peso",
                    "currency_code": "COP",
                    "from": "Discover 3172601889670065",
                    "to": "Discover 0720428384694643",
                    "description": "Перевод с карты на карту",
                },
            ]
        )
        mock_read_excel.return_value = mock_df

        file_name = "dummy_file.xlsx"
        result = read_from_excel(file_name)

        expected_result = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            },
            {
                "id": 3598919,
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": 29740,
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            },
        ]

        self.assertEqual(result, expected_result)
        mock_file.assert_called_once_with(file_name, "rb")
        mock_read_excel.assert_called_once()

    @patch("builtins.open", side_effect=FileNotFoundError("Файл не найден"))
    def test_read_from_excel_file_not_found(self, mock_file):
        file_name = "non_existent_file.xlsx"
        result = read_from_excel(file_name)

        self.assertEqual(result, "Файл не найден Файл не найден")
        mock_file.assert_called_once_with(file_name, "rb")


if __name__ == "__main__":
    unittest.main()
