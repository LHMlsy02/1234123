radio.onReceivedString(function (receivedString) {
    radio.sendValue(receivedString, radio.receivedPacket(RadioPacketProperty.SerialNumber))
})
let 已用时间 = 0
radio.setGroup(220)
let strip = neopixel.create(DigitalPin.P2, 1, NeoPixelMode.RGB)
basic.forever(function () {
    strip.clear()
    basic.showIcon(IconNames.Heart)
    basic.pause(2000)
    strip.showColor(neopixel.colors(NeoPixelColors.Red))
    music.playTone(494, music.beat(BeatFraction.Quarter))
    basic.showLeds(`
        # # # # #
        # . . . .
        # # # # #
        . . . . #
        # # # # #
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    music.playTone(440, music.beat(BeatFraction.Quarter))
    basic.showLeds(`
        . . . # .
        . . # # .
        . # . # .
        # # # # #
        . . . # .
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    music.playTone(440, music.beat(BeatFraction.Quarter))
    basic.showLeds(`
        # # # # #
        . . . . #
        # # # # #
        . . . . #
        # # # # #
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    music.playTone(440, music.beat(BeatFraction.Quarter))
    basic.showLeds(`
        # # # # #
        . . . . #
        # # # # #
        # . . . .
        # # # # #
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    music.playTone(440, music.beat(BeatFraction.Quarter))
    basic.showLeds(`
        . . # . .
        . # # . .
        # . # . .
        . . # . .
        # # # # #
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    strip.showColor(neopixel.colors(NeoPixelColors.Green))
    music.playTone(494, music.beat(BeatFraction.Quarter))
    basic.showLeds(`
        # # # # #
        # . . . .
        # # # # #
        . . . . #
        # # # # #
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    music.playTone(440, music.beat(BeatFraction.Quarter))
    basic.showLeds(`
        . . . # .
        . . # # .
        . # . # .
        # # # # #
        . . . # .
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    music.playTone(440, music.beat(BeatFraction.Quarter))
    basic.showLeds(`
        # # # # #
        . . . . #
        # # # # #
        . . . . #
        # # # # #
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    music.playTone(440, music.beat(BeatFraction.Quarter))
    basic.showLeds(`
        # # # # #
        . . . . #
        # # # # #
        # . . . .
        # # # # #
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    music.playTone(440, music.beat(BeatFraction.Quarter))
    basic.showLeds(`
        . . # . .
        . # # . .
        # . # . .
        . . # . .
        # # # # #
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
    if (radio.receivedPacket(RadioPacketProperty.SerialNumber) == 2) {
        for (let index = 0; index < 20; index++) {
            basic.pause(1000)
            已用时间 += 1
        }
    } else if (radio.receivedPacket(RadioPacketProperty.SerialNumber) == 1) {
        if (45 / 5 <= 20 - 已用时间) {
            radio.sendNumber(3)
        } else if (20 - 已用时间 >= 45 / 15) {
            radio.sendNumber(4)
        } else {
            radio.sendNumber(5)
        }
    }
})
