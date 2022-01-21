from behave import given, when, then


@given('Open Gettop wishlist page')
def open_gettop_wishlist(context):
    context.app.wishlist_page.open_gettop_wishlist()


@then('Verify {expected_text} text is displayed')
def verify_expected_text_displays(context, expected_text):
    context.app.wishlist_page.verify_expected_text_displays(expected_text)


@then('Verify {expected_text} text is displayed on mobile')
def verify_expected_text_displays_mobile(context, expected_text):
    context.app.wishlist_page.verify_expected_text_displays_mobile(expected_text)
