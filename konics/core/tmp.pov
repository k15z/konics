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
        location <0, 8, -10>
        look_at  <0, 8, 100>
        right x
        up y
    }

    light_source {
        <0, 100, 0> color White
    }
    sphere{<0,0,0>,1 hollow
    texture{FBM_Clouds}
     scale 10000
    }
    plane{ <0,1,0>, 0 
           texture{Brown_Agate}
     } // end of plane
    cone {
                <-10, 4, 0>, 0.1
                <-10, 0, 0>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <10, 4, 0>, 0.1
                <10, 0, 0>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <-10, 4, 20>, 0.1
                <-10, 0, 20>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <10, 4, 20>, 0.1
                <10, 0, 20>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <-10, 4, 40>, 0.1
                <-10, 0, 40>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <10, 4, 40>, 0.1
                <10, 0, 40>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <-10, 4, 60>, 0.1
                <-10, 0, 60>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <10, 4, 60>, 0.1
                <10, 0, 60>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <-10, 4, 80>, 0.1
                <-10, 0, 80>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <10, 4, 80>, 0.1
                <10, 0, 80>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <-10, 4, 100>, 0.1
                <-10, 0, 100>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <10, 4, 100>, 0.1
                <10, 0, 100>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <-10, 4, 120>, 0.1
                <-10, 0, 120>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <10, 4, 120>, 0.1
                <10, 0, 120>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <-10, 4, 140>, 0.1
                <-10, 0, 140>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <10, 4, 140>, 0.1
                <10, 0, 140>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <-10, 4, 160>, 0.1
                <-10, 0, 160>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <10, 4, 160>, 0.1
                <10, 0, 160>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <-10, 4, 180>, 0.1
                <-10, 0, 180>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <10, 4, 180>, 0.1
                <10, 0, 180>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <-13.0, 0, 40.0>, 0.1
                <-17.0, 1, 40.0>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }cone {
                <13.0, 0, 40.0>, 0.1
                <17.0, 1, 40.0>, 1.0
                texture { 
                    finish { ambient Orange }
                    pigment { color OrangeRed }
                }
            }