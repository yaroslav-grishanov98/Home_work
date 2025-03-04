from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    """Фикстура для предоставления тестовых данных словарей."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "PENDING", "date": "2023-01-02"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03"},
        {"id": 4, "state": "CANCELLED", "date": "2023-01-04"},
    ]


def test_filter_by_state(sample_data: List[Dict[str, Any]]) -> None:
    """Тестирование функции filter_by_state на различных статусах."""

    result = filter_by_state(sample_data, "EXECUTED")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3

    result = filter_by_state(sample_data, "PENDING")
    assert len(result) == 1
    assert result[0]["id"] == 2

    result = filter_by_state(sample_data, "CANCELLED")
    assert len(result) == 1
    assert result[0]["id"] == 4

    result = filter_by_state(sample_data, "UNKNOWN")
    assert len(result) == 0


def test_sort_by_date(sample_data: List[Dict[str, Any]]) -> None:
    """Тестирование функции sort_by_date на разных форматах данных."""

    sorted_data = sort_by_date(sample_data, reverse_order=False)
    assert sorted_data[0]["id"] == 1
    assert sorted_data[1]["id"] == 2
    assert sorted_data[2]["id"] == 3
    assert sorted_data[3]["id"] == 4

    sorted_data_desc = sort_by_date(sample_data, reverse_order=True)
    assert sorted_data_desc[0]["id"] == 4
    assert sorted_data_desc[1]["id"] == 3
    assert sorted_data_desc[2]["id"] == 2
    assert sorted_data_desc[3]["id"] == 1


# Запуск тестов:
if __name__ == "__main__":
    pytest.main()
