var _0x19fd = function PocketDropEvent(ballNumber, opt_target) {
    ballNumber = ballNumber - 0;
    var ball = _0x5f46[ballNumber];
    return ball;
};

function _0x10dbec(searchDefinition) {
    var river = _0x19fd("0x0");
    var _0x4e7c63 = 0;
    var stripTerrain = _0x4bf1ad(_0x53e54e(searchDefinition));
    if (stripTerrain == river) {
        _0x4e7c63 = 1;
    } else {
        _0x4e7c63 = 0;
    }
    return _0x4e7c63;
}

function _0x44d925() {
    var _0x44809b = [2, 21, 0, 34, 11, 9, 23, 30, 14, 5, 29, 4, 24, 22, 8, 20, 31, 17, 38, 35, 15, 1, 13, 6, 12, 26, 25, 27, 33, 10, 7, 16, 32, 28, 3, 19, 37, 36, 18, 39];
    return _0x44809b;
}

function _0x22f9d2() {
    var _0xb974a1 = [0, 21, 0, 34, 4, 9, 23, 30, 14, 5, 29, 4, 24, 22, 8, 20, 31, 17, 38, 35, 15, 1, 13, 6, 12, 26, 25, 27, 33, 10, 7, 16, 32, 28, 3, 19, 37, 36, 18, 39];
    return _0xb974a1;
}

function _0xdbb8b3() {
    var _0x22dcfa = [0, 21, 0, 34, 4, 9, 23, 7, 14, 5, 29, 4, 24, 13, 8, 20, 31, 17, 38, 35, 15, 1, 13, 6, 12, 26, 25, 27, 33, 10, 7, 16, 32, 28, 3, 19, 37, 36, 18, 39];
    return _0x22dcfa;
}

function _0x33903e(value) {
    var enc = _0x44d925();
    var arr = _0x19fd("0x1");
    var i = 0;
    var iter = arr[_0x19fd("0x2")];
    for (; value[_0x19fd("0x2")] < 40;) {
        value = value + arr[i++];
        if (i >= iter) {
            i = 0;
        }
    }
    var o = value[_0x19fd("0x3")]("");
    i = 0;
    for (; i < o[_0x19fd("0x2")]; i++) {
        o[enc[i]] = value[_0x19fd("0x4")](i);
    }
    return o[_0x19fd("0x5")]("");
}

function _0x53e54e(d) {
    var e = _0x22f9d2();
    var tiledImageBRs = _0x19fd("0x1");
    var b = 0;
    var tiledImageBR = tiledImageBRs[_0x19fd("0x2")];
    for (; d[_0x19fd("0x2")] < 40;) {
        d = d + tiledImageBRs[b++];
        if (b >= tiledImageBR) {
            b = 0;
        }
    }
    var a = d["split"]("");
    b = 0;
    for (; b < a["length"]; b++) {
        a[e[b]] = d[_0x19fd("0x4")](b);
    }
    return a["join"]("");
}

function _0x4bf1ad($this) {
    var PL$6 = _0x19fd("0x6");
    var PL$13 = $this[_0x19fd("0x3")]("");
    var artistTrack = 0;
    var PL$17 = 0;
    for (; PL$17 < PL$13["length"]; PL$17++) {
        artistTrack = $this[_0x19fd("0x7")](PL$17) ^ PL$6[_0x19fd("0x7")](PL$17) & 15;
        PL$13[PL$17] = String[_0x19fd("0x8")](artistTrack);
        if (artistTrack < 32 || artistTrack > 126) {}
    }
    return PL$13[_0x19fd("0x5")]("");
};