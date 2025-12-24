import pytest
import allure

TITLE = "Verify end-to-end order fulfillment from ShipAccel to Shopify with Full View"

@allure.tag("Automation")
@allure.epic("Order Fulfillment E2E")
@allure.suite("ShipAccel UI Automation")
@allure.story(TITLE)
@allure.title(TITLE)
@allure.owner("Amir")
@allure.label("priority", "Medium")
@allure.label("product", "Allure")
@allure.label("layer", "API")
@allure.label("trProject", "AllureTestOps")
@allure.layer("API")                       # <-- updated layer annotation (not label)

@pytest.mark.api
def test_e2e_order_fulfillment_full_view():

    with allure.step("Open ShipAccel and ensure Shopify integration is connected"):
        assert False, "Failed to open ShipAccel or Shopify integration not connected"

    with allure.step("Create or pick an order in ShipAccel and initiate fulfillment"):
        assert False, "Order creation or fulfillment initiation failed"

    with allure.step("Generate shipping label and capture tracking number"):
        assert False, "Failed to generate label or capture tracking"

    with allure.step("Verify order sync to Shopify and status updates"):
        assert False, "Order did not sync to Shopify or statuses are incorrect"

    with allure.step("Validate Full View sections (items, charges, tracking, history)"):
        assert False, "Full View fields are empty or inconsistent"

    with allure.step("Cross-system consistency: tracking link & details"):
        assert False, "Tracking details mismatch between Shopify and ShipAccel"
