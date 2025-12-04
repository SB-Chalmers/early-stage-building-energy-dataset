Synthetic dataset description
---------------------------

This folder contains synthetic training data used during development and testing. Files are CSVs where each row corresponds to a single building instance and columns include the architectural design variables and the target yearly energy demand in kWh.

Columns in `sample_synthetic.csv`:
- `shape_id`: Identifier for the generated shape (1..9 in the full dataset)
- `orientation`: Building orientation in degrees (0-360)
- `glazing_ratio`: Fraction of façade area that is glazing (0.0 - 1.0)
- `compactness`: Non-dimensional compactness metric
- `wall_u`: Wall U-value (W/m2K)
- `windows_u`: Window U-value (W/m2K)
- `insulation_thickness`: Insulation thickness (m)
- `yearly_energy_kwh`: Target variable - annual energy demand in kWh

For real experiments, generate a larger dataset using the Grasshopper script outputs and building energy simulation results. Keep datasets out of Git if they are large; instead store them in a data server or cloud storage and add download scripts here.
