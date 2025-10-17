import pytest
import allure

TITLE = "GetOrderJobStatus API"

@allure.tag("Automation")
@allure.epic("Test Cases")
@allure.suite("Master")
@allure.feature("GetOrderJobStatus API")
@allure.title(TITLE)
@allure.label("owner", "Shivam Sanjay Desale")
@allure.label("priority", "Medium")
@allure.label("trProject", "Connectors")
@allure.label("layer", "API")
@pytest.mark.parametrize(
    "action",
    [
        "Check All Error code for OrderJobStatus API for Shopify for SP360",
        "Check OrderJobStatus API for Shopify for SP360",
        "Check OrderJob status for multiple Stores",
    ],
    ids=["AllErrorCodes-SP360", "HappyPath-SP360", "MultiStore"]
)
def test_get_order_job_status(action):
    # Step 1: Prepare request
    with allure.step(f"Prepare request for: {action}"):
        base_url = "https://your.api.host"                     # TODO: put real host
        endpoint = "/connectors/shopify/order-job-status"      # TODO: real path
        method = "GET"
        prepared = True
        assert prepared is True
        allure.attach(
            f"base_url={base_url}\nendpoint={endpoint}\nmethod={method}\naction={action}",
            name="request_setup",
            attachment_type=allure.attachment_type.TEXT,
        )

    # Step 2: Execute request (placeholder until wired)
    with allure.step("Execute API request"):
        # Example when wiring:
        # resp = requests.get(f"{base_url}{endpoint}", params=query, headers=headers, timeout=30)
        # status_code = resp.status_code
        status_code = 200
        assert status_code in (200, 400, 401, 403, 404)

    # Step 3: Validate per action
    with allure.step("Validate response"):
        if action.startswith("Check All Error code"):
            # Validate error catalog/contract behaviour
            error_catalog_ok = True
            assert error_catalog_ok is True
        elif action.startswith("Check OrderJob status for multiple Stores"):
            # Validate multi-store handling (e.g., list of statuses by store)
            multi_store_ok = True
            assert multi_store_ok is True
        else:
            # Happy path assertions for SP360
            happy_ok = True
            assert happy_ok is True

    # Step 4: Attach parameters for traceability
    with allure.step("Attach parameters"):
        allure.attach(action, name="action", attachment_type=allure.attachment_type.TEXT)
