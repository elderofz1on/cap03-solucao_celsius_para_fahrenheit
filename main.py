def on_forever():
    basic.show_number(9 / 5 * input.temperature() + 32)
basic.forever(on_forever)
