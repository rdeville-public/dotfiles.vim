#!/usr/bin/env python3


import colorsys

MD_COLORS = {
    "white": "#ffffff",
    "black": "#000000",
    "red_50": "#ffebee",
    "red_100": "#ffcdd2",
    "red_200": "#ef9a9a",
    "red_300": "#e57373",
    "red_400": "#ef5350",
    "red_500": "#f44336",
    "red_600": "#e53935",
    "red_700": "#d32f2f",
    "red_800": "#c62828",
    "red_900": "#b71c1c",
    "red_A100": "#ff8a80",
    "red_A200": "#ff5252",
    "red_A400": "#ff1744",
    "red_A700": "#d50000",

    "pink_500": "#e91e63",
    "pink_50": "#fce4ec",
    "pink_100": "#f8bbd0",
    "pink_200": "#f48fb1",
    "pink_300": "#f06292",
    "pink_400": "#ec407a",
    "pink_500": "#e91e63",
    "pink_600": "#d81b60",
    "pink_700": "#c2185b",
    "pink_800": "#ad1457",
    "pink_900": "#880e4f",
    "pink_A100": "#ff80ab",
    "pink_A200": "#ff4081",
    "pink_A400": "#f50057",
    "pink_A700": "#c51162",

    "purple_50": "#f3e5f5",
    "purple_100": "#e1bee7",
    "purple_200": "#ce93d8",
    "purple_300": "#ba68c8",
    "purple_400": "#ab47bc",
    "purple_500": "#9c27b0",
    "purple_600": "#8e24aa",
    "purple_700": "#7b1fa2",
    "purple_800": "#6a1b9a",
    "purple_900": "#4a148c",
    "purple_A100": "#ea80fc",
    "purple_A200": "#e040fb",
    "purple_A400": "#d500f9",
    "purple_A700": "#aa00ff",

    "deep_purple_50": "#ede7f6",
    "deep_purple_100": "#d1c4e9",
    "deep_purple_200": "#b39ddb",
    "deep_purple_300": "#9575cd",
    "deep_purple_400": "#7e57c2",
    "deep_purple_500": "#673ab7",
    "deep_purple_600": "#5e35b1",
    "deep_purple_700": "#512da8",
    "deep_purple_800": "#4527a0",
    "deep_purple_900": "#311b92",
    "deep_purple_A100": "#b388ff",
    "deep_purple_A200": "#7c4dff",
    "deep_purple_A400": "#651fff",
    "deep_purple_A700": "#6200ea",

    "indigo_50": "#e8eaf6",
    "indigo_100": "#c5cae9",
    "indigo_200": "#9fa8da",
    "indigo_300": "#7986cb",
    "indigo_400": "#5c6bc0",
    "indigo_500": "#3f51b5",
    "indigo_600": "#3949ab",
    "indigo_700": "#303f9f",
    "indigo_800": "#283593",
    "indigo_900": "#1a237e",
    "indigo_A100": "#8c9eff",
    "indigo_A200": "#536dfe",
    "indigo_A400": "#3d5afe",
    "indigo_A700": "#304ffe",

    "blue_50": "#e3f2fd",
    "blue_100": "#bbdefb",
    "blue_200": "#90caf9",
    "blue_300": "#64b5f6",
    "blue_400": "#42a5f5",
    "blue_500": "#2196f3",
    "blue_600": "#1e88e5",
    "blue_700": "#1976d2",
    "blue_800": "#1565c0",
    "blue_900": "#0d47a1",
    "blue_A100": "#82b1ff",
    "blue_A200": "#448aff",
    "blue_A400": "#2979ff",
    "blue_A700": "#2962ff",

    "light_blue_50": "#e1f5fe",
    "light_blue_100": "#b3e5fc",
    "light_blue_200": "#81d4fa",
    "light_blue_300": "#4fc3f7",
    "light_blue_400": "#29b6f6",
    "light_blue_500": "#03a9f4",
    "light_blue_600": "#039be5",
    "light_blue_700": "#0288d1",
    "light_blue_800": "#0277bd",
    "light_blue_900": "#01579b",
    "light_blue_A100": "#80d8ff",
    "light_blue_A200": "#40c4ff",
    "light_blue_A400": "#00b0ff",
    "light_blue_A700": "#0091ea",

    "cyan_50": "#e0f7fa",
    "cyan_100": "#b2ebf2",
    "cyan_200": "#80deea",
    "cyan_300": "#4dd0e1",
    "cyan_400": "#26c6da",
    "cyan_500": "#00bcd4",
    "cyan_600": "#00acc1",
    "cyan_700": "#0097a7",
    "cyan_800": "#00838f",
    "cyan_900": "#006064",
    "cyan_A100": "#84ffff",
    "cyan_A200": "#18ffff",
    "cyan_A400": "#00e5ff",
    "cyan_A700": "#00b8d4",

    "teal_50": "#e0f2f1",
    "teal_100": "#b2dfdb",
    "teal_200": "#80cbc4",
    "teal_300": "#4db6ac",
    "teal_400": "#26a69a",
    "teal_500": "#009688",
    "teal_600": "#00897b",
    "teal_700": "#00796b",
    "teal_800": "#00695c",
    "teal_900": "#004d40",
    "teal_A100": "#a7ffeb",
    "teal_A200": "#64ffda",
    "teal_A400": "#1de9b6",
    "teal_A700": "#00bfa5",

    "green_50": "#e8f5e9",
    "green_100": "#c8e6c9",
    "green_200": "#a5d6a7",
    "green_300": "#81c784",
    "green_400": "#66bb6a",
    "green_500": "#4caf50",
    "green_600": "#43a047",
    "green_700": "#388e3c",
    "green_800": "#2e7d32",
    "green_900": "#1b5e20",
    "green_A100": "#b9f6ca",
    "green_A200": "#69f0ae",
    "green_A400": "#00e676",
    "green_A700": "#00c853",

    "light_green_50": "#f1f8e9",
    "light_green_100": "#dcedc8",
    "light_green_200": "#c5e1a5",
    "light_green_300": "#aed581",
    "light_green_400": "#9ccc65",
    "light_green_500": "#8bc34a",
    "light_green_600": "#7cb342",
    "light_green_700": "#689f38",
    "light_green_800": "#558b2f",
    "light_green_900": "#33691e",
    "light_green_A100": "#ccff90",
    "light_green_A200": "#b2ff59",
    "light_green_A400": "#76ff03",
    "light_green_A700": "#64dd17",

    "lime_50": "#f9fbe7",
    "lime_100": "#f0f4c3",
    "lime_200": "#e6ee9c",
    "lime_300": "#dce775",
    "lime_400": "#d4e157",
    "lime_500": "#cddc39",
    "lime_600": "#c0ca33",
    "lime_700": "#afb42b",
    "lime_800": "#9e9d24",
    "lime_900": "#827717",
    "lime_A100": "#f4ff81",
    "lime_A200": "#eeff41",
    "lime_A400": "#c6ff00",
    "lime_A700": "#aeea00",

    "yellow_50": "#fffde7",
    "yellow_100": "#fff9c4",
    "yellow_200": "#fff59d",
    "yellow_300": "#fff176",
    "yellow_400": "#ffee58",
    "yellow_500": "#ffeb3b",
    "yellow_600": "#fdd835",
    "yellow_700": "#fbc02d",
    "yellow_800": "#f9a825",
    "yellow_900": "#f57f17",
    "yellow_A100": "#ffff8d",
    "yellow_A200": "#ffff00",
    "yellow_A400": "#ffea00",
    "yellow_A700": "#ffd600",

    "amber_50": "#fff8e1",
    "amber_100": "#ffecb3",
    "amber_200": "#ffe082",
    "amber_300": "#ffd54f",
    "amber_400": "#ffca28",
    "amber_500": "#ffc107",
    "amber_600": "#ffb300",
    "amber_700": "#ffa000",
    "amber_800": "#ff8f00",
    "amber_900": "#ff6f00",
    "amber_A100": "#ffe57f",
    "amber_A200": "#ffd740",
    "amber_A400": "#ffc400",
    "amber_A700": "#ffab00",

    "orange_50": "#fff3e0",
    "orange_100": "#ffe0b2",
    "orange_200": "#ffcc80",
    "orange_300": "#ffb74d",
    "orange_400": "#ffa726",
    "orange_500": "#ff9800",
    "orange_600": "#fb8c00",
    "orange_700": "#f57c00",
    "orange_800": "#ef6c00",
    "orange_900": "#e65100",
    "orange_A100": "#ffd180",
    "orange_A200": "#ffab40",
    "orange_A400": "#ff9100",
    "orange_A700": "#ff6d00",

    "deep_orange_50": "#fbe9e7",
    "deep_orange_100": "#ffccbc",
    "deep_orange_200": "#ffab91",
    "deep_orange_300": "#ff8a65",
    "deep_orange_400": "#ff7043",
    "deep_orange_500": "#ff5722",
    "deep_orange_600": "#f4511e",
    "deep_orange_700": "#e64a19",
    "deep_orange_800": "#d84315",
    "deep_orange_900": "#bf360c",
    "deep_orange_A100": "#ff9e80",
    "deep_orange_A200": "#ff6e40",
    "deep_orange_A400": "#ff3d00",
    "deep_orange_A700": "#dd2c00",

    "brown_50": "#efebe9",
    "brown_100": "#d7ccc8",
    "brown_200": "#bcaaa4",
    "brown_300": "#a1887f",
    "brown_400": "#8d6e63",
    "brown_500": "#795548",
    "brown_600": "#6d4c41",
    "brown_700": "#5d4037",
    "brown_800": "#4e342e",
    "brown_900": "#3e2723",
    "brown_A100": "#d7ccc8",
    "brown_A200": "#bcaaa4",
    "brown_A400": "#8d6e63",
    "brown_A700": "#5d4037",

    "grey_50": "#fafafa",
    "grey_100": "#f5f5f5",
    "grey_200": "#eeeeee",
    "grey_300": "#e0e0e0",
    "grey_400": "#bdbdbd",
    "grey_500": "#9e9e9e",
    "grey_600": "#757575",
    "grey_700": "#616161",
    "grey_800": "#424242",
    "grey_900": "#212121",
    "grey_A100": "#f5f5f5",
    "grey_A200": "#eeeeee",
    "grey_A400": "#bdbdbd",
    "grey_A700": "#616161",

    "blue_grey_50": "#eceff1",
    "blue_grey_100": "#cfd8dc",
    "blue_grey_200": "#b0bec5",
    "blue_grey_300": "#90a4ae",
    "blue_grey_400": "#78909c",
    "blue_grey_500": "#607d8b",
    "blue_grey_600": "#546e7a",
    "blue_grey_700": "#455a64",
    "blue_grey_800": "#37474f",
    "blue_grey_900": "#263238",
    "blue_grey_A100": "#cfd8dc",
    "blue_grey_A200": "#b0bec5",
    "blue_grey_A400": "#78909c",
    "blue_grey_A700": "#455a64",
}

