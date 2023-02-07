from products.models import Category


def test_create_category(single_category):
    new_category = single_category
    get_category = Category.objects.all().first()

    assert get_category.id == new_category.id