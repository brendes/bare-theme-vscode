#!/usr/bin/env python3

milk = {
    "theme_name": "bare milk",
    "theme_type": "hc-light",
    "base_0": "#ffffff",
    "base_1": "#dfdfdf",
    "base_2": "#bbbbbb",
    "base_3": "#888888",
    "base_4": "#777777",
    "base_5": "#000000",
    "red_1": "#bb5555",
    "red_2": "#e89090",
    "orange_1": "#d08868",
    "orange_2": "#f0ccb0",
    "yellow_1": "#aa8877",
    "yellow_2": "#e8d0b8",
    "green_1": "#779955",
    "green_2": "#b0c088",
    "blue_1": "#6677aa",
    "blue_2": "#b8c8d7",
    "magenta_1": "#aa7788",
    "magenta_2": "#d8b8c8",
    "cyan_1": "#77aaaa",
    "cyan_2": "#b8dbd4",
}

sun = {
    **milk,
    "theme_name": "bare sun",
    "base_0": "#fffffa",
    "base_1": "#dfdfda",
    "base_2": "#bbbbb6",
    "base_3": "#888883",
    "base_4": "#777772",
}

acme = {
    **milk,
    "theme_name": "bare acme",
    "base_0": "#ffffee",
    "base_1": "#dfdfce",
    "base_2": "#bbbbaa",
    "base_3": "#888880",
    "base_4": "#777770",
}

dark = {
    "theme_name": "bare dark",
    "theme_type": "hc-black",
    "base_0": "#2b2b2b",
    "base_1": "#484848",
    "base_2": "#777777",
    "base_3": "#888888",
    "base_4": "#999999",
    "base_5": "#dddddd",
    "red_1": "#f87870",
    "orange_1": "#ddaa77",
    "yellow_1": "#d0a868",
    "green_1": "#a9b665",
    "blue_1": "#7daea3",
    "magenta_1": "#d3889b",
    "cyan_1": "#88b4a0",
}

nord = {
    **dark,
    "theme_name": "bare nord",
    "base_0": "#2e3440",
    "base_1": "#434c5e",
    "base_2": "#5c6372",
    "base_3": "#8895ae",
    "base_4": "#98a5be",
    "base_5": "#d8dee9",
    "red_1": "#bf616a",
    "orange_1": "#d08770",
    "green_1": "#a3be8c",
    "yellow_1": "#ebcb8b",
    "blue_1": "#81a1c1",
    "magenta_1": "#b48ead",
    "cyan_1": "#88c0d0",
}

red = {
    **dark,
    "theme_name": "bare red",
    "base_0": "#110000",
    "base_1": "#442222",
    "base_2": "#663333",
    "base_3": "#aa6666",
    "base_4": "#cc7777",
    "base_5": "#ee8888",
    "red_1": "#cc6666",
    "green_1": "#cc6666",
    "yellow_1": "#cc6666",
    "blue_1": "#cc6666",
    "magenta_1": "#cc6666",
    "cyan_1": "#cc6666",
    "orange_1": "#cc6666",
}

themes = {
    "light": {
        "milk": milk,
        "sun": sun,
        "acme": acme,
    },
    "dark": {
        "dark": dark,
        "nord": nord,
        "red": red,
    },
}

for category in themes.values():
    for theme_name, theme in category.items():
        theme["bg_main"] = theme["base_0"]
        theme["bg_hl"] = theme["base_1"]
        theme["fg_faint"] = theme["base_1"]
        theme["fg_fade"] = theme["base_2"]
        theme["fg_dim"] = theme["base_3"]
        theme["fg_subtle"] = theme["base_4"]
        theme["fg_main"] = theme["base_5"]

        if theme in themes["light"].values():
            theme["border"] = theme["base_4"]
            theme["black_1"] = theme["base_5"]
            theme["white_2"] = theme["base_0"]

        elif theme in themes["dark"].values():
            theme["border"] = theme["base_3"]
            theme["black_1"] = theme["base_0"]
            theme["white_2"] = theme["base_5"]
            for color in [
                "red",
                "green",
                "yellow",
                "blue",
                "magenta",
                "cyan",
                "orange",
            ]:
                theme[f"{color}_2"] = theme[f"{color}_1"]
