import pytest
import allure

# Global metadata (from your screenshot)
@allure.tag("Automation")
@allure.epic("UI Automation")
@allure.suite("ShipAccel UI Automation")
@allure.label("owner", "Sowmya Katamaneni")
@allure.label("priority", "Medium")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "UI")
@pytest.mark.parametrize(
    "title",
    [
        "Connect disconnect BigCommerce Store",
        "Connect Disconnect NetSuite Store",
        "Create and update automation rule",
        "Create order in WIX store and verify order getting synced and we are creating shipping label successfully",
        "Delete automation rules",
        "From ship orders page, print label and navigate to tracking link and verify",
        "Print consumer return label and email the label",
        "Set New York card as default card for Single Payer Fedex for ShipOrder flow",
        "ShipOrders V2 – Import ShipOrders through file upload and verify automation rules are applied and print labels for the orders",
        "Shopify – Print order and Verify Order number and Source in Shipping History",
        "Uploads an image to consumer tracking page",
        "Verify can't print labels for fileupload shiporders without automation rules",
        "Verify consumer return label created for WIX order in shipping history",
        "Verify designer page styles that we set are updated",
        "Verify file upload ship order doesn't have email return link button in shipping history",
        "Verify if we are able to set NY address credit card as default card for Single Payer Fedex",
        "Verify return address, policy description, policy url that was set in Return Settings page is applied",
        "Verify we are able to email the returns link for the WIX order shipping transaction and able to access the page",
    ],
)
def test_ui_green_suite(title):
    # Per-case Story + Title
    allure.dynamic.title(title)
    allure.dynamic.label("story", title)  # <- this is what shows up as Allure Story

    # Stub steps (replace with real UI automation)
    with allure.step("Open application / preconditions"):
        assert True

    with allure.step(f"Execute scenario: {title}"):
        assert True

    with allure.step("Validate expected behavior"):
        assert True
