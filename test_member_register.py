# test_member_register.py (Student B)
import pytest
from member_register import MemberRegistry


@pytest.fixture
def registry():
    # Create a fresh registry for each test
    return MemberRegistry()


def test_register_valid_member(registry):
    # Verify that a valid member can be registered successfully
    assert registry.register("M01", "Anu", "anu@mbcet.ac.in") is True
    assert registry.count() == 1


def test_duplicate_id_rejected(registry):
    # Verify that duplicate member IDs are rejected
    registry.register("M01", "Anu", "anu@mbcet.ac.in")
    with pytest.raises(ValueError):
        registry.register("M01", "Rahul", "rahul@mbcet.ac.in")


def test_invalid_email_rejected(registry):
    # Verify that an invalid email address raises an error
    with pytest.raises(ValueError):
        registry.register("M02", "Rahul", "rahul.mbcet")


def test_empty_name_rejected(registry):
    # Verify that an empty or whitespace-only name is rejected
    with pytest.raises(ValueError):
        registry.register("M03", " ", "x@y.com")