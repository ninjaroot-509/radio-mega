$((function() { var a, t, e, i, r, o, s, n, u, c, l, d, f, m = $("#player-track"),
        v = $("#bg-artwork"),
        p = $("#album-name"),
        N = $("#track-name"),
        h = $("#album-art"),
        x = $("#s-area"),
        g = $("#seek-bar"),
        k = $("#track-time"),
        C = $("#ins-time"),
        w = $("#s-hover"),
        y = $("#play-pause-button"),
        b = y.find("i"),
        M = $("#current-time"),
        T = $("#track-length"),
        A = 0,
        I = null,
        D = !1,
        _ = ["Dawn", "Me & You", "Electro Boy", "Home", "Proxy (Original Mix)"],
        S = ["Skylike - Dawn", "Alex Skrindo - Me & You", "Kaaze - Electro Boy", "Jordan Schor - Home", "Martin Garrix - Proxy"],
        B = ["_1", "_2", "_3", "_4", "_5"],
        E = ["https://raw.githubusercontent.com/himalayasingh/music-player-1/master/music/2.mp3"],
        H = $("#play-previous"),
        O = $("#play-next"),
        P = -1;

    function Y() { setTimeout((function() { audio.paused ? (m.addClass("active"), h.addClass("active"), K(), b.attr("class", "fas fa-pause"), audio.play()) : (m.removeClass("active"), h.removeClass("active"), clearInterval(I), h.removeClass("buffering"), b.attr("class", "fas fa-play"), audio.pause()) }), 300) }

    function z() { w.width(0), C.text("00:00").css({ left: "0px", "margin-left": "0px" }).fadeOut(0) }

    function G() { audio.currentTime = e, g.width(t), z() }

    function J() { A = (A = new Date).getTime(), D || (D = !0, k.addClass("active")), n = Math.floor(audio.currentTime / 60), u = Math.floor(audio.currentTime - 60 * n), c = Math.floor(audio.duration / 60), l = Math.floor(audio.duration - 60 * c), d = audio.currentTime / audio.duration * 100, n < 10 && (n = "0" + n), u < 10 && (u = "0" + u), c < 10 && (c = "0" + c), l < 10 && (l = "0" + l), isNaN(n) || isNaN(u) ? M.text("00:00") : M.text(n + ":" + u), isNaN(c) || isNaN(l) ? T.text("00:00") : T.text(c + ":" + l), isNaN(n) || isNaN(u) || isNaN(c) || isNaN(l) ? k.removeClass("active") : k.addClass("active"), g.width(d + "%"), 100 == d && (b.attr("class", "fa fa-play"), g.width(0), M.text("00:00"), h.removeClass("buffering").removeClass("active"), clearInterval(I)) }

    function K() { clearInterval(I), I = setInterval((function() { 0 == A || f - A > 1e3 ? h.addClass("buffering") : h.removeClass("buffering"), f = (f = new Date).getTime() }), 100) }

    function W(t) { 0 == t || 1 == t ? ++P : --P, P > -1 && P < B.length ? (0 == t ? b.attr("class", "fa fa-play") : (h.removeClass("buffering"), b.attr("class", "fa fa-pause")), g.width(0), k.removeClass("active"), M.text("00:00"), T.text("00:00"), currAlbum = _[P], currTrackName = S[P], currArtwork = B[P], audio.src = E[P], A = 0, f = (f = new Date).getTime(), 0 != t && (audio.play(), m.addClass("active"), h.addClass("active"), clearInterval(I), K()), p.text(currAlbum), N.text(currTrackName), h.find("img.active").removeClass("active"), $("#" + currArtwork).addClass("active"), a = $("#" + currArtwork).attr("src"), v.css({ "background-image": "url(" + a + ")" })) : 0 == t || 1 == t ? --P : ++P }
    audio = new Audio, W(0), audio.loop = !1, y.on("click", Y), x.mousemove((function(a) {! function(a) { i = x.offset(), t = a.clientX - i.left, e = audio.duration * (t / x.outerWidth()), w.width(t), r = e / 60, o = Math.floor(r), s = Math.floor(e - 60 * o), o < 0 || s < 0 || o < 0 || s < 0 || (o < 10 && (o = "0" + o), s < 10 && (s = "0" + s), isNaN(o) || isNaN(s) ? C.text("--:--") : C.text(o + ":" + s), C.css({ left: t, "margin-left": "-21px" }).fadeIn(0)) }(a) })), x.mouseout(z), x.on("click", G), $(audio).on("timeupdate", J), H.on("click", (function() { W(-1) })), O.on("click", (function() { W(1) })) })), $((function() { var a, t, e, i, r, o, s, n, u, c, l, d, f, m = $("#player-track"),
        v = $("#bg-artwork"),
        p = $("#album-name"),
        N = $("#track-name"),
        h = $("#album-art"),
        x = $("#s-area"),
        g = $("#seek-bar"),
        k = $("#track-time"),
        C = $("#ins-time"),
        w = $("#s-hover"),
        y = $("#play-pause-button2"),
        b = y.find("i"),
        M = $("#current-time"),
        T = $("#track-length"),
        A = 0,
        I = null,
        D = !1,
        _ = ["Dawn", "Me & You", "Electro Boy", "Home", "Proxy (Original Mix)"],
        S = ["Skylike - Dawn", "Alex Skrindo - Me & You", "Kaaze - Electro Boy", "Jordan Schor - Home", "Martin Garrix - Proxy"],
        B = ["_1", "_2", "_3", "_4", "_5"],
        E = ["https://raw.githubusercontent.com/himalayasingh/music-player-1/master/music/2.mp3"],
        H = $("#play-previous"),
        O = $("#play-next"),
        P = -1;

    function Y() { setTimeout((function() { audio.paused ? (m.addClass("active"), h.addClass("active"), K(), b.attr("class", "fas fa-pause"), audio.play()) : (m.removeClass("active"), h.removeClass("active"), clearInterval(I), h.removeClass("buffering"), b.attr("class", "fas fa-play"), audio.pause()) }), 300) }

    function z() { w.width(0), C.text("00:00").css({ left: "0px", "margin-left": "0px" }).fadeOut(0) }

    function G() { audio.currentTime = e, g.width(t), z() }

    function J() { A = (A = new Date).getTime(), D || (D = !0, k.addClass("active")), n = Math.floor(audio.currentTime / 60), u = Math.floor(audio.currentTime - 60 * n), c = Math.floor(audio.duration / 60), l = Math.floor(audio.duration - 60 * c), d = audio.currentTime / audio.duration * 100, n < 10 && (n = "0" + n), u < 10 && (u = "0" + u), c < 10 && (c = "0" + c), l < 10 && (l = "0" + l), isNaN(n) || isNaN(u) ? M.text("00:00") : M.text(n + ":" + u), isNaN(c) || isNaN(l) ? T.text("00:00") : T.text(c + ":" + l), isNaN(n) || isNaN(u) || isNaN(c) || isNaN(l) ? k.removeClass("active") : k.addClass("active"), g.width(d + "%"), 100 == d && (b.attr("class", "fa fa-play"), g.width(0), M.text("00:00"), h.removeClass("buffering").removeClass("active"), clearInterval(I)) }

    function K() { clearInterval(I), I = setInterval((function() { 0 == A || f - A > 1e3 ? h.addClass("buffering") : h.removeClass("buffering"), f = (f = new Date).getTime() }), 100) }

    function W(t) { 0 == t || 1 == t ? ++P : --P, P > -1 && P < B.length ? (0 == t ? b.attr("class", "fa fa-play") : (h.removeClass("buffering"), b.attr("class", "fa fa-pause")), g.width(0), k.removeClass("active"), M.text("00:00"), T.text("00:00"), currAlbum = _[P], currTrackName = S[P], currArtwork = B[P], audio.src = E[P], A = 0, f = (f = new Date).getTime(), 0 != t && (audio.play(), m.addClass("active"), h.addClass("active"), clearInterval(I), K()), p.text(currAlbum), N.text(currTrackName), h.find("img.active").removeClass("active"), $("#" + currArtwork).addClass("active"), a = $("#" + currArtwork).attr("src"), v.css({ "background-image": "url(" + a + ")" })) : 0 == t || 1 == t ? --P : ++P }
    audio = new Audio, W(0), audio.loop = !1, y.on("click", Y), x.mousemove((function(a) {! function(a) { i = x.offset(), t = a.clientX - i.left, e = audio.duration * (t / x.outerWidth()), w.width(t), r = e / 60, o = Math.floor(r), s = Math.floor(e - 60 * o), o < 0 || s < 0 || o < 0 || s < 0 || (o < 10 && (o = "0" + o), s < 10 && (s = "0" + s), isNaN(o) || isNaN(s) ? C.text("--:--") : C.text(o + ":" + s), C.css({ left: t, "margin-left": "-21px" }).fadeIn(0)) }(a) })), x.mouseout(z), x.on("click", G), $(audio).on("timeupdate", J), H.on("click", (function() { W(-1) })), O.on("click", (function() { W(1) })) }));