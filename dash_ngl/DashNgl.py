# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashNgl(Component):
    """A DashNgl component.
Dash ngl component

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- data (dict; optional): Custom property. data has the following type: list of dicts containing keys 'filename', 'ext', 'config'.
Those keys have the following types:
  - filename (string; required)
  - ext (string; optional)
  - config (dict; optional): config has the following type: dict containing keys 'type', 'input'.
Those keys have the following types:
  - type (string; required)
  - input (list | dict | string; optional) | dict containing keys 'filename', 'ext', 'config'.
Those keys have the following types:
  - filename (string; required)
  - ext (string; optional)
  - config (dict; optional): config has the following type: dict containing keys 'type', 'input'.
Those keys have the following types:
  - type (string; required)
  - input (list | dict | string; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data']
        self._type = 'DashNgl'
        self._namespace = 'dash_ngl'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashNgl, self).__init__(**args)
