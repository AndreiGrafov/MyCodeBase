from automation_testing.api_testing.APIs.api_class_example import ApiTestingExample


# very primitive test implementation
# just check that body is not empty

def test_api_get_all_meals():
    kitchen = ApiTestingExample()
    res = kitchen.get_some_meals()
    assert len(res) != 0

def test_api_get_kitchen():
    kitchen = ApiTestingExample()
    res = kitchen.get_some_kitchen()
    assert len(res) != 0

def test_api_get_next_meal():
    kitchen = ApiTestingExample()
    res = kitchen.get_next_meal()
    assert len(res) != 0

