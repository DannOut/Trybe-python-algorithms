from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    test_to_crypto = "daniel"

    # teste em número impar
    assert encrypt_message(test_to_crypto, 4) == "le_inad"

    # teste em número impar
    assert encrypt_message(test_to_crypto, 5) == "einad_l"

    # teste em length maior que o test_to_crypto
    assert encrypt_message(test_to_crypto, 10) == "leinad"

    # teste caso parãmetro seja errado
    with pytest.raises(TypeError):
        encrypt_message(3, test_to_crypto)  # type: ignore