COLORS = {
    "017": "#00005f",
    "018": "#000087",
    "019": "#0000af",
    "020": "#0000d7",
    "021": "#0000ff",
    "022": "#005f00",
    "023": "#005f5f",
    "024": "#005f87",
    "025": "#005faf",
    "026": "#005fd7",
    "027": "#005fff",
    "028": "#008700",
    "029": "#00875f",
    "030": "#008787",
    "031": "#0087af",
    "032": "#0087d7",
    "033": "#0087ff",
    "034": "#00af00",
    "035": "#00af5f",
    "036": "#00af87",
    "037": "#00afaf",
    "038": "#00afd7",
    "039": "#00afff",
    "040": "#00d700",
    "041": "#00d75f",
    "042": "#00d787",
    "043": "#00d7af",
    "044": "#00d7d7",
    "045": "#00d7ff",
    "046": "#00ff00",
    "047": "#00ff5f",
    "048": "#00ff87",
    "049": "#00ffaf",
    "050": "#00ffd7",
    "051": "#00ffff",
    "052": "#5f0000",
    "053": "#5f005f",
    "054": "#5f0087",
    "055": "#5f00af",
    "056": "#5f00d7",
    "057": "#5f00ff",
    "058": "#5f5f00",
    "059": "#5f5f5f",
    "060": "#5f5f87",
    "061": "#5f5faf",
    "062": "#5f5fd7",
    "063": "#5f5fff",
    "064": "#5f8700",
    "065": "#5f875f",
    "066": "#5f8787",
    "067": "#5f87af",
    "068": "#5f87d7",
    "069": "#5f87ff",
    "070": "#5faf00",
    "071": "#5faf5f",
    "072": "#5faf87",
    "073": "#5fafaf",
    "074": "#5fafd7",
    "075": "#5fafff",
    "076": "#5fd700",
    "077": "#5fd75f",
    "078": "#5fd787",
    "079": "#5fd7af",
    "080": "#5fd7d7",
    "081": "#5fd7ff",
    "082": "#5fff00",
    "083": "#5fff5f",
    "084": "#5fff87",
    "085": "#5fffaf",
    "086": "#5fffd7",
    "087": "#5fffff",
    "088": "#870000",
    "089": "#87005f",
    "090": "#870087",
    "091": "#8700af",
    "092": "#8700d7",
    "093": "#8700ff",
    "094": "#875f00",
    "095": "#875f5f",
    "096": "#875f87",
    "097": "#875faf",
    "098": "#875fd7",
    "099": "#875fff",
    "100": "#878700",
    "101": "#87875f",
    "102": "#878787",
    "103": "#8787af",
    "104": "#8787d7",
    "105": "#8787ff",
    "106": "#87af00",
    "107": "#87af5f",
    "108": "#87af87",
    "109": "#87afaf",
    "110": "#87afd7",
    "111": "#87afff",
    "112": "#87d700",
    "113": "#87d75f",
    "114": "#87d787",
    "115": "#87d7af",
    "116": "#87d7d7",
    "117": "#87d7ff",
    "118": "#87ff00",
    "119": "#87ff5f",
    "120": "#87ff87",
    "121": "#87ffaf",
    "122": "#87ffd7",
    "123": "#87ffff",
    "124": "#af0000",
    "125": "#af005f",
    "126": "#af0087",
    "127": "#af00af",
    "128": "#af00d7",
    "129": "#af00ff",
    "130": "#af5f00",
    "131": "#af5f5f",
    "132": "#af5f87",
    "133": "#af5faf",
    "134": "#af5fd7",
    "135": "#af5fff",
    "136": "#af8700",
    "137": "#af875f",
    "138": "#af8787",
    "139": "#af87af",
    "140": "#af87d7",
    "141": "#af87ff",
    "142": "#afaf00",
    "143": "#afaf5f",
    "144": "#afaf87",
    "145": "#afafaf",
    "146": "#afafd7",
    "147": "#afafff",
    "148": "#afd700",
    "149": "#afd75f",
    "150": "#afd787",
    "151": "#afd7af",
    "152": "#afd7d7",
    "153": "#afd7ff",
    "154": "#afff00",
    "155": "#afff5f",
    "156": "#afff87",
    "157": "#afffaf",
    "158": "#afffd7",
    "159": "#afffff",
    "160": "#d70000",
    "161": "#d7005f",
    "162": "#d70087",
    "163": "#d700af",
    "164": "#d700d7",
    "165": "#d700ff",
    "166": "#d75f00",
    "167": "#d75f5f",
    "168": "#d75f87",
    "169": "#d75faf",
    "170": "#d75fd7",
    "171": "#d75fff",
    "172": "#d78700",
    "173": "#d7875f",
    "174": "#d78787",
    "175": "#d787af",
    "176": "#d787d7",
    "177": "#d787ff",
    "178": "#d7af00",
    "179": "#d7af5f",
    "180": "#d7af87",
    "181": "#d7afaf",
    "182": "#d7afd7",
    "183": "#d7afff",
    "184": "#d7d700",
    "185": "#d7d75f",
    "186": "#d7d787",
    "187": "#d7d7af",
    "188": "#d7d7d7",
    "189": "#d7d7ff",
    "190": "#d7ff00",
    "191": "#d7ff5f",
    "192": "#d7ff87",
    "193": "#d7ffaf",
    "194": "#d7ffd7",
    "195": "#d7ffff",
    "196": "#ff0000",
    "197": "#ff005f",
    "198": "#ff0087",
    "199": "#ff00af",
    "200": "#ff00d7",
    "201": "#ff00ff",
    "202": "#ff5f00",
    "203": "#ff5f5f",
    "204": "#ff5f87",
    "205": "#ff5faf",
    "206": "#ff5fd7",
    "207": "#ff5fff",
    "208": "#ff8700",
    "209": "#ff875f",
    "210": "#ff8787",
    "211": "#ff87af",
    "212": "#ff87d7",
    "213": "#ff87ff",
    "214": "#ffaf00",
    "215": "#ffaf5f",
    "216": "#ffaf87",
    "217": "#ffafaf",
    "218": "#ffafd7",
    "219": "#ffafff",
    "220": "#ffd700",
    "221": "#ffd75f",
    "222": "#ffd787",
    "223": "#ffd7af",
    "224": "#ffd7d7",
    "225": "#ffd7ff",
    "226": "#ffff00",
    "227": "#ffff5f",
    "228": "#ffff87",
    "229": "#ffffaf",
    "230": "#ffffd7",
    "231": "#ffffff",
    "232": "#080808",
    "233": "#121212",
    "234": "#1c1c1c",
    "235": "#262626",
    "236": "#303030",
    "237": "#3a3a3a",
    "238": "#444444",
    "239": "#4e4e4e",
    "240": "#585858",
    "241": "#626262",
    "242": "#6c6c6c",
    "243": "#767676",
    "244": "#808080",
    "245": "#8a8a8a",
    "246": "#949494",
    "247": "#9e9e9e",
    "248": "#a8a8a8",
    "249": "#b2b2b2",
    "250": "#bcbcbc",
    "251": "#c6c6c6",
    "252": "#d0d0d0",
    "253": "#dadada",
    "254": "#e4e4e4",
    "255": "#eeeeee",
}


def color_distance(a, b):
    a = a.lstrip('#')
    b = b.lstrip('#')
    a = tuple(int(a[i:i+2], 16) for i in (0, 2, 4))
    b = tuple(int(b[i:i+2], 16) for i in (0, 2, 4))
    # Colors are list of 3 floats (RGB) from 0.0 to 1.0
    a_h, a_s, a_v = colorsys.rgb_to_hsv(a[0] / 255, a[1] / 255, a[2] / 255)
    b_h, b_s, b_v = colorsys.rgb_to_hsv(b[0] / 255, b[1] / 255, b[2] / 255)
    diff_h = 1 - abs(a_h - b_h)
    diff_s = 1 - abs(a_s - b_s)
    diff_v = 1 - abs(a_v - b_v)
    score = diff_h * diff_s * diff_v
    return score


def main():
    for i_md_key in MD_COLORS:
        score = []
        color = []
        for i_key in COLORS:
            score.append(color_distance(MD_COLORS[i_md_key], COLORS[i_key]))
            color.append(i_key)
        print(f"let g:{i_md_key} = [\"{MD_COLORS[i_md_key]}\", \"{color[score.index(max(score))]}\"]")


main()
