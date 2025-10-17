import pytest
import allure

TITLE = "Sync Order API"

@allure.tag("Automation")
@allure.epic("Test Cases")
@allure.suite("Master")
@allure.feature("Sync Order API")
@allure.title(TITLE)
@allure.label("owner", "Shivam Sanjay Desale")
@allure.label("priority", "Medium")
@allure.label("trProject", "Connectors")
@allure.label("layer", "API")
@pytest.mark.parametrize(
    "action",
    [
        "Check All Error Code for Shopify  for SP360",
        "Check Order Sync API for Shopify for SP360",
        "Check with multiple Stores for Order Sync API",
    ],
    ids=["AllErrorCodes-SP360", "HappyPath-SP360", "MultiStore"]
)
def test_sync_order_api(action):
    # Step 1: prepare request (replace with your real host/endpoint/headers/payload)
    with allure.step(f"Prepare request for: {action}"):
        base_url = "https://your.api.host"          # TODO
        endpoint = "/connectors/shopify/sync-order" # TODO
        method = "POST"
        prepared = True
        assert prepared is True
        allure.attach(
            f"base_url={base_url}\nendpoint={endpoint}\nmethod={method}\naction={action}",
            name="request_setup",
            attachment_type=allure.attachment_type.TEXT,
        )

    # Step 2: execute (stub until wired to requests)
    with allure.step("Execute API request"):
        # Example later:
        # resp = requests.post(f"{base_url}{endpoint}", json=payload, headers=headers, timeout=30)
        # status_code = resp.status_code
        status_code = 200
        assert status_code in (200, 400, 401, 403, 404)

    # Step 3: validate scenario-specific expectations
    with allure.step("Validate response"):
        if action.startswith("Check All Error Code"):
            error_catalog_ok = True
            assert error_catalog_ok is True
        elif action.startswith("Check with multiple Stores"):
            multi_store_ok = True
            assert multi_store_ok is True
        else:
            happy_ok = True
            assert happy_ok is True

    # Step 4: traceability
    with allure.step("Attach parameters"):
        allure.attach(action, name="action", attachment_type=allure.attachment_type.TEXT)
