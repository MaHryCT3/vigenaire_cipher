import pytest

from app.vigenaire_сipher import VigenaireСipher

@pytest.mark.parametrize(
        ('key', 'text_len', 'expected_key'),
        (
            ('KEY', 10, 'KEYKEYKEYK'),
            ('KEY', 2, 'KE'),
            ('K', 5, 'KKKKK'),
            ('KEY', 6, 'KEYKEY')
        )
)
def test_fill_key(key: str, text_len: int, expected_key: str):
    vigenaire_cipher = VigenaireСipher()
    result = vigenaire_cipher._fill_key_to_text_len(key, text_len)
    assert result == expected_key