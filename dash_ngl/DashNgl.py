# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashNgl(Component):
    """A DashNgl component.
The NglMoleculeViewer is used to render schematic diagrams
of biomolecules in ribbon-structure representations.
Read more about the used WebGL protein viewer here:
https://github.com/arose/ngl

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components in callbacks.
The ID needs to be unique across all of the components in an app.
- viewportStyle (dict; default {
  width: '500x',
  height: '500px'
}): The height and the width (in px) of the container
in which the molecules will be displayed.
Default: width:1000px / height:500px
It should be in JSON format. viewportStyle has the following type: dict containing keys 'width', 'height'.
Those keys have the following types:
  - width (string; optional)
  - height (string; optional)
- stageParameters (dict; default {
  quality: 'medium',
  backgroundColor: 'white',
  cameraType: 'perspective'
}): Parameters (in JSON format) for the stage object of ngl.
Currently implemented are the quality of the visualisation
and the background colorFor a full list see:
http://nglviewer.org/ngl/api/file/src/stage/stage.js.html. stageParameters has the following type: dict containing keys 'quality', 'backgroundColor', 'cameraType'.
Those keys have the following types:
  - quality (string; optional)
  - backgroundColor (string; optional)
  - cameraType (string; optional)
- imageParameters (dict; default {
  antialias: true,
  transparent: true,
  trim: true
}): Parameters (in JSON format) for exporting the image. imageParameters has the following type: dict containing keys 'antialias', 'transparent', 'trim'.
Those keys have the following types:
  - antialias (boolean; optional)
  - transparent (boolean; optional)
  - trim (boolean; optional)
- downloadImage (boolean; optional): flag if download image was pressed
- pdbString (string; optional): Variable which defines how many molecules should be shown and/or which chain
The following format needs to be used:
pdbID1.chain:start-end_pdbID2.chain:start-end
. indicates that only one chain should be shown
: indicates that a specific range should be shown (e.g. 1-50)
 _ indicates that more than one protein should be shown
- data (dict; default [{
  uploaded: true,
  selectedValue: 'placeholder',
  resetView: false,
  chain: 'ALL',
  range: 'ALL',
  color: 'red',
  filename: 'placeholder',
  ext: '',
  config: {
    type: 'text/plain',
    input: ''
  }
}]): The data (in JSON format) that will be used to display the molecule
filename: name of the used pdb/cif file
ext: file extensions (pdb or cif)
selectedValue: pdbString
molStyles: selected molecule representation (cartoon, stick, sphere)
chain: selected chain
range: selected range
color: color in hex format
config.input: content of the pdb file
config.type: format of config.input
resetView: bool if the view should be resettet
uploaded: bool if the file was uploaded. data has the following type: list of dicts containing keys 'filename', 'ext', 'selectedValue', 'chain', 'range', 'color', 'config', 'resetView', 'uploaded'.
Those keys have the following types:
  - filename (string; required)
  - ext (string; required)
  - selectedValue (string; required)
  - chain (string; required)
  - range (string; required)
  - color (string; required)
  - config (dict; optional): config has the following type: dict containing keys 'type', 'input'.
Those keys have the following types:
  - type (string; required)
  - input (string; required)
  - resetView (boolean; required)
  - uploaded (boolean; required)
- molStyles (list of strings; default 'cartoon'): Variable for changing the molecule representation
Selection of possible molecule styles:
    'ball+stick','cartoon','licorice',
    'line','ribbon','rope','spacefill',
    'surface','trace','tube'"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, viewportStyle=Component.UNDEFINED, stageParameters=Component.UNDEFINED, imageParameters=Component.UNDEFINED, downloadImage=Component.UNDEFINED, pdbString=Component.UNDEFINED, data=Component.UNDEFINED, molStyles=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'viewportStyle', 'stageParameters', 'imageParameters', 'downloadImage', 'pdbString', 'data', 'molStyles']
        self._type = 'DashNgl'
        self._namespace = 'dash_ngl'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'viewportStyle', 'stageParameters', 'imageParameters', 'downloadImage', 'pdbString', 'data', 'molStyles']
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
