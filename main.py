from nanoleafapi import Nanoleaf
import os.path
import pathlib
import config
import argparse


def setup(config_file_path: str = "config.json") -> (Nanoleaf, dict):
    # Check config exists
    if not os.path.exists(config_file_path):
        config.create_config(config_file_path)

    # Load config and prompt for missing data
    config_data = config.load_config(config_file_path)
    if config_data["nanoleafIP"] is None:
        print(f"No value set for nanoleafIP")
        value = input(f"Enter value for nanoleafIP: ")
        config.update_config(config_file_path, "nanoleafIP", value)
    config_data = config.load_config(config_file_path)

    nl = Nanoleaf(config_data["nanoleafIP"])
    return nl, config_data


if __name__ == '__main__':
    config_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "config.json")
    nanoleaf, config_data = setup(config_path)
    parser = argparse.ArgumentParser()
    parser.add_argument("effect", help="The scene to set the panels to - solid effects should be configured in the JSON")
    args = parser.parse_args()

    effect = args.effect

    if effect in nanoleaf.list_effects():
        nanoleaf.set_effect(effect)
    elif effect in config_data["effects"].keys():
        effect_data = config_data["effects"][effect]
        nanoleaf.set_color((
            effect_data["red"],
            effect_data["green"],
            effect_data["blue"]
        ))
        nanoleaf.set_brightness(effect_data["brightness"], 1)
    elif effect.lower() == "off":
        nanoleaf.power_off()
    elif effect.lower() == "on":
        nanoleaf.power_on()
    else:
        raise ValueError("Unknown effect name: " + effect)
