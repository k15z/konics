#include "textures.inc"

    #declare White   = rgb 1;
    #declare Orange = color red 1 green 0.5 blue 0.0;
    #declare OrangeRed = color red 1.0 green 0.25; 
    #declare Asphalt = texture{
        pigment{color rgb<0.05,0.05,0.05>}
        normal {bumps 0.75 scale 0.015}
    }

    camera {
        perspective
        location <0, 8, 0>
        look_at  <0, 8, 1>
        right x
        up y
    }

    light_source {
        <0, 100, 0> color White
    }
    sphere{<0,0,0>,1 hollow
    texture{Shadow_Clouds}
     scale 10000
    }
    plane{ <0,1,0>, 0 
           texture{Asphalt}
     } // end of plane
    