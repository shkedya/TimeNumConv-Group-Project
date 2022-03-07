import unittest
from task import conv_num


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test_conv_num1(self):
        """Testing a regular integer"""
        num_str = "123"
        expected = 123
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num2(self):
        """Testing a negative integer"""
        num_str = "-123"
        expected = -123
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num3(self):
        """Testing a regular float"""
        num_str = "12.13"
        expected = 12.13
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num4(self):
        """Testing another regular float"""
        num_str = "123.455"
        expected = 123.455
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num5(self):
        """Testing a float with no 0 before the decimal"""
        num_str = ".45"
        expected = 0.45
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num6(self):
        """Testing a negative float"""
        num_str = "-123.45"
        expected = -123.45
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num7(self):
        """Testing a float with no number after the decimal"""
        num_str = "123."
        expected = 123.0
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num8(self):
        """Testing a hexadecimal"""
        num_str = "0xAD4"
        expected = 2772
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num9(self):
        """Testing a negative hexadecimal"""
        num_str = "-0xAD4"
        expected = -2772
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num10(self):
        """Testing a hexadecimal that's all uppercase"""
        num_str = "0XAD4"
        expected = 2772
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num11(self):
        """Testing a hexadecimal that's negative and uppercase"""
        num_str = "-0XAD4"
        expected = -2772
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num12(self):
        """Testing a hexadecimal that's all lowercase"""
        num_str = "0xad4"
        expected = 2772
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num13(self):
        """Testing a negative lowercase hexadecimal"""
        num_str = "-0xad4"
        expected = -2772
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num14(self):
        """Testing an invalid hexadecimal"""
        num_str = "0xAZ4"
        expected = None
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num15(self):
        """Testing a hexadecimal with too many prefixes"""
        num_str = "0x0xAD4"
        expected = None
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num16(self):
        """Testing a hexadecimal with a decimal point"""
        num_str = "0xAD4.45"
        expected = None
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num17(self):
        """Testing a float with too many decimals"""
        num_str = "45.55.555.5"
        expected = None
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num18(self):
        """Testing an empty string"""
        num_str = ""
        expected = None
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))

    def test_conv_num19(self):
        """Testing a full sentence"""
        num_str = "Hello, this is the 19th test!"
        expected = None
        self.assertEqual(conv_num(num_str), expected, msg='conv_num({})'.format(num_str))


if __name__ == '__main__':
    unittest.main()
