import requests

def after_scenario(context, scenario):
    if "tag_name" in scenario.tags:
        pass
