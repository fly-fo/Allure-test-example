import pytest
import allure

# 2
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Connect Disconnect NetSuite Store")
@allure.title("Connect Disconnect NetSuite Store")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_connect_disconnect_netsuite_store():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Connect/disconnect NetSuite"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 3
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Create and update automation rule")
@allure.title("Create and update automation rule")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_create_and_update_automation_rule():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Create & update rule"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 4
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Create order in WIX store and verify order getting synced and we are creating shipping label successfully")
@allure.title("Create order in WIX store and verify order getting synced and we are creating shipping label successfully")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_wix_order_sync_and_label():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Create WIX order, sync & create label"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 5
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Delete automation rules")
@allure.title("Delete automation rules")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_delete_automation_rules():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Delete rule(s)"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 6
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("From ship orders page, print label and navigate to tracking link and verify")
@allure.title("From ship orders page, print label and navigate to tracking link and verify")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_ship_orders_print_and_tracking():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Print label & open tracking"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 7
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Print consumer return label and email the label")
@allure.title("Print consumer return label and email the label")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_print_consumer_return_label_and_email():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Print & email return label"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 8
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Set New York card as default card for Single Payer Fedex for ShipOrder flow")
@allure.title("Set New York card as default card for Single Payer Fedex for ShipOrder flow")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_set_ny_default_card_for_fedex_shiporder():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Set NY default card (FedEx ShipOrder)"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 9
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("ShipOrders V2 – Import ShipOrders through file upload and verify automation rules are applied and print labels for the orders")
@allure.title("ShipOrders V2 – Import ShipOrders through file upload and verify automation rules are applied and print labels for the orders")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_shiporders_v2_import_and_print():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Import ShipOrders file & print"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 10
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Shopify – Print order and Verify Order number and Source in Shipping History")
@allure.title("Shopify – Print order and Verify Order number and Source in Shipping History")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_shopify_print_and_verify_in_history():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Print Shopify order & verify in history"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True

# 12
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Verify can't print labels for fileupload shiporders without automation rules")
@allure.title("Verify can't print labels for fileupload shiporders without automation rules")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_cant_print_without_rules_for_fileupload_orders():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Attempt print without rules"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 13
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Verify consumer return label created for WIX order in shipping history")
@allure.title("Verify consumer return label created for WIX order in shipping history")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_wix_return_label_in_history():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Ensure return label appears in history"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 14
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Verify designer page styles that we set are updated")
@allure.title("Verify designer page styles that we set are updated")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_designer_page_styles_updated():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Update designer styles & refresh"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 15
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Verify file upload ship order doesn't have email return link button in shipping history")
@allure.title("Verify file upload ship order doesn't have email return link button in shipping history")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_no_email_return_link_for_file_upload_order():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Check history entry for email return link"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 16
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Verify if we are able to set NY address credit card as default card for Single Payer Fedex")
@allure.title("Verify if we are able to set NY address credit card as default card for Single Payer Fedex")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_set_ny_default_card_for_fedex_general():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Set NY default card (general)"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 17
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Verify return address, policy description, policy url that was set in Return Settings page is applied")
@allure.title("Verify return address, policy description, policy url that was set in Return Settings page is applied")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_return_settings_applied():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Validate return address/policy on flow"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True


# 18
@allure.tag("Automation")
@allure.epic("Automation")
@allure.suite("ShipAccel Automation")
@allure.story("Verify we are able to email the returns link for the WIX order shipping transaction and able to access the page")
@allure.title("Verify we are able to email the returns link for the WIX order shipping transaction and able to access the page")
@allure.layer("Unit Tests")
@allure.label("owner", "Amir")
@allure.label("priority", "Medium")
@allure.label("product", "pitneyship")
@allure.label("product", "shipaccel")
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "Unit Tests")
@pytest.mark.ui
def test_email_returns_link_for_wix_order():
    with allure.step("Open application / preconditions"):
        assert True
    with allure.step("Execute scenario: Email returns link & open page"):
        assert True
    with allure.step("Validate expected behavior"):
        assert True
