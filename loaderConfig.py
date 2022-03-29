import yaml

def get_exchange_config():

    with open("exchange-config.yaml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg