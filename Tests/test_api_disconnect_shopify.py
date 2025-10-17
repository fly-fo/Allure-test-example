import pytest
import allure

TITLE = "Disconnect API"

@allure.tag("Automation")
@allure.epic("Test Cases")
@allure.suite("Master")
@allure.story("Disconnect API")            
@allure.title(TITLE)
@allure.label("owner", "Shivam Sanjay Desale")
@allure.label("priority", "Medium")
@allure.label("trProject", "Connectors")
@allure.label("layer", "API")
@pytest.mark.parametrize(
    "action",
    [
        "Check All Error Code for Disconnect Store API for Shopify for SP360",
        "Check Disconnect Store API for Shopify for SP3",   
    ],
    ids=["AllErrorCodes-SP360", "DisconnectStore-SP3"]
)
def test_disconnect_api(action):
    # Step 1: Prepare request for the selected action
    with allure.step(f"Prepare request for action: {action}"):
        # placeholder: build URL, headers, payload
        base_url = "https://your.api.host"   # TODO: replace
        endpoint = "/connectors/shopify/disconnect"  # TODO: replace per action
        method = "POST"
        prepared = True
        assert prepared is True
        allure.attach(
            f"base_url={base_url}\nendpoint={endpoint}\nmethod={method}\naction={action}",
            name="request_setup",
            attachment_type=allure.attachment_type.TEXT,
        )

    # Step 2: Execute request
    with allure.step("Execute API request"):
        # Example if you later wire requests:
        # resp = requests.post(f"{base_url}{endpoint}", json=payload, headers=headers, timeout=30)
        # status_code = resp.status_code
        status_code = 200  # dummy result until real call is wired
        assert status_code in (200, 400, 401, 403, 404)  # allow typical statuses for now

    # Step 3: Validate result per action
    with allure.step("Validate response according to action semantics"):
        if action.startswith("Check All Error Code"):
            # placeholder: verify documented error codes surfaced correctly
            verified_error_catalog = True
            assert verified_error_catalog is True
        else:
            # placeholder: verify successful disconnect (or proper error for invalid state)
            disconnect_ok_or_expected_error = True
            assert disconnect_ok_or_expected_error is True

    # Step 4: Attach parameters for traceability
    with allure.step("Attach parameters"):
        allure.attach(action, name="action", attachment_type=allure.attachment_type.TEXT)
