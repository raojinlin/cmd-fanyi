function toArray(text) {
    if (Array.isArray(text)) {
        let result = Array(text.length);
        for (let i = 0; i < text.length; i++) {
            result[i] = text[i];
        }

        return result
    }

    return Array.from(text)
}

function encodeByKey(num, key) {
    for (let t = 0; t < key.length - 2; t += 3) {
        let a = key[t + 2];

        if (a >= 'a') {
            a = a.charCodeAt(0) - 87;
        } else {
            a = Number(a);
        }


        if (key[t + 1] === '+') {
            a = num >>> a;
        } else {
            a = num << a;
        }


        if ("+" === key[t]) {
            num = num + a & 4294967295;
        } else {
            num = num ^ a;
        }
    }

    return num
}

function generateToken(text, gtk) {
    let outUtf8 = text.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
    if (null === outUtf8) {
        if (text.length > 30) {
            text =
                text.substr(0, 10) +
                text.substr(Math.floor(text.length / 2) - 5, 10) +
                text.substr(-10, 10)
        }
    } else {
        let chars = text.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/);
        let charsLength = chars.length;
        let reforms = [];

        for (let i = 0; charsLength > i; i++) {
            if ("" !== chars[i]) {
                reforms.push.apply(reforms, toArray(chars[i].split("")))
            }

            if (i !== charsLength - 1) {
                reforms.push(outUtf8[i]);
            }
        }

        if (reforms.length > 30) {
            text =
                reforms.slice(0, 10).join("") +
                reforms.slice(
                    Math.floor(reforms.length / 2) - 5,
                    Math.floor(reforms.length / 2) + 5
                ).join("") +
                reforms.slice(-10).join("")
        }
    }
    let gtkArray = gtk.split(".");
    let prefix = Number(gtkArray[0]) || 0;
    let suffix = Number(gtkArray[1]) || 0;
    let s = [];

    for (let v = 0; v < text.length; v++) {
        let a = text.charCodeAt(v);
        if (128 > a) {
            s.push(a)
        } else {
            if (2048 > a) {
                s.push(a >> 6 | 192);
            } else {
                if (55296 === (64512 & a) && v + 1 < text.length && 56320 === (64512 & text.charCodeAt(v + 1))) {
                    a = 65536 + ((1023 & a) << 10) + (1023 & text.charCodeAt(++v));
                    s.push(a >> 18 | 240);
                    s.push(a >> 12 & 63 | 128);
                } else {
                    s.push(a >> 12 | 224)
                }

                s.push(a >> 6 & 63 | 128)
            }

            s.push(63 & a | 128)
        }
    }

    let key1 = "+-a^+6";
    let key2 = "+-3^+b+-f";
    let p = prefix;
    for (let b = 0; b < s.length; b++) {
        p += s[b];
        p = encodeByKey(p, key1);
    }

    p = encodeByKey(p, key2);
    p ^= suffix;

    if (p < 0) {
        p = (2147483647 & p) + 2147483648
    }

    p %= 1e6;

    return p.toString() + "." + (p ^ prefix)
}

// console.log(encodeByKey(123456, '+-a^6'));
const gtk = '320305.131321201';
console.log('😀', generateToken('😀', gtk) === "137522.457219");
console.log(generateToken('hello', gtk) === '54706.276099');
console.log(generateToken('hello world are you ok ? this is funny.', gtk));
console.log(generateToken('你好', gtk));
console.log(generateToken('抽刀断水水更流，举杯消愁愁更愁。', gtk));
// console.log(encodeByKey(320305, '+-a^+6'));
