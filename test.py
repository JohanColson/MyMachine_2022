# import board
# import neopixel
# pixels=neopixel.NeoPixel(board.D18, 198)
# red = (255,0,0)
# blue = (0,0,255)
# green = (0,255,0)
# off = (0,0,0)

# pixels[0] = (255,0,0)

# from time import sleep
# from neopixel import NeoPixel



# NUM_PIXELS = 198
# pixels = NeoPixel(pin=28,n=198, pixel_order="GRB")
# ColorsAR = (0x0080FF, 0xFFFFFF)
# NeoPixel()
# ColorsOFF = 0x000000
# DELAY = 1
# # #GPIO 10 voor de datapin
# yellow = (255,100,0)
# blue = (0,0,255)
# red = (255,0,0)
# green = (0,255,0)
# off = (0,0,0)

# pixels.brightness(80)
# pixels.fill(off)

# while True:
#     pixels.set_pixel_line(0,5,yellow)
#     sleep(1)
#     pixels.set_pixel_line(0,5,blue)
#     sleep(1)
#     pixels.set_pixel_line(0,5,red)
#     sleep(1)
#     pixels.set_pixel_line(0,5,green)
#     sleep(1)
#                     # GPIO.output(8, 1)
#         # if GPIO.input(11):
#         #     AR = vlc.MediaPlayer("Argentinië.mp3")
#         #     AR.play()            
#         #     for j in range(10):
#         #         for color in ColorsAR:
#         #             for i in range(6):
#         #                 pixels[i] = color
#         #                 pixels.show()
#         #                 sleep(DELAY)
#         #             pixels.fill(0)
#         # else:
#         #     for i in range(NUM_PIXELS):
#         #         pixels[i] = ColorsOFF
#         #         pixels.show()
                      
# # except KeyboardInterrupt:
# #     for i in range(NUM_PIXELS):
# #         pixels[i] = ColorsOFF
# #         pixels.show()
# #     spi.__exit__    
# #     GPIO.cleanup()         