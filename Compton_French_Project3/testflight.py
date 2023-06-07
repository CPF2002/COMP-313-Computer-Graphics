import bpy
import math
'''
Sites and Videos used: 
https://polyhaven.com/a/scythian_tombs
https://www.youtube.com/watch?v=uT127TSmBwU&ab_channel=5MinutesBlender
https://www.youtube.com/watch?v=mM3M1Vj6DxQ&ab_channel=DeepakGraphics
https://www.youtube.com/watch?v=FZFs6Bad0lk&ab_channel=PolygonRunway
https://gamedevtraum.com/en/blender-tutorials-and-curiosities/how-to-change-the-skybox-in-blender-make-a-custom-sky-with-an-hdr-texture/

scythian_tombs_4k.exr is the world background file

Sample 1 : 15 sec ; plane striaght ; camera moving around behind
Sample 2 : ~20 sec ; plane fly up, slow twisting, fly down ; camera behind not moving as much as sample 1
Sample 3 : basically sample 2, but with a stall at the top of the curve
Sample 4 : on the fall down, rapid twwisting then stop twist and smooth curve at 90 degree angle
Sample 5 : 

Notes : 
    for 2 and 3 deselerate approaching top
    dont necessarily want the camera rotationg with the plane
    
    Camera 2 from frame 0-120
    Camera 3 from 120-192 for 180 turn
    Camera 4 from 192-504 to watch under and spin down
    Camera 2 from 504-600
    Camera 3 from 600-888 following behind
    End with cockpit camera

'''
# Initialize lists of tuples
#           /Sample 1 : straight flight                                        /right turn                   /straight     /curve up                                       /stright up                                                       /curve down     /start fall down with small angle                          /start right turn                    /stright small angle up                                          /climb up again /twist 90 left                       /backflip                                   /aggressive spiral down                     STOP                                             /make turn back to land                                                   /straight
positions = (0, 0, 1), (0, 20, 3), (0, 35, 17), (0, 60, 20), (0, 80, 20), (0, 105, 20), (30, 130, 20), (60, 105, 20), (60, 80, 20),   (60, 70, 25),    (60, 65, 35),    (60, 60, 55),    (60, 60, 80),    (60, 60, 92),    (60, 60, 100),   (60, 56, 104),  (60, 56, 95), (60, 56, 80), (60, 45, 60),   (60, 35, 40),   (55, 27, 25),    (45, 20, 20),  (30, 15, 20),   (15, 15, 25),   (0, 15, 30),    (-15, 15, 35),  (-30, 15, 40),   (-45, 15, 50),     (-55, 15, 65),     (-55, 15, 80),     (-55, 15, 90),     (-55, 20, 95),     (-55, 25, 90),     (-55, 15, 70),     (-55, 5, 50),      (-55, -5, 30),     (-55, -20, 15),     (-55, -40, 7),     (-55, -70, 5),    (-37, -90, 5),      (-17, -90, 5),     (0, -70, 5),       (0, -55, 4),       (0, -40, 3),       (0, -30, 2.5),     (0, -20, 2.5),     (0, -12, 2),       (0, -4, 1.5),      (0, 0, 1)
# Spins:                                                                                                                                                                      ------------------small twists------------------                 ---------be upright for apex------                                                                             ---------------crazy twisting------------------STOP
rotations = (90,0,180),(75,0,180), (90,0, 180), (90,0, 180), (90,0, 180), (90, 0, 180), (0, -90, 180), (-90,-180,180),(-120,-180,180),(-135,-180,180), (-155,-180,180), (-180,-180,180), (-180,-180,180), (-180,-180,180), (-155,-180,180), (-90,-180,180), (0,-180,180), (0,-180,540), (-20,-180,900), (-20,-180,900), (-90,-140,900), (-90,-180,820), (-98,-180,810), (-98,-180,810), (-98,-180,810), (-98,-180,810), (-150,-180,810), (-180, -180, 900), (-180, -180, 600), (-180, -180, 300), (-210, -180, 180), (-270, -180, 180), (-380, -180, 180), (-380, -180, 180), (-380, -180, 180), (-405, -180, 180), (-420, -180, 180), (-445, -180, 180), (-445, -180, 215), (-445, -275, 265),  (-445, -275, 265), (-450, -180, 360), (-450, -180, 360), (-450, -180, 360), (-450, -180, 360), (-450, -180, 360), (-450, -180, 360), (-450, -180, 360), (-450, -180, 360)

