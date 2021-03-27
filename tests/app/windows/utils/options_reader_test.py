import os

from app.windows.utils.options_reader import OptionsReader


def test_options_reader_get_options_works_properly():
    # GIVEN
    OptionsReader.OPTIONS_PATH = os.getcwd() + "/tests/sample_settings/options.json"

    # WHEN
    options = OptionsReader.get_options()

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
    OptionsReader.OPTIONS_PATH = os.getcwd() + "/tests/sample_settings/options_temp.json"
    sample_options = {"sample_id_1": {"state": "down"}, "sample_id_2": {"price": 10}}

    # WHEN
    OptionsReader.save_options(sample_options)
    # options should be saved by now.
    options = OptionsReader.get_options()

    # THEN
    assert options == sample_options
