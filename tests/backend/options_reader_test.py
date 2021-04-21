import os

from backend.options_reader import OptionsReader


def test_options_reader_get_options_works_properly():
    # GIVEN
    options_reader = OptionsReader()
    options_reader.OPTIONS_PATH = os.getcwd() + "/tests/sample_settings/options.json"

    # WHEN
    options = options_reader.get_options()

    # THEN
    assert options
    assert isinstance(options, dict)

    for name, settings in options.items():
        assert isinstance(name, str)
        assert isinstance(settings, dict)

        for name, setting in settings.items():
            assert isinstance(name, str)
            assert settings is not None


def test_options_reader_save_options_works_propely():
    # GIVEN
    options_reader = OptionsReader()
    options_reader.OPTIONS_PATH = os.getcwd() + "/tests/sample_settings/options_temp.json"
    widgets_state = {"sample_id_1": {"state": "down"}, "sample_id_2": {"price": 10}}

    # WHEN
    options_reader.save_options(widgets_state)
    # options should be saved by now.
    options = options_reader.get_options()

    # THEN
    assert options == widgets_state
