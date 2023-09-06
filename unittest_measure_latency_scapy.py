import unittest
from unittest.mock import patch
from module_scapy_measure_latency import scapy_measure_latency

class TestLatencyMeasurement(unittest.TestCase):
    
    # @patch('module_latency_measurement.ping_with_options')
    # @patch('module_latency_measurement.get_round_trip_time')
    #def test_successful_latency_measurement(self, mock_get_round_trip_time, mock_ping_with_options):
    def test_successful_latency_measurement(self):
        # mock_ping_with_options.return_value = "mocked_ping_output"
        # mock_get_round_trip_time.return_value = 50.0
        
        # Test input
        addr = '8.8.8.8'
        pkts2send = 5
        pktsize = 64
        ttl = 128
        interval = 1
        timeout = 2
        IP_v = 4
        latency  = scapy_measure_latency(addr, pkts2send, pktsize, ttl, interval, timeout, IP_v)
        
        # Test for all packets 
        for x in latency:
            self.assertIsNotNone(x)
            self.assertGreaterEqual(x, 0.0)
            #self.assertIsInstance(x, float)

if __name__=='__main__':
    unittest.main()

