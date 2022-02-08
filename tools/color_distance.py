#!/usr/bin/env python3

import colorsys


MD_COLORS={
    "red_50":"#FFEBEE",
    "red_100":"#FFCDD2",
    "red_200":"#EF9A9A",
    "red_300":"#E57373",
    "red_400":"#EF5350",
    "red_500":"#F44336",
    "red_600":"#E53935",
    "red_700":"#D32F2F",
    "red_800":"#C62828",
    "red_900":"#B71C1C",
    "pink_50":"#FCE4EC",
    "pink_100":"#F8BBD0",
    "pink_200":"#F48FB1",
    "pink_300":"#F06292",
    "pink_400":"#EC407A",
    "pink_500":"#E91E63",
    "pink_600":"#D81B60",
    "pink_700":"#C2185B",
    "pink_800":"#AD1457",
    "pink_900":"#880E4F",
    "purple_50":"#F3E5F5",
    "purple_100":"#E1BEE7",
    "purple_200":"#CE93D8",
    "purple_300":"#BA68C8",
    "purple_400":"#AB47BC",
    "purple_500":"#9C27B0",
    "purple_600":"#8E24AA",
    "purple_700":"#7B1FA2",
    "purple_800":"#6A1B9A",
    "purple_900":"#4A148C",
    "deep_purple_50":"#EDE7F6",
    "deep_purple_100":"#D1C4E9",
    "deep_purple_200":"#B39DDB",
    "deep_purple_300":"#9575CD",
    "deep_purple_400":"#7E57C2",
    "deep_purple_500":"#673AB7",
    "deep_purple_600":"#5E35B1",
    "deep_purple_700":"#512DA8",
    "deep_purple_800":"#4527A0",
    "deep_purple_900":"#311B92",
    "indigo_50":"#E8EAF6",
    "indigo_100":"#C5CAE9",
    "indigo_200":"#9FA8DA",
    "indigo_300":"#7986CB",
    "indigo_400":"#5C6BC0",
    "indigo_500":"#3F51B5",
    "indigo_600":"#3949AB",
    "indigo_700":"#303F9F",
    "indigo_800":"#283593",
    "indigo_900":"#1A237E",
    "blue_50":"#E3F2FD",
    "blue_100":"#BBDEFB",
    "blue_200":"#90CAF9",
    "blue_300":"#64B5F6",
    "blue_400":"#42A5F5",
    "blue_500":"#2196F3",
    "blue_600":"#1E88E5",
    "blue_700":"#1976D2",
    "blue_800":"#1565C0",
    "blue_900":"#0D47A1",
    "light_blue_50":"#E1F5FE",
    "light_blue_100":"#B3E5FC",
    "light_blue_200":"#81D4FA",
    "light_blue_300":"#4FC3F7",
    "light_blue_400":"#29B6FC",
    "light_blue_500":"#03A9F4",
    "light_blue_600":"#039BE5",
    "light_blue_700":"#0288D1",
    "light_blue_800":"#0277BD",
    "light_blue_900":"#01579B",
    "cyan_50":"#E0F7FA",
    "cyan_100":"#B2EBF2",
    "cyan_200":"#80DEEA",
    "cyan_300":"#4DD0E1",
    "cyan_400":"#26C6DA",
    "cyan_500":"#00BCD4",
    "cyan_600":"#00ACC1",
    "cyan_700":"#0097A7",
    "cyan_800":"#00838F",
    "cyan_900":"#006064",
    "teal_50":"#E0F2F1",
    "teal_100":"#B2DFDB",
    "teal_200":"#80CBC4",
    "teal_300":"#4DB6AC",
    "teal_400":"#26A69A",
    "teal_500":"#009688",
    "teal_600":"#00897B",
    "teal_700":"#00796B",
    "teal_800":"#00695C",
    "teal_900":"#004D40",
    "green_50":"#E8F5E9",
    "green_100":"#C8E6C9",
    "green_200":"#A5D6A7",
    "green_300":"#81C784",
    "green_400":"#66BB6A",
    "green_500":"#4CAF50",
    "green_600":"#43A047",
    "green_700":"#388E3C",
    "green_800":"#2E7D32",
    "green_900":"#1B5E20",
    "light_green_50":"#F1F8E9",
    "light_green_100":"#DCEDC8",
    "light_green_200":"#C5E1A5",
    "light_green_300":"#AED581",
    "light_green_400":"#9CCC65",
    "light_green_500":"#8BC34A",
    "light_green_600":"#7CB342",
    "light_green_700":"#689F38",
    "light_green_800":"#558B2F",
    "light_green_900":"#33691E",
    "lime_50":"#F9FBE7",
    "lime_100":"#F0F4C3",
    "lime_200":"#E6EE9C",
    "lime_300":"#DCE775",
    "lime_400":"#D4E157",
    "lime_500":"#CDDC39",
    "lime_600":"#C0CA33",
    "lime_700":"#A4B42B",
    "lime_800":"#9E9D24",
    "lime_900":"#827717",
    "yellow_50":"#FFFDE7",
    "yellow_100":"#FFF9C4",
    "yellow_200":"#FFF590",
    "yellow_300":"#FFF176",
    "yellow_400":"#FFEE58",
    "yellow_500":"#FFEB3B",
    "yellow_600":"#FDD835",
    "yellow_700":"#FBC02D",
    "yellow_800":"#F9A825",
    "yellow_900":"#F57F17",
    "amber_50":"#FFF8E1",
    "amber_100":"#FFECB3",
    "amber_200":"#FFE082",
    "amber_300":"#FFD54F",
    "amber_400":"#FFCA28",
    "amber_500":"#FFC107",
    "amber_600":"#FFB300",
    "amber_700":"#FFA000",
    "amber_800":"#FF8F00",
    "amber_900":"#FF6F00",
    "orange_50":"#FFF3E0",
    "orange_100":"#FFE0B2",
    "orange_200":"#FFCC80",
    "orange_300":"#FFB74D",
    "orange_400":"#FFA726",
    "orange_500":"#FF9800",
    "orange_600":"#FB8C00",
    "orange_700":"#F57C00",
    "orange_800":"#EF6C00",
    "orange_900":"#E65100",
    "deep_orange_50":"#FBE9A7",
    "deep_orange_100":"#FFCCBC",
    "deep_orange_200":"#FFAB91",
    "deep_orange_300":"#FF8A65",
    "deep_orange_400":"#FF7043",
    "deep_orange_500":"#FF5722",
    "deep_orange_600":"#F4511E",
    "deep_orange_700":"#E64A19",
    "deep_orange_800":"#D84315",
    "deep_orange_900":"#BF360C",
    "brown_50":"#EFEBE9",
    "brown_100":"#D7CCC8",
    "brown_200":"#BCAAA4",
    "brown_300":"#A1887F",
    "brown_400":"#8D6E63",
    "brown_500":"#795548",
    "brown_600":"#6D4C41",
    "brown_700":"#5D4037",
    "brown_800":"#4E342E",
    "brown_900":"#3E2723",
    "grey_50":"#FAFAFA",
    "grey_100":"#F5F5F5",
    "grey_200":"#EEEEEE",
    "grey_300":"#E0E0E0",
    "grey_400":"#BDBDBD",
    "grey_500":"#9E9E9E",
    "grey_600":"#757575",
    "grey_700":"#616161",
    "grey_800":"#424242",
    "grey_900":"#212121",
    "blue_grey_50":"#ECEFF1",
    "blue_grey_100":"#CFD8DC",
    "blue_grey_200":"#B0BBC5",
    "blue_grey_300":"#90A4AE",
    "blue_grey_400":"#78909C",
    "blue_grey_500":"#607D8B",
    "blue_grey_600":"#546E7A",
    "blue_grey_700":"#455A64",
    "blue_grey_800":"#37474F",
    "blue_grey_900":"#263238",
    "black_1000":"#000000",
    "white_1000":"#FFFFFF",
}

