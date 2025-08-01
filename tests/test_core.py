import pandas as pd
from datacleanerpro.core import remove_constant_columns, remove_duplicates, fill_missing_values, fix_column_types

def test_remove_constant_columns():
    df = pd.DataFrame({
        'A': [1, 1, 1],
        'B': [1, 2, 3]
    })
    result = remove_constant_columns(df)
    assert 'A' not in result.columns
    assert 'B' in result.columns

def test_remove_duplicates():
    df = pd.DataFrame({
        'A': [1, 1, 2],
        'B': ['x', 'x', 'y']
    })
    result = remove_duplicates(df)
    assert len(result) == 2

def test_impute_missing_values():
    df = pd.DataFrame({
        'A': [1, None, 3],
        'B': ['a', None, 'a']
    })
    result = fill_missing_values(df)
    assert result.isnull().sum().sum() == 0

def test_fix_column_types():
    df = pd.DataFrame({
        'A': ['1', '2', '3'],
        'B': ['2023-01-01', '2023-02-01', '2023-03-01']
    })
    result = fix_column_types(df)
    assert pd.api.types.is_numeric_dtype(result['A'])
    assert pd.api.types.is_datetime64_any_dtype(result['B'])
