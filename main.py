def on_a_pressed():
    global myBall2
    myBall2 = carnival.create_projectile_ball_from_sprite(assets.image("""
        ball-blue
    """), myBall)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    info.change_score_by(-1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.booth, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    otherSprite2.destroy(effects.disintegrate, 150)
    sprite2.destroy(effects.disintegrate, 150)
    info.change_score_by(1)
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
myBall2: Ball = None
myBall: Ball = None
scene.set_background_image(assets.image("""
    wildWest
"""))
myBall = carnival.create(assets.image("""
    ball-yellow
"""), SpriteKind.player)
myBall.set_position(80, 90)
myBall.control_ball_with_arrow_keys()
myBall.set_trace_multi(carnival.Tracers.CROSS)
myBooth = sprites.create(assets.image("""
    booth
"""), SpriteKind.booth)
myBooth.z = 20
statusbar = statusbars.create(120, 6, StatusBarKind.energy)
statusbar.set_color(5, 10)
statusbar.set_bar_border(2, 1)
statusbar.bottom = 115
myBall.variable_power(statusbar, 30, 60)
carnival.start_countdown_game(30, carnival.WinTypes.SCORE)

def on_forever():
    global projectile
    if randint(0, 1) == 0:
        projectile = sprites.create_projectile_from_side(assets.image("""
            target
        """), 50, 0)
    else:
        projectile = sprites.create_projectile_from_side(assets.image("""
            can
        """), 50, 0)
        projectile.set_scale(1.5, ScaleAnchor.MIDDLE)
    projectile.bottom = 56
    projectile.set_kind(SpriteKind.enemy)
    pause(randint(500, 2000))
forever(on_forever)
