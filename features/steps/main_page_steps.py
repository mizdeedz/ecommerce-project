from behave import given, when, then


@given('Open Gettop main page')
def open_gettop(context):
    context.app.main_page.open_main_page()


@when('Hover over the top banner')
def hover_over_top_banner(context):
    context.app.main_page.hover_over_top_banner()


@when('Click the right arrow icon')
def click_right_arrow(context):
    context.app.main_page.click_right_arrow()


@when('Click the left arrow icon')
def click_left_arrow(context):
    context.app.main_page.click_left_arrow()


@when('Click the bottom right dot')
def click_bottom_right_dot(context):
    context.app.main_page.click_bottom_right_dot()


@when('Click the bottom left dot')
def click_bottom_left_dot(context):
    context.app.main_page.click_bottom_left_dot()


@when('Swipe right on banner')
def swipe_right_banner(context):
    context.app.main_page.swipe_right_banner()


@when('Swipe left on banner')
def swipe_left_banner(context):
    context.app.main_page.swipe_left_banner()


@when('Store next product name')
def store_next_product_name(context):
    context.app.main_page.store_next_product_name()


@when('Store first product name')
def store_first_product_name(context):
    context.app.main_page.store_first_product_name()


@then('Verify different products were seen')
def verify_product_text(context):
    context.app.main_page.verify_product_text()


@then('User can click through banner links and verify correct page opens')
def verify_banner_link_clicks(context):
    context.app.main_page.verify_banner_link_clicks()


@then('User can tap through banner links and verify correct page opens')
def verify_mobile_banner_link_taps(context):
    context.app.main_page.verify_mobile_banner_link_taps()