# positions_cam stays because child of plane
positions_cam = (0,8.11,1.69)
positions_cam_fly_1 = (9,-6,1)
positions_smoke = (0, -1.1, 1)
rotation_cam_fly_1 = (math.radians(90), math.radians(0), math.radians(60))

#Frames:                  0                          48                        96                        144                      192                             240                               288                                336                            384                          432                            480                            528                                576         #Frame 600 (-15,15,35)                               672                                                         744                                                        816                                                       # Frame 888 (-55, -40, 7)
positions_cam_fly_2 = (30,105,20), (30,105,20), (30,105,20), (30,105,20), (30,105,20), (30,105,20), (30,105,20), (30,105,20), (30,105,20),   (30,105,20),     (30,105,20),     (30,105,20),     (30,105,20),     (30,105,20),     (30,105,20),    (30,105,20),   (30,105,20),  (30,105,20),  (30,105,20),    (30,105,20),    (30,105,20),      (30,105,20),  (30,105,20),    (30,105,20),      (-45, -5, 50),  (-45, -5, 50),  (-45, -5, 50),   (-45, -5, 50),     (-55, -5, 65),     (-55, -5, 80),     (-45, -5, 80),     (-45, -5, 80),     (-45, -5, 80),     (-45, -5, 80),     (-45, -5, 80),      (-47.38, -5, 43.26),    (-46, -5, 28),     (-46, -14, 20),    (-46, -14, 20),    (-46, -14, 20),      (-46, -14, 20),     (-46, -14, 20),       (-46, -14, 20),       (-46, -14, 20),       (-46, -14, 20),     (-46, -14, 20),     (-46, -14, 20),       (-46, -14, 20),      (-46, -14, 20)
rotations_cam_fly_2 = (90,0,100),  (90,0,100),  (90,0,100),  (90,0,100),  (90,0,100),  (90,0,100),  (90,0,0),    (90,0,-95),  (90,0,-125),   (90,0,100),      (90,0,100),      (90,0,100),      (90,0,100),      (90,0,100),      (90,0,100),      (90,0,100),     (90,0,100),   (90,0,100),   (90,0,100),     (90,0,100),     (90,0,100),      (90,0,100),    (90,0,100),     (90,0,100),     (90,0,100),     (67,0,306),     (67,0,329),      (90,0,360),        (90,0,360),        (90,0,360),        (109,0,386),       (118,0,381),       (107,0,376),        (68,0,385),        (-5,-20,512),        (30.5,-10,466),        (50.5,0,507),      (61,0,517),        (61,0,517),        (61,0,517),          (61,0,517),         (61,0,517),           (61,0,517),           (61,0,517),           (61,0,517),         (61,0,517),         (61,0,517),           (61,0,517),          (61,0,517)

positions_cam_fly_3 = (30,105,20), (30,105,20), (30,105,20), (30,105,20), (30,105,20), (30,105,20), (30,105,20), (56,68,26),  (56,68,26),    (57,64,42),      (57,59,51),      (57,54,71),      (53,54,99),      (50,54,110),     (50,54,110),    (50,54,110),   (50,54,110),  (50,54,110),  (50,54,85),     (50,54,65),     (50,54,65),       (50,154,65),  (50,154,65),    (30,105,20),      (-45, -5, 50),  (-45, -5, 50),  (-45, -5, 50),   (-45, -5, 50),     (-55, -5, 65),     (-55, -5, 80),     (-45, -5, 80),     (-45, -5, 80),     (-45, -5, 80),     (-45, -5, 80),     (-45, -5, 80),      (-47.38, -5, 43.26),    (-46, -5, 28),     (-46, -14, 20),    (-46, -14, 20),    (-46, -14, 20),      (-46, -14, 20),     (-46, -14, 20),       (-46, -14, 20),       (-46, -14, 20),       (-46, -14, 20),     (-46, -14, 20),     (-46, -14, 20),       (-46, -14, 20),      (-46, -14, 20)
rotations_cam_fly_3 = (90,0,100),  (90,0,100),  (90,0,100),  (90,0,100),  (90,0,100),  (90,0,100),  (90,0,0),    (66,0,-16),  (66,0,-16),    (22,0,-23),      (22,0,-23),      (22,0,-23),      (24,0,-39),      (36,0,-61),      (48,0,-61),      (58,0,-71),     (35,0,-76),   (27,0,-80),   (27,0,-123),    (42,0,-145),    (30,0,-169),     (35,0,-180),    (35,0,-180),     (90,0,100),     (90,0,100),     (67,0,306),     (67,0,329),      (90,0,360),        (90,0,360),        (90,0,360),        (109,0,386),       (118,0,381),       (107,0,376),        (68,0,385),        (6,-10,512),        (30.5,-10,466),        (50.5,0,507),      (61,0,517),        (61,0,517),        (61,0,517),          (61,0,517),         (61,0,517),           (61,0,517),           (61,0,517),           (61,0,517),         (61,0,517),         (61,0,517),           (61,0,517),          (61,0,517)

