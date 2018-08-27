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
    const ㄱ = 12593
    const ㅣ = 12643

    '''
    constructor
    function Inko() {
        return this;
    }
    '''

    INKO_PYTHON_VERSION = '1.0.0'

    def korean_generator(self, initial, nucleus, final):
        return String.fromCharCode(44032 + initial * 588 + nucleus * 28 + final + 1)
    

    def en2ko(self, input):
        result = ''
        if not input:
            return result

        _initial, _nucleus, _final = -1, -1, -1

        for i in range(len(input)):
            char = input[i]
            index = char in ENGLISH_ALPHABET and ENGLISH_ALPHABET.index(char)
            _korean = KOREAN_ALL[index]

            if not index:
                # condier the remaining korean
                if _initial != -1:
                    if _nucleus != -1: result += self.korean_generator(_initial, _nucleus, _final)
                    else: result += KOREAN_INITIAL[_initial]

                else:
                    if _nucleus != -1: result += KOREAN_NUCLEUS[_nucleus]
                    else if _final != -1: result += KOREAN_FINAL[_final]
                _initial, _nucleus, _final = -1, -1, -1
                result += char

            else if index < FIRST_VOWEL:
                if _nucleus != -1:
                    if _initial == -1:
                        result += KOREAN_NUCLEUS[_nucleus]
                        _nucleus = -1
                        _initial = KOREAN_INITIAL.index(_korean)

                    else:
                        if _nucleus == -1:
                            _nucleus = KOREAN_NUCLEUS.index(_korean)
                            if _nucleus == -1:
                                result += self.korean_generator(_initial, _nucleus, _final)
                                _initial = KOREAN_INITIAL.index(_korean)
                                _nucleus = -1

                        # 복자음 처리
                        elif _final === KOREAN_FINAL.index('ㄱ') and _korean == 'ㅅ': 
                            _final = KOREAN_FINAL.index('ㄳ')   # 복자음 ㄳ
                        elif _final === KOREAN_FINAL.index('ㄴ') and _korean == 'ㅈ': 
                            _final = KOREAN_FINAL.index('ㄵ')   # 복자음 ㄵ
                        elif _final === KOREAN_FINAL.index('ㄴ') and _korean == 'ㅎ': 
                            _final = KOREAN_FINAL.index('ㄶ');  # 복자음 ㄶ
                        elif _final === KOREAN_FINAL.index('ㄹ') and _korean == 'ㄱ': 
                            _final = KOREAN_FINAL.index('ㄺ');  # 복자음 ㄺ
                        elif _final === KOREAN_FINAL.index('ㄹ') and _korean == 'ㅁ': 
                            _final = KOREAN_FINAL.index('ㄻ')   # 복자음 ㄻ
                        elif _final === KOREAN_FINAL.index('ㄹ') and _korean == 'ㅂ': 
                            _final = KOREAN_FINAL.index('ㄼ')   # 복자음 ㄼ
                        elif _final === KOREAN_FINAL.index('ㄹ') and _korean == 'ㅅ': 
                            _final = KOREAN_FINAL.index('ㄽ')   # 복자음 ㄽ
                        elif _final === KOREAN_FINAL.index('ㄹ') and _korean == 'ㅌ': 
                            _final = KOREAN_FINAL.index('ㄾ')   # 복자음 ㄾ
                        elif _final === KOREAN_FINAL.index('ㄹ') and _korean == 'ㅍ': 
                            _final = KOREAN_FINAL.index('ㄿ')   # 복자음 ㄿ
                        elif _final === KOREAN_FINAL.index('ㄹ') and _korean == 'ㅎ': 
                            _final = KOREAN_FINAL.index('ㅀ')   # 복자음 ㅀ
                        elif _final === KOREAN_FINAL.index('ㅂ') and _korean == 'ㅅ': 
                            _final = KOREAN_FINAL.index('ㅄ')   # 복자음 ㅄ
                        # 복자음이 아니므로 초성으로 처리
                        else:
                            result += self.korean_generator(_initial, _nucleus, _final)
                            _nucleus = -1, _final = -1
                            _initial = KOREAN_INITIAL.index(_korean)
                        
                # 중성이 없음
                else: 
                    # 초성이 없음
                    if _initial == -1: _initial = KOREAN_INITIAL.index(_korean)
                    # 초성이 있는데 또 자음이 들어옴
                    else:
                        result += KOREAN_INITIAL[_initial]
                        _initial = KOREAN_INITIAL.index(_korean)
                    

            # 모음이라면
            else:
                if _final != -1:						# (앞글자 종성), 초성+중성
                    // 복자음 다시 분해
                    tmp_initial = -1;			                               # 임시 초성
                    if _final == KOREAN_FINAL.index('ㄳ') 				# ㄱ / ㅅ
                        _final = KOREAN_FINAL.index('ㄱ')
                        tmp_initial = KOREAN_FINAL.index('ㅅ')
                    else if _final == KOREAN_FINAL.index('ㄵ') 		# ㄴ / ㅈ
                        _final = KOREAN_FINAL.index('ㄴ')
                        tmp_initial = KOREAN_FINAL.index('ㅈ')
                    else if _final == KOREAN_FINAL.index('ㄶ') 			# ㄴ / ㅎ
                        _final = KOREAN_FINAL.index('ㄴ')
                        tmp_initial = KOREAN_FINAL.index('ㅎ')
                    else if _final == KOREAN_FINAL.index('ㄺ') 			# ㄹ / ㄱ
                        _final = KOREAN_FINAL.index('ㄹ')
                        tmp_initial = KOREAN_FINAL.index('ㄱ')
                    else if _final == KOREAN_FINAL.index('ㄻ') 			# ㄹ / ㅁ
                        _final = KOREAN_FINAL.index('ㄹ')
                        tmp_initial = KOREAN_FINAL.index('ㅁ')
                    else if _final == KOREAN_FINAL.index('ㄼ') 			# ㄹ / ㅂ
                        _final = KOREAN_FINAL.index('ㄹ')
                        tmp_initial = KOREAN_FINAL.index('ㅂ')
                    else if _final == KOREAN_FINAL.index('ㄽ') 			# ㄹ / ㅅ
                        _final = KOREAN_FINAL.index('ㄹ')
                        tmp_initial = KOREAN_FINAL.index('ㅅ')
                    else if _final == KOREAN_FINAL.index('ㄾ') 			# ㄹ / ㅌ
                        _final = KOREAN_FINAL.index('ㄹ')
                        tmp_initial = KOREAN_FINAL.index('ㅌ')
                    else if _final == KOREAN_FINAL.index('ㄿ') 			# ㄹ / ㅍ
                        _final = KOREAN_FINAL.index('ㄹ')
                        tmp_initial = KOREAN_FINAL.index('ㅍ')
                    else if _final == KOREAN_FINAL.index('ㅀ') 			# ㄹ / ㅎ
                        _final = KOREAN_FINAL.index('ㄹ')
                        tmp_initial = KOREAN_FINAL.index('ㅎ')
                    else if _final == KOREAN_FINAL.index('ㅄ')			# ㅂ / ㅅ
                        _final = KOREAN_FINAL.index('ㅂ')
                        tmp_initial = KOREAN_FINAL.index('ㅅ')
                    
                    # 복자음 아님 
                    else: 
                        tmp_initial = KOREAN_INITIAL.indexOf(KOREAN_FINAL[_final])
                        _final = -1
                    
                    # 앞글자가 초성 + 중성 + (종성)
                    if _초성 != -1:
                        result += this.한글생성(_초성, _중성, _종성);
                    # 복자음만 있음
                    else: 
                        result += 종성[_종성];
                    _초성 = 새초성;
                    _중성 = -1;
                    _종성 = -1;
      


if __name__ == "__main__":
    main()
