Synthetic dataset description
---------------------------

This folder contains synthetic training data used during development and testing. Files are CSVs where each row corresponds to a single building instance and columns include the architectural design variables and the target yearly energy demand in kWh/m2.

Columns in `sample_synthetic.csv`:
- `idf_name`: Identifier for the generated building configuration (shape type+index)
- `district_heating_demand_kwh`: district_heating_demand_kwh
- `total_building_area_m2`: total_building_area_m2
- `total_demand_kwh`: total_demand_kwh
- `normalised_district_demand_kwh_m2`: normalised_district_demand_kwh_m2
- `in:INDEX`: index for the configuration in the same shape type
- `out:BuildingArea`: building area for one floor
- `out:BuildingPerimeter`: perimeter of one floor
- 'out:CorridorArea': area of the unconditioned area, including corridor and vertical circulation area.
- 'out:CorriodrPerimeter': perimeter of the unconditioned area, including corridor and vertical circulation area.
- 'out:WWR': Window-to-wall ratio
- 'out:SHADING TYPE': 0: horozontal shading; 1: vertical shading; 2: combined shading
- 'out:STOREY NUMBER': number of stories
- 'out:ANGLE': building orientation
- 'out:storey height': height of each floor
- 'out:shading length': the length of shading device
- 'out:window height': the height of window
- 'out:WALL_U_VALUE':wall U value
- 'out:ROOF_U_VALUE':roof U value
- 'out:FLOOR_U_VALUE':floor U value
- 'out:ROOF_U_VALUE':roof U value
- 'out:WINDOW_U_VALUE': window u value
