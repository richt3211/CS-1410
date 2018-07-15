import switch

def main():
	#assume this is extracted from the log file
	errors = 2
	bytes_in= 11232123
	bytes_out = 1234
	port_number = 1


	p01 = switch.Port( port_number, bytes_in, bytes_out, errors)

