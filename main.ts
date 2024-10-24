controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    myBall2 = carnival.createProjectileBallFromSprite(assets.image`
        ball-blue
    `, myBall)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Booth, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    sprite.destroy()
    info.changeScoreBy(-1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    otherSprite2.destroy(effects.disintegrate, 150)
    sprite2.destroy(effects.disintegrate, 150)
    info.changeScoreBy(1)
    music.baDing.play()
})
let projectile : Sprite = null
let myBall2 : Ball = null
let myBall : Ball = null
scene.setBackgroundImage(assets.image`
    wildWest
`)
myBall = carnival.create(assets.image`
    ball-yellow
`, SpriteKind.Player)
myBall.setPosition(80, 90)
myBall.controlBallWithArrowKeys()
myBall.setTraceMulti(carnival.Tracers.Cross)
let myBooth = sprites.create(assets.image`
    booth
`, SpriteKind.Booth)
myBooth.z = 20
let statusbar = statusbars.create(120, 6, StatusBarKind.Energy)
statusbar.setColor(5, 10)
statusbar.setBarBorder(2, 1)
statusbar.bottom = 115
myBall.variablePower(statusbar, 30, 60)
carnival.startCountdownGame(30, carnival.WinTypes.Score)
forever(function on_forever() {
    
    if (randint(0, 1) == 0) {
        projectile = sprites.createProjectileFromSide(assets.image`
            target
        `, 50, 0)
    } else {
        projectile = sprites.createProjectileFromSide(assets.image`
            can
        `, 50, 0)
        projectile.setScale(1.5, ScaleAnchor.Middle)
    }
    
    projectile.bottom = 56
    projectile.setKind(SpriteKind.Enemy)
    pause(randint(500, 2000))
})
