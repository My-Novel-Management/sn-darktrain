# -*- cofing: utf-8 -*-
'''
Stage: xxx
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def sc_1(w: World):
    tada = w.get('tada')
    megu = w.get('megu')
    return w.scene("# 皐月０５１１",
            w.tag.title("皐月　０５１１"),
            tada.do("ホームの間に架けられた跨線橋《こせんきょう》の股から、山の麓《ふもと》のそれがすっかり葉桜になってしまったのが分かった"),
            tada.do("スーツを着込た人たちが年齢も性別も関係なくただ几帳面に列を作って待っている。それを傍目に、多田純一《ただじゅんいち》は足元に落ちていたゴミをチリトリに収めていく。真新しい緑の作業服の右足側がまくれ上がり、彼のそれが人間のものではなく単なる木の模造品であることが誰の目にも明白だったが、それを気にかける者はいない"),
            tada.talk("おはようございます。今日もご苦労さまです"),
            tada.do("多田は左足を踏ん張り、体を彼女の方へと向ける"),
            megu.look("膝頭が収まる程度の長さのスカートに両手で持つ大きめの鞄、胸元がＶ字に切られた淡いグレィのスーツの生地は皺《しわ》もなく、そこから覗く白い喉元から丸い顎《あご》、大きめの口は笑った時に右側に笑窪《えくぼ》が生まれる。髪は肩の上でちょうどカーブしていて、多田にはそれが地毛なのか染めたものか判別できなかったが、彼女の性格を思わせる茶色がかった柔らかなものだった"),
            megu.talk("……あ、はい"),
            tada.do("いつも挨拶くらいはまともに返せればと思うのだが、彼女に見つめられるとどうにも顔を上げていられず、多田は俯《うつむ》いて「ああ」とか「はい」とかそんな声を吐き出すだけだ"),
            tada.do("黒光りした鉄の塊がまるで亡者の悲鳴のような金属音を立ててホームに滑り込んでくる", "&"),
            tada.do("ドアが開き、待っていた人の列があっという間にその車体に吸い込まれていく。列の最後の方だった彼女は駅員に背中から押し込まれ、それでも何とか車内に乗り込むと、多田に苦笑を送った"),
            tada.do("瞬間、ドアは閉じた", "&"),
            tada.do("けたたましい発車ベルに続いて、ゆっくりと重くなった列車が動き出す"),
            tada.do("多田は仕事に戻る"),
            tada.do("と、彼女が立っていた辺りだった。そこに小さな赤いものが落ちていた。拾い上げてみると、小指の先ほどの大きさのネジだ"),
            tada.do("――彼女のものだろうか"),
            tada.do("誰も、見ていない"),
            tada.do("それを確認してから、作業服のポケットにそっと滑り込ませた"),
            tada.talk("――昨年の過労死の統計について厚労省より発表がありましたが"),
            tada.do("雑音混じりの低い男性の声が、ニュースを読み上げている。ラジオからのものだ"),
            tada.do("ベンチを見れば、ポータブルラジオを鳴らしながらスマートフォンを操作する、無精髭の男がいた。男の姿は毎日のように確認しているが、何をしている風でもない。多田は一歩間違えていれば自分の数十年後の姿だったかも知れないと思い、箒《ほうき》をせわしなく動かした"),
            )

def sc_2(w: World):
    tada, megu = w.get('tada'), w.get('megu')
    man1 = w.get('man1')
    death = w.get('death')
    return w.scene("# 水無月０６０５",
            w.tag.title("水無月　０６０５"),
            tada.do("その日は朝から小雨だった", "&"),
            megu.do("ホームで列車を待っていた彼女は言うことを聞かない髪の毛を押さえて、"),
            megu.talk("湿気と蜘蛛だけは昔から苦手なんです"),
            tada.do("と笑った"),
            tada.do("その笑顔一つで、多田はホームに漂う空気がすうっと軽くなる気がした。おそらく会社でもそういう存在なのだろう。彼女と一緒に仕事ができる人間たちが少し羨ましい"),
            man1.talk("あぁ、もう……くそ"),
            tada.do("そんな多田の本心を、誰かが代弁した訳ではない"),
            tada.do("咳き込みながら、ネクタイを緩めた男性が階段を上がってくる。隈のある目がぎょろりと動いて、土気色した顔で彼を睨みつけ、再び咳き込んで背中を大きく丸めた", "&"),
            tada.do("男性はそのままホームにうずくまり、横たわる。声も上げず、そのうちに動かなくなる"),
            tada.do("僅かに残っていた列車を待つ人々は、けれど誰一人として彼を気にしない", "&"),
            tada.do("すぐに複数の駅員がやってきて、男性の周りに集まる"),
            tada.do("救急車をもう呼んだのだろうか"),
            tada.do("そんな多田の心配をよそに、二、三言葉を交わすと駅員たちは男性を担ぎ上げ、跨線橋を渡っていく。向こう側のホームにはいつ動いているのか分からない貨物列車が停まっていたが、担がれた男性はそのまま駅員たちの手で、それに連結された天井のない箱型の貨物台の前まで運ばれ、"),
            tada.talk("せーの"),
            tada.do("無造作に投げ入れられた"),
            tada.do("かすかに金属音が響いた気がするが、やはり誰も気にしていない"),
            death.talk("あいつはもうダメだ"),
            tada.do("そう言うとおもむろにベンチの男は立ち上がり、さっき男が倒れた場所に向かう。そこには拳大のくるくると丸まった黒い何かが落ちていたが、確認するより早く、男が拾い上げ、そのまま振り返ることなく階段を降りて行ってしまった"),
            )

def sc_3(w: World):
    tada, megu = w.get('tada'), w.get('megu')
    return w.scene("# 文月０７０７",
            w.tag.title("文月　０７０７"),
            tada.talk("――今日は七夕ですが、夜は分厚い雲で天の川が隠されてしまいそうですね"),
            tada.do("ベンチ男のポータブルラジオからは彦星と織姫に諦めろという通告がされていた"),
            megu.talk("今朝も、がんばってますね"),
            tada.do("振り返ると彼女だった。いつもより随分と早い"),
            tada.do("何一つ心の用意をしていなかった多田は咄嗟のことに手にしていた箒を取り落としてしまう"),
            megu.talk("実は今朝のオフィス清掃の任を申し付けられまして。わたしも箒とチリトリマンです"),
            tada.do("失敗してしまった、というのを誤魔化すためか、彼女はくしゃっとした笑顔を作り、多田が落としてしまった箒を拾ってくれる。しゃがみこんだ彼女が見上げてその笑窪が零れそうだと思ったが、じっと見つめる訳にもいかず、すぐに視線を彼方に向けてしまう"),
            tada.do("今日の彼女は髪をきゅっと後ろで括り、普段よりもチークやアイシャドウが濃い。隣に彼女が立つと淡い柑橘系の香りが漂った"),
            megu.talk("多田さん、て言うんですね"),
            tada.do("作業服の名札に、そう書いてあった"),
            tada.do("彼女から手渡しで箒を受け取ってしまったことで、多田は唾を呑み込んだ"),
            megu.talk("わたしは日嵐《ひがらし》って言うんです。日に嵐でヒガラシ。でもそう呼ばれるのあまり好きじゃなくて、友達には恵《めぐみ》って最初から呼んでもらうんです。だから上司にいつもヒガラシクンって呼ばれると、背筋が凍っちゃって"),
            tada.do("それは彼女にとって面白い話なのだろう。多田は自分の名前が認識され、それと同時に彼女の名前が「日嵐恵」と言うのだと知ることができて胸が苦しくなった"),
            megu.talk("この時間少し空いてるんですね。大発見"),
            tada.do("彼女はやってきた列車に乗り込む。小さく手を振り返す様をホームで見送りながら多田は箒を動かすが、右手にその感触がなく、再び箒を落としてしまったことに気づいて視線を落とす"),
            tada.do("と、そこにはまた小さな赤い部品が転がっていた"),
            tada.do("今度は小さなベアリングのようだった"),
            w.br(),
            tada.do("その日から、日嵐恵は時々早い時刻にホームに現れた"),
            tada.do("彼女の仕事のことはよく分からなかったが、それでもギリギリにやってきて挨拶だけしか交せないよりも、僅かでいいので彼女の声が聞けることが単純に嬉しかった"),
            )

def sc_4(w: World):
    tada, megu = w.get('tada'), w.get('megu')
    man, death = w.get('man1'), w.get('death')
    return w.scene("# 長月０９０４",
            w.tag.title("長月　０９０４"),
            tada.do("カレンダーが九月に変わっても、まだ夏の暑さは過ぎ去ってはくれなかった"),
            tada.talk("――昨日発生した台風十八号の予想進路は……"),
            tada.do("ベンチに座っている男はポータブルラジオの音量を上げたり下げたりしながら、スマートフォンを親指で器用に操っていた"),
            tada.do("発車のベルに似た着信音で男は電話に出て立ち上がる"),
            death.talk("お待ちしてました。はい。いよいよ、決心つきました？"),
            tada.do("多田は掃除をする振りをして、男が無精髭を弄びながら応対しているのをそっと観察する。今までは単なるホームレスの類の人種だろうと思っていたのだが、電話の態度はどうにも高圧的だ"),
            death.talk("そうですよ。もうそこまで来てるんですから、やらなきゃダメですよ？　決めましょう。明日？　まだそんなことを言ってる。ご自分の状況ってもの、分かってますかね？"),
            tada.do("明日、という言葉に多田の頭に真っ先に浮かんだのは借金の取り立て屋だった。それなら日がなベンチでスマートフォンを弄っていることも説明がつくような気がする"),
            death.talk("じゃ、西口のところで待ってますよ"),
            tada.do("電話を切ると、男はポータブルラジオを手に、階段を降りていく"),
            tada.do("すれ違い様に多田に視線を投げたような気がしたが、清掃作業に戻った彼がそれを確認する術はなかった"),
            )

def sc_5(w: World):
    tada, megu = w.get('tada'), w.get('megu')
    return w.scene("# 神無月１０２３",
            w.tag.title("神無月　１０２３"),
            megu.talk("来週、誕生日なんです"),
            tada.do("先週末にその言葉を聞いて、今日、多田はその手に彼には似つかわしくない小さな紙袋を持っていた。赤いリボンで何とか蝶々結びをしてみたが、いざこうして人前に晒してみると自分のセンスのなさを嘆くしかない"),
            tada.do("実は多田はこれまでにも何度か拾い集めたネジや金属部品の類を彼女に返そうと思ったのだが、こっそりと収集していたことに対しての幾らかの罪悪感と、何より彼女がそれを大切に思っているのかどうか判断がつかず、結局ずるずるとこんな季節まで引き伸ばしてしまった"),
            tada.do("彼女はまだ来ない"),
            tada.do("紙袋の中には他にも小さな星型の砂が詰められたガラス製の小瓶を忍ばせていた。以前日嵐恵が話してくれたのだけれど、彼女は小さな頃、「魔法使い」になりたかったそうだ。アニメで見かけた魔法の杖を振り回して闘うその姿に、自分にとっての「スーパーマン」的存在だと、教えてくれた"),
            tada.do("いつの間に現れたのだろう"),
            tada.do("そう。たぶん彼女は、日嵐恵だ"),
            tada.do("ただ髪はぼさぼさで、化粧もなんだか慌ただしく塗っただけ、といった感じ。その上、足首までの長い紺のパンツスーツだった"),
            tada.talk("……あ"),
            megu.do("おはようございます"),
            tada.do("そういう口の動きだったのだろうが、声は聞こえず、そのまま沢山のスーツに紛れて彼女は列車へと吸い込まれていった"),
            tada.do("発車のベルで多田は我に返ったけれど、ホームを出ていく黒い列車を見送ってしまってから、自分の手の上のラッピングされた紙袋をどうしたものかと、所在なく視線を彷徨わせた"),
            )

def sc_6(w: World):
    tada, megu = w.get('tada'), w.get('megu')
    man, death = w.get('man1'), w.get('death')
    return w.scene("# 霜月１１２２",
            w.tag.title("霜月　１１２２"),
            tada.do("あれから日嵐恵はスカートを履くことがなくなった"),
            tada.do("単に衣替えだとか、服装の好みが変わったのだとか、理由付けをすることはできたけれど、最近の彼女の様子からしてどうにもそう単純な話で片付けられそうには思えなかった。かと言って、多田がそれを聞いてどうにかできる訳でもない"),
            tada.do("自分は無力な人間でしかない"),
            tada.talk("――世間は既に来月のクリスマスムードで盛り上がっているようで……"),
            tada.do("いつの間にかベンチに戻ってきた男が、ポータブルラジオの音量を上げる。つい十分ほど前に、彼に話しかけていたお腹の出た中年男性と階段を降りていったのを見かけたけれど、彼からの取り立てがうまくいったのだろうか。男は一月以上早いクリスマスソングを鼻歌で歌っている"),
            man.talk("あの、ありがとうございました"),
            tada.do("その男に声を掛けたのは、先程彼と一緒に階下に向かった中年男性だ"),
            death.talk("おいおい。気安く声かけないで下さいって、注意したでしょう？"),
            man.talk("あ、はい。すみません。けど"),
            death.talk("あんたはもういいの。また必要になったら、宜しくね"),
            tada.do("中年男性は何度も頭を下げてから、やってきた列車に駆けていった。その足取りが随分と身軽なもので多田は驚いたが、思い返してみれば、その男性はベンチの男と会う前はもっと背中も丸くて肩で息をしている風だった"),
            tada.talk("あの"),
            tada.do("多田は思い切って声をかけた。一瞬｜睨《にら》まれたように感じたが、男の右目が白濁していて、それがぎょろりとこちらを向いたためだろう。左目しか見えないのかも知れない"),
            death.talk("さっきのおっさんか？"),
            tada.talk("あ、いや、その……"),
            tada.do("男は黄ばんだ歯を見せて笑う"),
            death.talk("あんたにはまだまだ関係ない話だ。見たところ、あんたのゼンマイはかなり丈夫そうだしな"),
            tada.do("ゼンマイ。丈夫"),
            tada.do("それらの言葉の意味は分からなかったが、それでも「まだ関係ない」と男は言ったのだ"),
            tada.talk("誰に、関係があるんですか？"),
            tada.do("その質問にふっと歯を見せると、男は舌で乾いた上唇を舐めてから言った"),
            death.talk("疲れ果てた社畜どもだ"),
            tada.do("その声の低さに、多田は思わず息を呑む"),
            death.talk("内緒の話だ"),
            tada.do("男は声を潜めて多田に近づくように指招きをし、続ける"),
            death.talk("オレはな、くたびれたゼンマイを新しいゼンマイに取り替えてやっているんだよ。ゼンマイ、知らないか？　金属の板をくるくるとまるめたあれ。そういえば、あんたらはもっと違う名前で呼んでいるんだったな。確か……心臓"),
            tada.do("男の目がぎっと多田の胸元に向けられて、思わずかばうように左胸を押さえてしまう"),
            death.talk("なぁに、あんたには手が出せない代物だから安心しなよ"),
            tada.do("そう言ってから、男はよれよれの上掛けのポケットに手を突っ込む。男の手に握られていたものは、黒光りする一つの歯車だった"),
            tada.talk("そ、それ"),
            tada.do("彼女の歯車、と口走りそうになり、咄嗟に口を押さえる"),
            death.talk("見たことあるのか？　ああ、そうだな。時々、社畜どもが落としていくからな。もし見つけたなら、そっとオレに回してくれれば悪いようにはしないよ。な、頼んだぜ"),
            tada.do("肩を叩かれて、男は歯を見せる。よく見ればその幾つかは黄ばんでいるのではなく、真鍮色をした歯ではない別の何かだった"),
            )

def sc_7(w: World):
    tada, megu = w.get('tada'), w.get('megu')
    return w.scene("# 師走１２２４",
            w.tag.title("師走　１２２４"),
            tada.do("その年のクリスマスイブは、珍しく朝から雪がちらついていた"),
            megu.talk("多田さん"),
            tada.do("日嵐恵の声だった"),
            tada.do("振り返ると、「メリークリスマス」と笑顔で多田に差し出した彼女の手に、赤と緑のクリスマスカラーで包装された小さな箱があった"),
            tada.do("それが何か、と尋ねるより先に、彼女の髪が耳の辺りまで短くなっていることに気づく。よく見れば分厚くファンデーションが塗られ、まるで仮装用の化粧のように口紅もアイシャドウも濃い。彼女が羽織った淡い桜色のコートの下からは、膝頭が覗いていた。最近は全然履いていなかったスカートだ"),
            tada.talk("あの"),
            megu.talk("クリスマスプレゼントです。大したものじゃ、ありませんけど"),
            tada.do("もらって下さい。と念を押され、多田は手にしていた箒とチリトリをどうしたものかと思っているうちに、ホームに列車が激しい金属音と共に入ってきてしまう"),
            megu.talk("あ、行かなきゃ"),
            tada.do("多田は箒とチリトリを手放して、恵から小箱を受け取ると、"),
            tada.talk("う、うれしいです"),
            tada.do("大きな声で、初めて自分の感情を伝えることができた"),
            megu.talk("わたしも、嬉しかったです。ありがとうございました"),
            tada.do("そう言って恵は小さく手を振り、列車の入り口に小走りで向かって行った"),
            tada.do("多田は列車がすっかりホームから消えてしまうまで、一歩も動けず、ただ白い息を吐き出しているだけだった。けれどそれは決して寒かったからじゃなく、彼の心は高価なコートを着せてもらったくらいに、温まっていた"),
            tada.do("仕事が終わってから開いたその小箱には、箒に乗った少女が半透明の青い球体に閉じ込められた、キーホルダーだろうか、それが一つ入れられていた。球体の下半分に小さく「Thank you」と書かれていたが、その「you」の文字がくしゃりと潰れていて、一緒に入れられていたメモにはこうあった"),
            megu.voice("うまくできなくて、ごめんなさい。　めぐみ"),
            )

def sc_8(w: World):
    tada, megu = w.get('tada'), w.get('megu')
    return w.scene("# 師走１２２５",
            w.tag.title("師走　１２２５"),
            tada.do("翌朝、今度こそ彼女にネジと歯車を返そうと、多田は待ち構えていた"),
            tada.talk("あの、えっと……"),
            tada.do("けれど、その日階段を上がってきてホームに姿を見せた日嵐恵は、七部丈のストライプのシャツと寝間着だろうか、足首のあたりまでひらひらとした素材のワンピースを着ていた。それが彼女の髪からずっと、濡れている。まるで土砂降りの中を走ってきたかのようだ"),
            tada.do("風邪でも引いたら大変だと、多田は首に巻いていたタオルを外すが、その結び目を解く前に日嵐恵は膝から崩れて倒れてしまった。一瞬多田を見やり、寂しげに微笑したような気がしたが、それよりも彼女の体が横倒しになってしまったことに動転してしまい、やっと解いたタオルを握ったまま、"),
            tada.talk("大変だ"),
            tada.do("そう口走った"),
            tada.do("早く、彼女を助けないと"),
            tada.do("多田は右足を引きずって近寄ろうとするが、その脇を駅員たちが軽々と追い抜いていく"),
            tada.do("動かなくなった日嵐恵はすぐに駅員に取り囲まれてしまうが、その隙間から、何か赤いものが床に転がり落ちるのが見えた。ぐるぐると巻いた、金属の塊"),
            tada.talk("ゼンマイ……"),
            tada.do("違う。そう。ベンチの男はあれは「心臓」と多田たちが呼ぶものだと教えてくれた"),
            tada.do("日嵐恵の心臓はガチャガチャと丸まったり伸びたりしながら転がり、彼女を担ぎ上げた駅員の一人の足の蹴飛ばされ、階段の下へと落ちていってしまった"),
            tada.talk("ま、待ってください！"),
            tada.do("多田は右足に思い切り力を入れて駅員の一人の背中にしがみつく。その刹那、ボキリ、と鈍い音がして木製の足が脛から折れた。それでも構わず、"),
            tada.talk("お願いです！　彼女はまだ、大丈夫なんです！"),
            tada.do("多田は駅員たちを必死でその場に留める"),
            tada.talk("あの、ちょっとだけ、待って下さい"),
            tada.do("ベンチを見れば、多田と目線の合った男が首を素早く横に振る"),
            tada.talk("お願いです！　こ、これで……これで何とか！"),
            tada.do("多田は足元に転がってしまった不器用にラッピングされた紙袋を破って中身をひっくり返し、床に真っ赤なネジや歯車、金属の小さなパイブにベアリングといった部品をばらまいた"),
            tada.do("その歯車が一つ、ベンチの方に転がっていく"),
            tada.do("男は足元に転がってきたそれを拾い上げ、裏返したりしてよく見ていたが、"),
            tada.talk("ダメだ"),
            tada.do("と冷たく言い放つ"),
            tada.talk("それなら……これを、僕のゼンマイを、彼女にやってくれ！　頼む！"),
            tada.talk("やめておけ"),
            tada.talk("頼む"),
            tada.talk("無駄だ"),
            tada.talk("僕には、彼女にあげられるものなんて、他にないんだよ！"),
            tada.do("多田は折れた右足を引きずって、ベンチ男にすがりつく"),
            tada.talk("僕は、彼女に、沢山のものを、もらったんだ。だから、それを返さなきゃいけないんだ。でも今の僕には彼女に何もしてあげられない。けど、あんたなら、それができる。そうなんだろう？"),
            tada.do("男は歯を見せながら困った顔で、多田と駅員、それに動かなくなった日嵐恵を何度も見た"),
            tada.talk("こういうのは許可されていないんだが……どうなってもいいんだな？　それだけの覚悟が、お前にはあるんだな？"),
            tada.do("男の白濁した右目と、細めた左目が、多田を見下ろす"),
            tada.do("多田は声を出さずに頷き、それから「頼む」と絞り出した"),
            tada.talk("仕方ない"),
            tada.do("男は右手を何度か握って、開いて、小さく息を吐き出した"),
            tada.talk("やってくれ"),
            tada.do("多田は目を閉じる"),
            tada.do("男の右手が彼の胸元を探り、何かを探し、そこ、と照準を定めると、"),
            tada.talk("残念だよ"),
            tada.do("一気に突っ込んだ。何かをもぎ取り、引き抜く"),
            tada.do("男の手には真っ赤に光る、ゼンマイが握られていた"),
            tada.do("多田はすぐに何も見えなくなり、そのまま体を動かすこともできずに、倒れてしまう"),
            tada.do("それでも、これでいい"),
            tada.do("きっと、これで彼女は助かる"),
            tada.do("起き上がったら、彼女はどんな顔をするだろう"),
            tada.do("また、元気に笑ってくれるだろうか"),
            tada.do("もし「おはよう」と言ってくれたなら、今度こそちゃんと「おはようございます」と返そう"),
            tada.do("そんな思いが、一瞬で駆け巡る"),
            tada.talk("……なんで、よ"),
            tada.do("目が見えなくなった多田の耳に、低い、女の声が入ってくる"),
            tada.talk("なんで蘇らせたりしたのよ！　わたしはもう無理なの！　せっかく、これで全部なくなって楽になれるところだったのに！　なんで！　なんでよ！　もう嫌なの！　働くなんてごめんなの！　なんにもない無になって、誰からも怒鳴られず、叱られず、笑われずに、ただ気持ちを消して、眠りたい……眠り、たいの"),
            tada.do("それが恵の言葉だと理解するまで、多田には意識が残っていただろうか"),
            tada.talk("お願い。これ、抜いて。もう、いらない"),
            tada.do("その言葉が、日嵐恵が残した最期のものになった"),
            w.symbol("　　　　※"),
            tada.do("ベンチに座り、男は貨物列車の荷台に投げ込まれた二つの社畜の成れの果てを、見やる。手元にはその一人が持っていた、小さな赤い歯車がある"),
            tada.do("ポータブルラジオからは一日遅れのクリスマスソングが流れていたが、すぐに暗黒鉄道の発車のベルにかき消されてしまう"),
            tada.do("暗黒鉄道の行き先は『地獄』、そして向こう側の貨物列車の行き先には『天国』と書かれていることを男は知っていたが、どちらにも乗ったことがなかった"),
            tada.do("ホームの屋根の隙間から見上げた空は薄曇りだったが、きっとあの闇の先よりは明るい世界だろう"),
            tada.do("男の手にしていたスマートフォンの画面が明るくなる。『株式会社しにがみ』と表示されていた"),
            tada.talk("相変わらず人使いが荒いことだ"),
            tada.do("誰にともなくぼやき、席を立つ"),
            tada.do("発車のベルが鳴り響き、駅員の冷たいアナウンスが流れた"),
            tada.talk("暗黒鉄道、過労死行き、発車します"),
            )

