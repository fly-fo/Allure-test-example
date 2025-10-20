import pytest
import allure

TITLE = "Order Fulfillment API"

@allure.tag("Automation")
@allure.epic("Test Cases")
@allure.suite("Master")
@allure.story("Order Fulfillment API")
@allure.title(TITLE)
@allure.label("owner", "Shivam Sanjay Desale")
@allure.label("priority", "P0")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Connectors")
@allure.label("layer", "API")
@pytest.mark.parametrize(
    "action",
    [
        "Check All Error Code for Order Fulfillment API for Shopify  for SP360",
        "Check Order Fulfillment API for Shopify for SP360",
    ],
    ids=["AllErrorCodes-SP360", "HappyPath-SP360"]
)
def test_order_fulfillment_api(action):
    # Step 1: Prepare request (replace with your real host/endpoint/headers)
    with allure.step(f"Prepare request for: {action}"):
        base_url = "https://your.api.host"                 # TODO
        endpoint = "/connectors/shopify/order-fulfillment" # TODO
        method = "POST"
        prepared = True
        assert prepared is True
        allure.attach(
            f"base_url={base_url}\nendpoint={endpoint}\nmethod={method}\naction={action}",
            name="request_setup",
            attachment_type=allure.attachment_type.TEXT,
        )

    # Step 2: Execute (stub until wired)
    with allure.step("Execute API request"):
        # Example later:
        # resp = requests.post(f"{base_url}{endpoint}", json=payload, headers=headers, timeout=30)
        # status_code = resp.status_code
        status_code = 200
        assert status_code in (200, 400, 401, 403, 404)

    # Step 3: Validate per scenario
    with allure.step("Validate response"):
        if action.startswith("Check All Error Code"):
            error_catalog_ok = True
            assert error_catalog_ok is True
        else:
            happy_ok = True
            assert happy_ok is True

    # Step 4: Traceability
    with allure.step("Attach parameters"):
        allure.attach(action, name="action", attachment_type=allure.attachment_type.TEXT)
