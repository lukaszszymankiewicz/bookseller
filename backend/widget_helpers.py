class WidgetInspector:
    """Helper class for better iteating through kivy widgets."""

    def __init__(self):
        pass

    def filter_widgets_by_attribute(self, widgets: dict, attribute: str) -> dict:
        """
        Iterates through all widgets inputted, filter only those widgets which have certain flag (in
        case of Kivy widgets this flag is set by having some attribute) and state od this attribute
        is stored.

        Please note that this function allows only ONE particular attribute to be stored. More
        detailed function is not implemented.

        Args:
            widgets: dict containing ids and wigets object,
            attribute: string representing name of attribute to be stored,

        Return:
            Dict containing widgets name and inputted attribute value.

            Example returned dict (with inputted attribute 'color'):

            {
                "widget_1": {"color": "black"},
                "widget_2": {"color": "green"},
                "widget_3": {"color": "white"},
            }
        """
        widgets_states = {}

        for name, widget in widgets.items():
            if hasattr(widget, attribute) and getattr(widget, attribute) != "":
                attrname = getattr(widget, attribute)
                attrvalue = getattr(widget, attrname)
                widgets_states[name] = {attrname: attrvalue}

        return widgets_states

    def set_widgets_default_values(self, widgets: dict) -> None:
        """
        Iterates through inputted widgets, checks for its default values and sets it.

        Default values are defined on kivy lang level.

        Args:
            widgets - dict containing widgets ids ads keys and widgets data (as values).
        """
        for name, widget in widgets.items():
            if hasattr(widget, "default") and getattr(widget, "default") != {}:
                state = getattr(widget, "default")
                for key, value in state.items():
                    setattr(widget, key, value)

    # TODO: add some simple validation if ANY of the option is save wrong!
    # TODO: and I demand unit test for such situation!
    def set_widgets_values(self, widgets: dict, data: dict) -> None:
        """
        Iterates through inputted widgets, and sets values equal to inputted values.

        Args:
            widgets - dict containing widgets ids ads keys and widgets data (as values),
            data - values to be set on widgets.
        """
        for widget_id, settings in data.items():
            for setting, value in settings.items():
                if hasattr(widgets[widget_id], setting):
                    setattr(widgets[widget_id], setting, value)
