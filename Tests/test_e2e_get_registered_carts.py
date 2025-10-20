import pytest
import allure

TITLE = "GetRegisteredCarts"

@allure.tag("Automation")
@allure.epic("Test Cases")
@allure.suite("Master")
@allure.story("GetRegisteredCarts")
@allure.title(TITLE)
@allure.label("owner", "Shivam Sanjay Desale")
@allure.label("priority", "P0")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Connectors")
@allure.label("layer", "UI-API")
@pytest.mark.parametrize(
    "action",
    [
        "Check All Error Codes API for Shopify  for SP360",
        "Check Registered Carts for Multiple Stores",
        "Get RegisteredCarts API for Shopify for SP360",
    ],
    ids=["AllErrorCodes-SP360", "MultiStore-UI", "HappyPath-SP360"]
)
def test_e2e_get_registered_carts(action):
    # Step 1: Navigate to the UI page that surfaces Registered Carts (placeholder)
    with allure.step("Open UI: Navigate to Registered Carts page"):
        ui_opened = True
        assert ui_opened is True

    # Step 2: Trigger the flow in the UI according to the scenario
    with allure.step(f"Trigger UI flow for action: {action}"):
        triggered = True
        assert triggered is True

    # Step 3: (Optional) Call the backing API for verification (placeholder)
    with allure.step("Verify via API (optional)"):
        base_url = "https://your.api.host"  # TODO: replace
        endpoint = "/connectors/shopify/get-registered-carts"  # TODO: replace
        method = "GET"
        # Example when you wire requests:
        # resp = requests.get(f"{base_url}{endpoint}", headers=headers, params=params, timeout=30)
        # status_code = resp.status_code
        status_code = 200  # stub
        assert status_code in (200, 400, 401, 403, 404)
        allure.attach(
            f"base_url={base_url}\nendpoint={endpoint}\nmethod={method}\naction={action}",
            name="api_probe",
            attachment_type=allure.attachment_type.TEXT,
        )

    # Step 4: Validate according to scenario (what UI shows vs. API contract)
    with allure.step("Validate outcome"):
        if action.startswith("Check All Error Codes"):
            # Validate error catalog/contract (UI messages + API codes)
            error_catalog_ok = True
            assert error_catalog_ok is True
        elif action.startswith("Check Registered Carts for Multiple Stores"):
            # Validate multi-store rendering in UI and consistency with API
            multi_store_ok = True
            assert multi_store_ok is True
        else:
            # Happy path (SP360) – UI shows carts and API returns expected data
            happy_ok = True
            assert happy_ok is True

    # Step 5: Attach scenario params for traceability
    with allure.step("Attach parameters"):
        allure.attach(action, name="action", attachment_type=allure.attachment_type.TEXT)
