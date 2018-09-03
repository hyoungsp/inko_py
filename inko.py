###  (c) 2018 Jon Jee, Stanley Park (python)
###  Inko may be freely distributed or modified under the MIT license.



def main():
    # constants variables
    ENGLISH_ALPHABET = "rRseEfaqQtTdwWczxvgASDFGZXCVkoiOjpuPhynbmlYUIHJKLBNM"                         
    KOREAN_ALL = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅁㄴㅇㄹㅎㅋㅌㅊㅍㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣㅛㅕㅑㅗㅓㅏㅣㅠㅜㅡ"     
    KOREAN_INITIAL = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"                     
    KOREAN_NUCLEUS = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"                   
    KOREAN_FINAL = "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"       
    FIRST_VOWEL = 28
    VERY_FIRST_COMBINATION = 44032
    VERY_LAST_COMBINATION = 55203

    FIRST_FINAL_NUM = 12593
    LAST_NUCLEUS_NUM = 12643


    def eng_index(self, en):
        x = {}
        for i in range(len(en)):
            x[en[i]] = i
        return x 

    eng_index = self.eng_index(ENGLISH_ALPHABET)   

    def kor_index(self, kr):
        x = {}
        for i in range(len(kr)):
            x[kr[i]] = i
        return x

    kor_index = self.kor_index(KOREAN_ALL)

    '''
    def korean_generator(self, initial, nucleus, final):
        return String.fromCharCode(44032 + initial * 588 + nucleus * 28 + final + 1)
    '''

    connectableConsonant = {
        'ㄱㅅ': 'ㄳ',
        'ㄴㅈ': 'ㄵ',
        'ㄴㅎ': 'ㄶ',
        'ㄹㄱ': 'ㄺ',
        'ㄹㅁ': 'ㄻ',
        'ㄹㅂ': 'ㄼ',
        'ㄹㅅ': 'ㄽ',
        'ㄹㅌ': 'ㄾ',
        'ㄹㅍ': 'ㄿ',
        'ㄹㅎ': 'ㅀ',
        'ㅂㅅ': 'ㅄ'
    }

    connectableVowel = {
        'ㅗㅏ': 'ㅘ',
        'ㅗㅐ': 'ㅙ',
        'ㅗㅣ': 'ㅚ',
        'ㅜㅓ': 'ㅝ',
        'ㅜㅔ': 'ㅞ',
        'ㅜㅣ': 'ㅟ',
        'ㅡㅣ': 'ㅢ'
    };

    def isVowel(self, e):
        return kor_index[e] >= FIRST_VOWEL

    self._allowDoubleConsonant = False

    def __init__(self, _option):
        option = _option or {}
        self._allowDoubleConsonant = option[allowDoubleConsonant] if allowDoubleConsonant in option else False

    '''
    // constructor
    function Inko(_option) {
        var option = _option || {};
        this._allowDoubleConsonant = typeof option.allowDoubleConsonant !== 'undefined' ?
            option.allowDoubleConsonant : false;
        return this;
    }

    Inko.prototype.config = function(_option) {
        var option = _option || {};
        this._allowDoubleConsonant = typeof option.allowDoubleConsonant !== 'undefined' ?
            option.allowDoubleConsonant : false;
    }

    Inko.prototype.VERSION = '1.0.6';
    '''

    def en2ko(self, eng, _option):
        option = _option or {}

        allowDoubleConsonant = option.allowDoubleConsonant if typeof option.allowDoubleConsonant else False
                
        # self = this

        stateLength = [0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
        transitions = [
            [1, 1, 2, 2], # 0, EMPTY
            [3, 1, 4, 4], # 1, 자
            [1, 1, 5, 2], # 2, 모
            [3, 1, 4, -1], # 3, 자자
            [6, 1, 7, 2], # 4, 자모
            [1, 1, 2, 2], # 5, 모모
            [9, 1, 4, 4], # 6, 자모자
            [9, 1, 2, 2], # 7, 자모모
            [1, 1, 4, 4], # 8, 자모자자
            [10, 1, 4, 4], # 9, 자모모자
            [1, 1, 4, 4], # 10, 자모모자자
        ]

        def last(arr):
            return arr[len(arr) - 1]

        
        def combine(arr):
            group = [];

            for idx, element in enumerate(arr):
                h = KOREAN_ALL[idx]
                if i == 0 or isVowel(last(group)[0]) != isVowel(h):
                    group.append([])
                last(group).append(h)


            for i in range(len(group)):
                w = group[i].join('')
                group[i] = connectableConsonant[w] or connectableVowel[w] or w


            if len(group) == 1:
                return group[0]

            charSet = [KOREAN_INITIAL, KOREAN_NUCLEUS, KOREAN_FINAL]
            
            code = [None for _ in range(len(group))]
            for idx, val in enumerate(group):
                code[idx] = charSet[idx].index(val) 

            if len(code) < 3:
                code.append(-1)

            return self.korean_generator.apply(self, code); # 질문
        
        
        length = eng.length
        last = -1
        result = []
        state = 0
        tmp = []

        def flush():
            if len(tmp) > 0:
                result.append(combine(tmp))
            tmp = []

        for i in range(0, length):
            chr = eng[i]
            cur = eng_index[chr]
            if not cur:
                state = 0
                flush()
                result.append(chr)
            else:
                transition = 2
                c = (KOREAN_ALL[last] or '') + KOREAN_ALL[cur]
                lastIsVowel = isVowel(KOREAN_ALL[last])
                if not curIsVowel:
                    if lastIsVowel:
                        transition = 1 if KOREAN_ALL[cur] in 'ㄸㅃㅉ' else 0
                    if state == 1 and not allowDoubleConsonant:
                        transition = 1
                elif lastIsVowel:
                    transition = 2 if connectableVowel[c] else 3
                else:
                    transition = 2
                nxtState = transitions[state][transition]
                tmp.append(cur)
                diff = len(tmp) - stateLength[nxtState]
                if diff:
                    portion = tmp[:diff+1]
                    del tmp[:diff+1]
                    result.append(combine(portion))
        flush()
        return result.join('')   

    def ko2en(inp):
        result = ''
        if not inp: 
            return result
        _separate = [-1, -1, -1, -1, -1];

        for i in range(len(inp)): 
            _korean = inp[i]
            _code = ord(_korean)
            # 가 ~ 힣 사이에 있는 한글이라면
            if (_code >= VERY_FIRST_COMBINATION && _code <= VERY_LAST_COMBINATION) or (_code >= FIRST_FINAL_NUM && _code <= LAST_NUCLEUS_NUM):
                _separate = self.한글분리(_korean)
            
            # 한글이 아니라면
            else 
                result += _korean
                # 분리 배열 초기화
                _separate = [-1, -1, -1, -1, -1]
            
            for j in range(len(_separate)):
                if _separate[j] != -1:
                    result += ENGLISH_ALPHABET[_separate[j]]
            
        return result;
    

    # 초성, 중성, 종성의 charCode를 받아서 합친 한글의 charCode를 반환함
    def korean_generator(first, middle, last): 
        return String.fromCharCode(44032 + first * 588 + middle * 28 + last + 1);
    

    # 한글 입력값으로 받아서 초성, 중성, 종성 분리해줌
    def korean_separator(_korean):
        code = ord(_korean)

        if (code >= VERY_FIRST_COMBINATION && code <= VERY_LAST_COMBINATION): 
            _first = (code - VERY_FIRST_COMBINATION) // 588
            _middle = (code - VERY_FIRST_COMBINATION - _first * 588) // 28
            _last = code - VERY_FIRST_COMBINATION - _first * 588 - _middle * 28 - 1;
            _middle1, _middle2 = -1, -1
            _last1, _last2 = -1, -1

            if _middle == _middle.index("ㅘ"):
                _middle1, _middle2 = KOREAN_ALL.index("ㅗ"), KOREAN_ALL.index("ㅏ");
            elif _middle == _middle.index("ㅙ"):
                _middle1, _middle2 = KOREAN_ALL.index("ㅗ"), KOREAN_ALL.index("ㅐ");
            elif _middle == _middle.index("ㅚ"):
                _middle1, _middle2 = KOREAN_ALL.index("ㅗ"), KOREAN_ALL.index("ㅣ");
            elif _middle == _middle.index("ㅝ"):
                _middle1, _middle2 = KOREAN_ALL.index("ㅜ"), KOREAN_ALL.index("ㅓ");
            elif _middle == _middle.index("ㅞ"):
                _middle1, _middle2 = KOREAN_ALL.index("ㅜ"), KOREAN_ALL.index("ㅔ");
            elif _middle == _middle.index("ㅟ"):
                _middle1, _middle2 = KOREAN_ALL.index("ㅜ"), KOREAN_ALL.index("ㅣ");
            elif _middle == _middle.index("ㅢ"):
                _middle1, _middle2= KOREAN_ALL.index("ㅡ"), KOREAN_ALL.index("ㅣ");

            if _last == KOREAN_FINAL.index("ㄳ"):
                _last1, _last2 = KOREAN_ALL.index("ㄱ"), KOREAN_ALL.index("ㅅ");
            elif _last == KOREAN_FINAL.index("ㄵ"):
                _last1, _last2 = KOREAN_ALL.index("ㄴ"), KOREAN_ALL.index("ㅈ");
            elif _last == KOREAN_FINAL.index("ㄶ"):
                _last1, _last2 = KOREAN_ALL.index("ㄴ"), KOREAN_ALL.index("ㅎ");
            elif _last == KOREAN_FINAL.index("ㄺ"):
                _last1, _last2 = KOREAN_ALL.index("ㄹ"), KOREAN_ALL.index("ㄱ");
            elif _last == KOREAN_FINAL.index("ㄻ"):
                _last1, _last2 = KOREAN_ALL.index("ㄹ"), KOREAN_ALL.index("ㅁ");
            elif _last == KOREAN_FINAL.index("ㄼ"):
                _last1, _last2 = KOREAN_ALL.index("ㄹ"), KOREAN_ALL.index("ㅂ");
            elif _last == KOREAN_FINAL.index("ㄽ"):
                _last1, _last2 = KOREAN_ALL.index("ㄹ"), KOREAN_ALL.index("ㅅ");
            elif _last == KOREAN_FINAL.index("ㄾ"):
                _last1, _last2 = KOREAN_ALL.index("ㄹ"), KOREAN_ALL.index("ㅌ");
            elif _last == KOREAN_FINAL.index("ㄿ"):
                _last1, _last2 = KOREAN_ALL.index("ㄹ"), KOREAN_ALL.index("ㅍ");
            elif _last == KOREAN_FINAL.index("ㅀ"):
                _last1, _last2 = KOREAN_ALL.index("ㄹ"), KOREAN_ALL.index("ㅎ");
            elif _last == KOREAN_FINAL.index("ㅄ"):
                _last1, _last2 = KOREAN_ALL.index("ㅂ"), KOREAN_ALL.index("ㅅ");

            # 복모음이 아니라면
            if _middle2 == -1:
                _middle1 = KOREAN_ALL.index(KOREAN_NUCLEUS[_middle])

            # 복자음이 아니라면
            if _last2 == -1:
                _last1 = KOREAN_ALL.index(KOREAN_FINAL[_last])

            return [_first, _middle1, _middle2, _last1, _last2]

         elif code >= FIRST_FINAL_NUM and code <= LAST_NUCLEUS_NUM:
            if KOREAN_INITIAL.index(_korean) > -1: 
                _initial = KOREAN_ALL.indexOf(_korean)
                return [_initial, -1, -1, -1, -1]
            elif (KOREAN_NUCLEUS.index(_korean) > -1):
                _middle = KOREAN_NUCLEUS.index(_korean)
                _middle1, _middle2 = _middle, -1
                if _middle == KOREAN_NUCLEUS.index("ㅘ"):
                    _middle1, _middle2 = KOREAN_ALL.index("ㅗ"), KOREAN_ALL.index("ㅏ")
                elif _middle == KOREAN_NUCLEUS.index("ㅙ"):
                    _middle1, _middle2 = KOREAN_ALL.index("ㅗ"), KOREAN_ALL.index("ㅐ")
                elif _middle == KOREAN_NUCLEUS.index("ㅚ"):
                    _middle1, _middle2 = KOREAN_ALL.index("ㅗ"), KOREAN_ALL.index("ㅣ")
                elif _middle == KOREAN_NUCLEUS.index("ㅝ"):
                    _middle1, _middle2 = KOREAN_ALL.index("ㅜ"), KOREAN_ALL.index("ㅓ")
                elif _middle == KOREAN_NUCLEUS.index("ㅞ"):
                    _middle1, _middle2 = KOREAN_ALL.index("ㅜ"), KOREAN_ALL.index("ㅔ")
                elif _middle == KOREAN_NUCLEUS.index("ㅟ"):
                    _middle1, _middle2 = KOREAN_ALL.index("ㅜ"), KOREAN_ALL.index("ㅣ")
                elif _middle == KOREAN_NUCLEUS.index("ㅢ"):
                    _middle1, _middle2 = KOREAN_ALL.index("ㅡ"), KOREAN_ALL.index("ㅣ")

                # 복모음이 아니라면
                if _middle2 == -1:
                    _middle1 = KOREAN_ALL.index(KOREAN_NUCLEUS[_middle])

                return [-1, _middle1, _middle2, -1, -1]
            
        
        return [-1, -1, -1, -1, -1]
    



    def isKorean(char):
        if len(char) > 1:
            # throw new Error("한글자가 아닙니다.")
        return /[ㄱ-ㅎ|ㅏ-ㅣ|기-힣]/.test(char) 
    

    '''
    # CommonJS module
    if (typeof exports !== 'undefined') {
        if (typeof module !== 'undefined' && module.exports) {
            exports = module.exports = Inko;
        }
        exports.Inko = Inko;
    }

    # Register as an anonymous AMD module
    if (typeof define === 'function' && define.amd) {
        define([], function () {
            return Inko;
        });
    }

    # if there is a importsScrips object define chance for worker
    // allows worker to use full Chance functionality with seed
    if (typeof importScripts !== 'undefined') {
        inko = new Inko();
        self.Inko = Inko;
    }

    # If there is a window object, that at least has a document property,
    # instantiate and define chance on the window
    if (typeof window === "object" && typeof window.document === "object") {
        window.Inko = Inko;
        window.inko = new Inko();
    }
    '''

      


if __name__ == "__main__":
    main()
