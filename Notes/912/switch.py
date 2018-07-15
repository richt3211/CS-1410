class Port:

	def __init__(self, port_number, bytes_in, bytes_out, error):
		self.mErrorCount = error
		self.mBytesOut = bytes_out
		self.mBytesIn = bytes_in
		self.mPortsNumber = port_number

		return