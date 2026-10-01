from app.services.pricing_service import apply_discount


def test_apply_discount() -> None:
    result = apply_discount(200.0, 10.0)

    assert result == 180.0