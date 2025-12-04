Grasshopper generation script
----------------------------

Place the Grasshopper file(s) used to generate the 9 building shapes in this folder. If you cannot commit the binary `.gh` file, include a `README` that documents the definition, inputs, and how to run it.

Suggested inputs to the Grasshopper definition:
- `shape_variation` - index to select one of 9 base shapes
- `width`, `depth`, `height` - primary dimensions
- `glazing_ratio` - glazing fraction per façade
- `orientation` - rotation angle in degrees

The script should output a CSV or JSON per shape containing the architectural design variables so they can be merged with energy simulation outputs.