# Initialize object references
# bpy.ops.anim.keyframe_clear_v3d() clears all key frame data
plane = bpy.data.objects["plane"]
bpy.ops.anim.keyframe_clear_v3d()
camera = bpy.data.objects["Camera1"]
bpy.ops.anim.keyframe_clear_v3d()
camera_fly_1 = bpy.data.objects["Camera2"]
bpy.ops.anim.keyframe_clear_v3d()
camera_fly_2 = bpy.data.objects["Camera3"]
bpy.ops.anim.keyframe_clear_v3d()
camera_fly_3 = bpy.data.objects["Camera4"]
bpy.ops.anim.keyframe_clear_v3d()
propeller = bpy.data.objects["propeller"]
bpy.ops.anim.keyframe_clear_v3d()
smoke = bpy.data.objects["Smoke"]
bpy.ops.anim.keyframe_clear_v3d()
smoke_domain = bpy.data.objects["Smoke Domain"]
bpy.ops.anim.keyframe_clear_v3d()


# Declare function
def set_keyframes():
    # set frame number and the increments for each key frame
    frame_num = 0
    keyframe_increment = 24
    
    for index, position in enumerate(positions):
        # Goes to the next keyframe
        bpy.context.scene.frame_set(frame_num)
        
        # Plane
        plane.location = position
        plane.rotation_euler = (math.radians(rotations[index][0]), math.radians(rotations[index][1]), math.radians(rotations[index][2]))
        plane.keyframe_insert(data_path='location', index=-1)
        plane.keyframe_insert(data_path='rotation_euler', index=-1)
        # camera fly follows rotation
        
        # Propeller is always rotating on the y-axis
        # Rotates 360 every keyframe
        propeller.rotation_euler = (math.radians(90), math.radians(360 * index), (math.radians(0)))
        propeller.keyframe_insert(data_path='rotation_euler', index=-1)
        
        # Smoke and Smoke Domain
        # Smoke Domain is a child of smoke, which is a child of plane
        smoke.location = positions_smoke
        smoke.keyframe_insert(data_path='location', index=-1)
        smoke.keyframe_insert(data_path='rotation_euler', index=-1)
        
        # Camera 1
        # Child of plane ; in cockpit
        # Frames 888-1152
        camera.location = positions_cam
        camera.keyframe_insert(data_path='rotation_euler', index=-1)
        
        # Camera 2
        # Child of plane ; following behind to right
        # Frames 0-120 ; 504-600
        camera_fly_1.location = positions_cam_fly_1  #find way to make follow behind it
        camera_fly_1.rotation_euler = rotation_cam_fly_1
        
        # Camera 3
        # Frames 120-192 ; 600-888
        camera_fly_2.location = (positions_cam_fly_2[index][0], positions_cam_fly_2[index][1], positions_cam_fly_2[index][2])
        camera_fly_2.keyframe_insert(data_path='location', index=-1)
        camera_fly_2.rotation_euler = (math.radians(rotations_cam_fly_2[index][0]), math.radians(rotations_cam_fly_2[index][1]), math.radians(rotations_cam_fly_2[index][2]))
        camera_fly_2.keyframe_insert(data_path='rotation_euler', index=-1)

        # Camera 4
        # Frames 192-504
        camera_fly_3.location = (positions_cam_fly_3[index][0], positions_cam_fly_3[index][1], positions_cam_fly_3[index][2])
        camera_fly_3.keyframe_insert(data_path='location', index=-1)
        camera_fly_3.rotation_euler = (math.radians(rotations_cam_fly_3[index][0]), math.radians(rotations_cam_fly_3[index][1]), math.radians(rotations_cam_fly_3[index][2]))
        camera_fly_3.keyframe_insert(data_path='rotation_euler', index=-1)

        # Keyframe increment
        frame_num += keyframe_increment
        
    # end of loop sets the length of frames
    bpy.data.scenes[0].frame_end = frame_num - keyframe_increment
        
    pass

def main():
    set_keyframes()
    pass
    
main()
