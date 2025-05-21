def before_all(context):
    # Setup any global test configuration here
    pass

def after_all(context):
    # Cleanup after all tests are done
    pass

def before_feature(context, feature):
    # Setup before each feature
    pass

def after_feature(context, feature):
    # Cleanup after each feature
    pass

def before_scenario(context, scenario):
    # Setup before each scenario
    pass

def after_scenario(context, scenario):
    # Cleanup after each scenario
    if hasattr(context, 'driver'):
        context.driver.quit() 