"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import math
import bullet

class TestBulletSetters( unittest.TestCase ):

    def setUp( self ):
        initial_x = 11
        initial_y = 22
        initial_dx = 11
        initial_dy = 22
        self.expected_rotation = 45
        self.expected_radius = 3
        self.expected_world_width = 600
        self.expected_world_height = 800
        self.expected_color = ( 255, 255, 255 )
        self.expected_age = 0
        
        self.expected_dx = initial_dx + 100. * math.cos( math.radians( self.expected_rotation ) )
        self.expected_dy = initial_dy + 100. * math.sin( math.radians( self.expected_rotation ) )
        
        self.expected_x = initial_x + 0.1 * self.expected_dx
        self.expected_y = initial_y + 0.1 * self.expected_dy
        
        self.constructed_obj = bullet.Bullet( initial_x, initial_y, initial_dx, initial_dy, self.expected_rotation, self.expected_world_width, self.expected_world_height )
        
        return

    def tearDown( self ):
        return

    def test001_SetsAge( self ):
        new_age = 3.14
        self.constructed_obj.setAge( new_age )
        self.assertEqual( self.constructed_obj.getAge( ), new_age )
        return
    
 
def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestBulletSetters )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )
