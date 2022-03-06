def on_received_string(receivedString):
    radio.send_value(receivedString,
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER))
radio.on_received_string(on_received_string)

已用时间 = 0
radio.set_group(220)
strip = neopixel.create(DigitalPin.P2, 1, NeoPixelMode.RGB)

def on_forever():
    global 已用时间
    strip.clear()
    basic.show_icon(IconNames.HEART)
    basic.pause(2000)
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    music.play_tone(494, music.beat(BeatFraction.QUARTER))
    basic.show_leds("""
        # # # # #
                # . . . .
                # # # # #
                . . . . #
                # # # # #
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    basic.show_leds("""
        . . . # .
                . . # # .
                . # . # .
                # # # # #
                . . . # .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    basic.show_leds("""
        # # # # #
                . . . . #
                # # # # #
                . . . . #
                # # # # #
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    basic.show_leds("""
        # # # # #
                . . . . #
                # # # # #
                # . . . .
                # # # # #
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    basic.show_leds("""
        . . # . .
                . # # . .
                # . # . .
                . . # . .
                # # # # #
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    music.play_tone(494, music.beat(BeatFraction.QUARTER))
    basic.show_leds("""
        # # # # #
                # . . . .
                # # # # #
                . . . . #
                # # # # #
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    basic.show_leds("""
        . . . # .
                . . # # .
                . # . # .
                # # # # #
                . . . # .
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    basic.show_leds("""
        # # # # #
                . . . . #
                # # # # #
                . . . . #
                # # # # #
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    basic.show_leds("""
        # # # # #
                . . . . #
                # # # # #
                # . . . .
                # # # # #
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    basic.show_leds("""
        . . # . .
                . # # . .
                # . # . .
                . . # . .
                # # # # #
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
    if radio.received_packet(RadioPacketProperty.SERIAL_NUMBER) == 2:
        for index in range(20):
            basic.pause(1000)
            已用时间 += 1
    else:
        if radio.received_packet(RadioPacketProperty.SERIAL_NUMBER) == 1:
            if 45 / 5 <= 20 - 已用时间:
                radio.send_number(3)
            elif 20 - 已用时间 >= 45 / 15:
                radio.send_number(4)
            else:
                radio.send_number(5)
basic.forever(on_forever)