COLORS = {
    "017":"#00005f",
    "018":"#000087",
    "019":"#0000af",
    "020":"#0000d7",
    "021":"#0000ff",
    "022":"#005f00",
    "023":"#005f5f",
    "024":"#005f87",
    "025":"#005faf",
    "026":"#005fd7",
    "027":"#005fff",
    "028":"#008700",
    "029":"#00875f",
    "030":"#008787",
    "031":"#0087af",
    "032":"#0087d7",
    "033":"#0087ff",
    "034":"#00af00",
    "035":"#00af5f",
    "036":"#00af87",
    "037":"#00afaf",
    "038":"#00afd7",
    "039":"#00afff",
    "040":"#00d700",
    "041":"#00d75f",
    "042":"#00d787",
    "043":"#00d7af",
    "044":"#00d7d7",
    "045":"#00d7ff",
    "046":"#00ff00",
    "047":"#00ff5f",
    "048":"#00ff87",
    "049":"#00ffaf",
    "050":"#00ffd7",
    "051":"#00ffff",
    "052":"#5f0000",
    "053":"#5f005f",
    "054":"#5f0087",
    "055":"#5f00af",
    "056":"#5f00d7",
    "057":"#5f00ff",
    "058":"#5f5f00",
    "059":"#5f5f5f",
    "060":"#5f5f87",
    "061":"#5f5faf",
    "062":"#5f5fd7",
    "063":"#5f5fff",
    "064":"#5f8700",
    "065":"#5f875f",
    "066":"#5f8787",
    "067":"#5f87af",
    "068":"#5f87d7",
    "069":"#5f87ff",
    "070":"#5faf00",
    "071":"#5faf5f",
    "072":"#5faf87",
    "073":"#5fafaf",
    "074":"#5fafd7",
    "075":"#5fafff",
    "076":"#5fd700",
    "077":"#5fd75f",
    "078":"#5fd787",
    "079":"#5fd7af",
    "080":"#5fd7d7",
    "081":"#5fd7ff",
    "082":"#5fff00",
    "083":"#5fff5f",
    "084":"#5fff87",
    "085":"#5fffaf",
    "086":"#5fffd7",
    "087":"#5fffff",
    "088":"#870000",
    "089":"#87005f",
    "090":"#870087",
    "091":"#8700af",
    "092":"#8700d7",
    "093":"#8700ff",
    "094":"#875f00",
    "095":"#875f5f",
    "096":"#875f87",
    "097":"#875faf",
    "098":"#875fd7",
    "099":"#875fff",
    "100":"#878700",
    "101":"#87875f",
    "102":"#878787",
    "103":"#8787af",
    "104":"#8787d7",
    "105":"#8787ff",
    "106":"#87af00",
    "107":"#87af5f",
    "108":"#87af87",
    "109":"#87afaf",
    "110":"#87afd7",
    "111":"#87afff",
    "112":"#87d700",
    "113":"#87d75f",
    "114":"#87d787",
    "115":"#87d7af",
    "116":"#87d7d7",
    "117":"#87d7ff",
    "118":"#87ff00",
    "119":"#87ff5f",
    "120":"#87ff87",
    "121":"#87ffaf",
    "122":"#87ffd7",
    "123":"#87ffff",
    "124":"#af0000",
    "125":"#af005f",
    "126":"#af0087",
    "127":"#af00af",
    "128":"#af00d7",
    "129":"#af00ff",
    "130":"#af5f00",
    "131":"#af5f5f",
    "132":"#af5f87",
    "133":"#af5faf",
    "134":"#af5fd7",
    "135":"#af5fff",
    "136":"#af8700",
    "137":"#af875f",
    "138":"#af8787",
    "139":"#af87af",
    "140":"#af87d7",
    "141":"#af87ff",
    "142":"#afaf00",
    "143":"#afaf5f",
    "144":"#afaf87",
    "145":"#afafaf",
    "146":"#afafd7",
    "147":"#afafff",
    "148":"#afd700",
    "149":"#afd75f",
    "150":"#afd787",
    "151":"#afd7af",
    "152":"#afd7d7",
    "153":"#afd7ff",
    "154":"#afff00",
    "155":"#afff5f",
    "156":"#afff87",
    "157":"#afffaf",
    "158":"#afffd7",
    "159":"#afffff",
    "160":"#d70000",
    "161":"#d7005f",
    "162":"#d70087",
    "163":"#d700af",
    "164":"#d700d7",
    "165":"#d700ff",
    "166":"#d75f00",
    "167":"#d75f5f",
    "168":"#d75f87",
    "169":"#d75faf",
    "170":"#d75fd7",
    "171":"#d75fff",
    "172":"#d78700",
    "173":"#d7875f",
    "174":"#d78787",
    "175":"#d787af",
    "176":"#d787d7",
    "177":"#d787ff",
    "178":"#d7af00",
    "179":"#d7af5f",
    "180":"#d7af87",
    "181":"#d7afaf",
    "182":"#d7afd7",
    "183":"#d7afff",
    "184":"#d7d700",
    "185":"#d7d75f",
    "186":"#d7d787",
    "187":"#d7d7af",
    "188":"#d7d7d7",
    "189":"#d7d7ff",
    "190":"#d7ff00",
    "191":"#d7ff5f",
    "192":"#d7ff87",
    "193":"#d7ffaf",
    "194":"#d7ffd7",
    "195":"#d7ffff",
    "196":"#ff0000",
    "197":"#ff005f",
    "198":"#ff0087",
    "199":"#ff00af",
    "200":"#ff00d7",
    "201":"#ff00ff",
    "202":"#ff5f00",
    "203":"#ff5f5f",
    "204":"#ff5f87",
    "205":"#ff5faf",
    "206":"#ff5fd7",
    "207":"#ff5fff",
    "208":"#ff8700",
    "209":"#ff875f",
    "210":"#ff8787",
    "211":"#ff87af",
    "212":"#ff87d7",
    "213":"#ff87ff",
    "214":"#ffaf00",
    "215":"#ffaf5f",
    "216":"#ffaf87",
    "217":"#ffafaf",
    "218":"#ffafd7",
    "219":"#ffafff",
    "220":"#ffd700",
    "221":"#ffd75f",
    "222":"#ffd787",
    "223":"#ffd7af",
    "224":"#ffd7d7",
    "225":"#ffd7ff",
    "226":"#ffff00",
    "227":"#ffff5f",
    "228":"#ffff87",
    "229":"#ffffaf",
    "230":"#ffffd7",
    "231":"#ffffff",
    "232":"#080808",
    "233":"#121212",
    "234":"#1c1c1c",
    "235":"#262626",
    "236":"#303030",
    "237":"#3a3a3a",
    "238":"#444444",
    "239":"#4e4e4e",
    "240":"#585858",
    "241":"#626262",
    "242":"#6c6c6c",
    "243":"#767676",
    "244":"#808080",
    "245":"#8a8a8a",
    "246":"#949494",
    "247":"#9e9e9e",
    "248":"#a8a8a8",
    "249":"#b2b2b2",
    "250":"#bcbcbc",
    "251":"#c6c6c6",
    "252":"#d0d0d0",
    "253":"#dadada",
    "254":"#e4e4e4",
    "255":"#eeeeee",
}

def color_distance(a, b):
    a = a.lstrip('#')
    b = b.lstrip('#')
    a=tuple(int(a[i:i+2], 16) for i in (0, 2, 4))
    b=tuple(int(b[i:i+2], 16) for i in (0, 2, 4))
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
            score.append(color_distance(MD_COLORS[i_md_key],COLORS[i_key]))
            color.append(i_key)
        print(f"let g:{i_md_key}_cterm = \"{color[score.index(max(score))]}\"")

main()