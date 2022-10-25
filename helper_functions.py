def calculate_wbgt(wet_bulb_temp, globe_temp, dry_bulb_temp):
	return 0.7 * wet_bulb_temp + 0.2 * globe_temp + 0.1 * dry_bulb_temp
