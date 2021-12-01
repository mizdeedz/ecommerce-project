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


@when('Store product name')
def store_product_name(context):
    context.app.main_page.store_product_name()


@then('Verify different products were seen')
def verify_product_text(context):
    context.app.main_page.verify_product_text()
