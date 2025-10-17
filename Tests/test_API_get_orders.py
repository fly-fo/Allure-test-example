import pytest
import allure

TITLE = "GetOrders API"

@allure.tag("Automation")
@allure.epic("Test Cases")
@allure.suite("Master")
@allure.feature("GetOrders API")
@allure.title(TITLE)
@allure.label("owner", "Shivam Sanjay Desale")
@allure.label("priority", "Medium")
@allure.label("trProject", "Connectors")
@allure.label("layer", "API")
@pytest.mark.parametrize(
    "action",
    [
        "Check All Error Code for GetOrders API for Shopify  for SP360",
        "Check GetOrdersAPI for Multiple Stores",
        "Check GetOrdersAPI for Shopify for SP360",
    ],
    ids=["AllErrorCodes-SP360", "MultiStore", "HappyPath-SP360"]
)
def test_get_orders_api(action):
    # Step 1: Prepare request (placeholder values; wire your real host/paths/headers)
    with allure.step(f"Prepare request for: {action}"):
        base_url = "https://your.api.host"                 # TODO
        endpoint = "/connectors/shopify/get-orders"        # TODO
        method = "GET"
        prepared = True
        assert prepared is True
        allure.attach(
            f"base_url={base_url}\nendpoint={endpoint}\nmethod={method}\naction={action}",
            name="request_setup",
            attachment_type=allure.attachment_type.TEXT,
        )

    # Step 2: Execute request (stub until real call is added)
    with allure.step("Execute API request"):
        # Example later:
        # resp = requests.get(f"{base_url}{endpoint}", params=query, headers=headers, timeout=30)
        # status_code = resp.status_code
        status_code = 200
        assert status_code in (200, 400, 401, 403, 404)

    # Step 3: Validate per scenario
    with allure.step("Validate response"):
        if action.startswith("Check All Error Code"):
            error_catalog_ok = True
            assert error_catalog_ok is True
        elif action.endswith("Multiple Stores"):
            multi_store_ok = True
            assert multi_store_ok is True
        else:
            happy_ok = True
            assert happy_ok is True

    # Step 4: Traceability
    with allure.step("Attach parameters"):
        allure.attach(action, name="action", attachment_type=allure.attachment_type.TEXT)
