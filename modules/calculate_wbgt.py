def calculate_wbgt(sensors):
	return 0.7 * sensors['wet_bulb_sensor'] + 0.2 * sensors['globe_sensor'] + 0.1 * sensors['dry_bulb_sensor']
