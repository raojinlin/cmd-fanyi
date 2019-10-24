__all__ = ['baidu_translate_sign']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['n', 'sign'])
@Js
def PyJsHoisted_n_(r, o, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'o':o, 'r':r, 'this':this}, var)
    var.registers(['a', 'o', 'r', 't'])
    #for JS loop
    var.put('t', Js(0.0))
    while (var.get('t')<(var.get('o').get('length')-Js(2.0))):
        try:
            var.put('a', var.get('o').get((var.get('t')+Js(2.0))))
            if (var.get('a')>=Js('a')):
                var.put('a', (var.get('a').callprop('charCodeAt', Js(0.0))-Js(87.0)))
            else:
                var.put('a', var.get('Number')(var.get('a')))
            if PyJsStrictEq(var.get('o').get((var.get('t')+Js(1.0))),Js('+')):
                var.put('a', PyJsBshift(var.get('r'),var.get('a')))
            else:
                var.put('a', (var.get('r')<<var.get('a')))
            if PyJsStrictEq(var.get('o').get(var.get('t')),Js('+')):
                var.put('r', ((var.get('r')+var.get('a'))&Js(4294967295.0)))
            else:
                var.put('r', (var.get('r')^var.get('a')))
        finally:
                var.put('t', Js(3.0), '+')
    return var.get('r')
PyJsHoisted_n_.func_name = 'n'
var.put('n', PyJsHoisted_n_)
@Js
def PyJsHoisted_sign_(r, l, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'l':l, 'r':r, 'this':this}, var)
    var.registers(['p', 'e', 'D', 'c', 'm', 'C', 'l', 'g', 'F', 'd', 'o', 'b', 't', 'S', 'h', 'u', 'A', 'f', 'r', 's'])
    var.put('o', var.get('r').callprop('match', JsRegExp('/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]/g')))
    if PyJsStrictEq(var.get(u"null"),var.get('o')):
        var.put('t', var.get('r').get('length'))
        if (var.get('t')>Js(30.0)):
            var.put('r', (((Js('')+var.get('r').callprop('substr', Js(0.0), Js(10.0)))+var.get('r').callprop('substr', (var.get('Math').callprop('floor', (var.get('t')/Js(2.0)))-Js(5.0)), Js(10.0)))+var.get('r').callprop('substr', (-Js(10.0)), Js(10.0))))
    else:
        var.put('e', var.get('r').callprop('split', JsRegExp('/[\\uD800-\\uDBFF][\\uDC00-\\uDFFF]/')))
        var.put('h', var.get('e').get('length'))
        var.put('f', Js([]))
        #for JS loop
        var.put('C', Js(0.0))
        while (var.get('h')>var.get('C')):
            try:
                if PyJsStrictNeq(Js(''),var.get('e').get(var.get('C'))):
                    var.get('f').get('push').callprop('apply', var.get('f'), var.get('a')(var.get('e').get(var.get('C')).callprop('split', Js(''))))
                if PyJsStrictNeq(var.get('C'),(var.get('h')-Js(1.0))):
                    var.get('f').callprop('push', var.get('o').get(var.get('C')))
            finally:
                    (var.put('C',Js(var.get('C').to_number())+Js(1))-Js(1))
        var.put('g', var.get('f').get('length'))
        if (var.get('g')>Js(30.0)):
            var.put('r', ((var.get('f').callprop('slice', Js(0.0), Js(10.0)).callprop('join', Js(''))+var.get('f').callprop('slice', (var.get('Math').callprop('floor', (var.get('g')/Js(2.0)))-Js(5.0)), (var.get('Math').callprop('floor', (var.get('g')/Js(2.0)))+Js(5.0))).callprop('join', Js('')))+var.get('f').callprop('slice', (-Js(10.0))).callprop('join', Js(''))))
    var.put('u', (var.get('l') or Js('')))
    var.put('d', var.get('u').callprop('split', Js('.')))
    var.put('m', (var.get('Number')(var.get('d').get('0')) or Js(0.0)))
    var.put('s', (var.get('Number')(var.get('d').get('1')) or Js(0.0)))
    var.put('S', Js([]))
    var.put('c', Js(0.0))
    #for JS loop
    var.put('v', Js(0.0))
    while (var.get('v')<var.get('r').get('length')):
        try:
            var.put('A', var.get('r').callprop('charCodeAt', var.get('v')))
            if (Js(128.0)>var.get('A')):
                var.get('S').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), var.get('A'))
            else:
                if (Js(2048.0)>var.get('A')):
                    var.get('S').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), ((var.get('A')>>Js(6.0))|Js(192.0)))
                else:
                    if ((PyJsStrictEq(Js(55296.0),(Js(64512.0)&var.get('A'))) and ((var.get('v')+Js(1.0))<var.get('r').get('length'))) and PyJsStrictEq(Js(56320.0),(Js(64512.0)&var.get('r').callprop('charCodeAt', (var.get('v')+Js(1.0)))))):
                        var.put('A', ((Js(65536.0)+((Js(1023.0)&var.get('A'))<<Js(10.0)))+(Js(1023.0)&var.get('r').callprop('charCodeAt', var.put('v',Js(var.get('v').to_number())+Js(1))))))
                        var.get('S').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), ((var.get('A')>>Js(18.0))|Js(240.0)))
                        var.get('S').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), (((var.get('A')>>Js(12.0))&Js(63.0))|Js(128.0)))
                    else:
                        var.get('S').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), ((var.get('A')>>Js(12.0))|Js(224.0)))
                        var.get('S').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), (((var.get('A')>>Js(6.0))&Js(63.0))|Js(128.0)))
                    var.get('S').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), ((Js(63.0)&var.get('A'))|Js(128.0)))
        finally:
                (var.put('v',Js(var.get('v').to_number())+Js(1))-Js(1))
    var.put('p', var.get('m'))
    var.put('F', Js('+-a^+6'))
    var.put('D', Js('+-3^+b+-f'))
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get('S').get('length')):
        try:
            PyJsComma(var.put('p', var.get('S').get(var.get('b')), '+'),var.put('p', var.get('n')(var.get('p'), var.get('F'))))
        finally:
                (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    var.put('p', var.get('n')(var.get('p'), var.get('D')))
    var.put('p', var.get('s'), '^')
    ((Js(0.0)>var.get('p')) and var.put('p', ((Js(2147483647.0)&var.get('p'))+Js(2147483648.0))))
    var.put('p', Js(1000000.0), '%')
    return ((var.get('p').callprop('toString')+Js('.'))+(var.get('p')^var.get('m')))
PyJsHoisted_sign_.func_name = 'sign'
var.put('sign', PyJsHoisted_sign_)
pass
pass
pass


# Add lib to the module scope
baidu_translate_sign = var.to_python()
