from tregex import Tregex as T

# 기본 문법

용언구 = T('VP')
명사수식_용언구 = T('VP_MOD')
형용사구인_용언구 = T('VP < VA')
형용사구가_아닌_용언구 = T('VP !< VA')
동사구인_용언구 = T('VP < VV|VX')
형용사가_수식하는_명사구 = T('NP $ VP_MOD')
쉼표로_종결되는_접속명사구 = T('NP_CNJ <<- ,')
쉼표_외로_종결되는_접속명사구 = T('NP_CNJ <<- !,')
문장_안_문장 = T('S < S')

# 복합 문법

주어_동사_문장 = T('S < NP_SBJ < VP')
주어절_수식있는_문장 = T('S < ')
복합명사구 = T('NP < ( NP $ NP )')

# advanced topic : 연결어미

연결어미_선행절
연결어미_후행절
연결어미_선행절의_주절
연결어미_후행절의_주절

# advanced topic : TBA



