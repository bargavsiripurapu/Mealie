from fastapi.testclient import TestClient

from tests.utils import api_routes
from tests.utils.factories import random_string
from tests.utils.fixture_schemas import TestUser


def test_get_available_exports(api_client: TestClient, unique_user: TestUser) -> None:
    # Get Templates
    response = api_client.get(api_routes.recipes_exports, headers=unique_user.token)

    # Assert Templates are Available
    assert response.status_code == 200

    as_json = response.json()

    assert "recipes.md" in as_json["jinja2"]
    assert "raw" in as_json["json"]


def test_render_jinja_template(api_client: TestClient, unique_user: TestUser) -> None:
    # Create Recipe
    recipe_name = random_string()
    response = api_client.post(api_routes.recipes, json={"name": recipe_name}, headers=unique_user.token)
    assert response.status_code == 201
    slug = response.json()

    # Render Template
    response = api_client.get(
        api_routes.recipes_slug_exports(slug) + "?template_name=recipes.md", headers=unique_user.token
    )
    assert response.status_code == 200

    # Assert Template is Rendered Correctly
    # TODO: More robust test
    assert f"# {recipe_name}" in response.text


# TODO: Allow users to upload templates to their own directory
# def test_upload_template(api_client: TestClient, unique_user: TestUser) -> None:
#     assert False


# # TODO: Allow users to upload templates to their own directory
# def test_delete_template(api_client: TestClient, unique_user: TestUser) -> None:
#     assert False
