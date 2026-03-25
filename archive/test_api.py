import pytest

@pytest.mark.parametrize("code", [200, 201, 404, 500])
def test_status_codes(code):
    assert code in [200, 201, 404]