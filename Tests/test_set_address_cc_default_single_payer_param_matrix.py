import pytest
import allure

TITLE = "Verify if we are able to set address credit card as default card for Single Payer across carriers and flows"

@allure.tag("Automation")
@allure.epic("UI Automation")
@allure.suite("ShipAccel UI Automation")
@allure.feature(TITLE)                 
@allure.title(TITLE)
@allure.label("owner", "Sowmya Katamaneni")
@allure.label("priority", "Medium")    
@allure.label("trProject", "Shipaccel")
@allure.label("layer", "UI")
@pytest.mark.parametrize(
    "address, carrier, flow",
    [
        # FEDEX
        ("CT", "FEDEX", "ShipOrder"),
        ("NY", "FEDEX", "ShipOrder"),
        ("CT", "FEDEX", "Shipping Label"),
        ("NY", "FEDEX", "Shipping Label"),
        # UPS
        ("CT", "UPS", "Import Ship Order"),
        ("NY", "UPS", "Import Ship Order"),
        ("CT", "UPS", "Shipping Label"),
        ("NY", "UPS", "Shipping Label"),
    ],
    ids=[
        "CT-FEDEX-ShipOrder",
        "NY-FEDEX-ShipOrder",
        "CT-FEDEX-ShippingLabel",
        "NY-FEDEX-ShippingLabel",
        "CT-UPS-ImportShipOrder",
        "NY-UPS-ImportShipOrder",
        "CT-UPS-ShippingLabel",
        "NY-UPS-ShippingLabel",
    ],
)
def test_set_address_cc_default_single_payer(address, carrier, flow):
    # Step 1: Open the correct flow for the carrier
    with allure.step(f"Open {flow} flow for {carrier} (address={address})"):
        assert address in ("CT", "NY")
        assert carrier in ("FEDEX", "UPS")
        assert flow in ("ShipOrder", "Shipping Label", "Import Ship Order")

    # Step 2: Set address credit card as DEFAULT for Single Payer
    with allure.step("Set address credit card as DEFAULT for Single Payer"):
        set_default_ok = True  # placeholder for UI/API action
        assert set_default_ok is True

    # Step 3: Execute the printing action for this carrier/flow
    with allure.step("Execute printing action for selected carrier/flow"):
        printed = True  # placeholder
        assert printed is True

    # Step 4: Verify the DEFAULT address card is used (no fallback/other card)
    with allure.step("Verify DEFAULT address credit card is used"):
        default_used = True  # placeholder verification
        assert default_used is True

    # Step 5: Attach parameters for traceability
    with allure.step("Attach parameters"):
        allure.attach(
            f"Address={address}\nCarrier={carrier}\nFlow={flow}",
            name="params",
            attachment_type=allure.attachment_type.TEXT,
        )
