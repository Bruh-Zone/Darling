label SGFD_AAA01:
#call macrosys2,SET_SCR_VALUE
#call macrosys2,Init_SGFD
    $persistent.gd["AchievementData"][0]["Check"]=1
    $date="8/5"
    $day="THU"
#setFlag SF_Phone_Disable
#resetFlag SF_PhoneSD_Disp
#/SetSavePoint
#/#AutoSave 1 yujin 20130812 削除
#mwait 1
#setFlag SF_MOVIE_Prologue01
    if video:
        $renpy.movie_cutscene("video/prologue01"+movief)
#PlayMovie prologue01
#PlayMovieWait
#messWindowCloseWait
#call macrosys2,Init_SGFD
    scene expression Solid("000000") with fade
#call macrosys,InitGraph
#call macrosys,InitSound
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    $loadBG(1,"IBGX072")
#setFlag SF_BG1DISP
#call macrosys,FadeInVery2Slow
#resetFlag SF_SYSTEMMENUDISABLE
    $stopvoc("OKA")
    play OKA "FOKA_0021"
    "伦太郎""「时间在流转，随着那行将逝去之物的死而一同消失。有限。」"
    $stopvoc("OKA")
    play OKA "FOKA_0022"
    "伦太郎""「另一方面，时间并不是从过去流向未来的，而是以一种超自然的状态悠然地存在于那里。无限。」"
    $stopvoc("OKA")
    play OKA "FOKA_0023"
    "伦太郎""「拥有睿智而不知者才是真正的智者，乃是在恒久的过去之中从智者口中所出的话语。」"
    $stopvoc("OKA")
    play OKA "FOKA_0024"
    "伦太郎""「知道智慧者因智慧而溺亡，不知智慧者则不懂畅游之术。」"
    $stopvoc("OKA")
    play OKA "FOKA_0025"
    "伦太郎""「知之为知之，不知为不知，是知也。」"
    $stopvoc("OKA")
    play OKA "FOKA_0026"
    "伦太郎""「所以承认自身不知之事，乃接近为神的第一步——」"
#messWindowCloseWait
#call macrosys,FadeOutVery2Slow
#call macrosys,InitGraph
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    $loadBG(1,"BG01N")
#setFlag SF_BG1DISP
#call macrosys,TUNE_CHACOL_BG1
#assign $W(SW_PHONE_PRI),PRI_UPPER_CHARA
#call macrosys2,SET_PHONE_OPEN
    show screen phone(interact=False,transit=False)
#assign $W(SW_PHONE_MODE),PhoneMode_Default
#call macrosys,FadeInVerySlow
#assign $W(SW_PHONE_PRI),PRI_PHONE
#setFlag SF_PhoneSD_Disp
    show screen phoneSD1
    play bgm "BGM06"
    $stopvoc("OKA")
    play OKA "FOKA_0027"
    "伦太郎""「不，在这种场合下与其说不知道……」"
    $stopvoc("CRS")
    play CRS "FCRS_0000"
    "红莉栖？""「那个啊、真由理。请问放在这里的纸杯可以用么？」"
    $stopvoc("MAY")
    play MAY "FMAY_0000"
    "真由理？""「啊、嗯。我觉得可以哦。」"
    $stopvoc("SUZ")
    play SUZ "FSUZ_0000"
    "铃羽？""「给，你要的点心我买了哦。这种感觉的点心就可以了吗？」"
    $stopvoc("RUK")
    play RUK "FRUK_0000"
    "琉华？""「那个，这是母亲大人说要我带来的……」"
    $stopvoc("MAY")
    play MAY "FMAY_0001"
    "真由理？""「哇哦，这个炸的东西。看上去好好吃啊♪」"
    $stopvoc("FEI")
    play FEI "FFEI_0000"
    "菲利丝？""「呐呐，稍微占你点时间可以喵？」"
    $stopvoc("MOE")
    play MOE "FMOE_0000"
    "萌郁？""「……什么？」"
    $stopvoc("FEI")
    play FEI "FFEI_0001"
    "菲利丝？""「我想让你帮我把这个宝特瓶放进冰箱里喵。」"
    $stopvoc("MOE")
    play MOE "FMOE_0001"
    "萌郁？""「啊……知道了……」"
    $stopvoc("OKA")
    play OKA "FOKA_0028"
    "伦太郎""「与其说是不知道，不如应该说是搞不明白来得恰当……」"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA03"),"True","lh/MAY_CMA03a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0002"
    "真由理？""「呐呐，你在那边咕噜咕噜地说什么呀？」"
    "紧贴着我右耳的手机。从听筒那里什么也听不到，连噪音都没有，是完全的沉默。"
    "室内充斥着热气与喧闹声。"
    "啪嗒一声，一滴汗从我额头上落下，弹到了木地板上。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC02"),"True","lh/MAY_CMC02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0003"
    "真由理？""「小冈伦？　我在叫你的说。」"
    "在我面前的是一位少女。"
    "正不解地歪着头跟我打招呼。"
    "明明现在正是深入敌后的关键时刻，可她那张怎么看都稚气未脱的中学生的脸上，却感觉不到一丝紧张。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMB03"),"True","lh/MAY_CMB03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0004"
    "真由理？""「你说搞不明白是指、是指搞不明白什么呢？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KIKAN"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("OKA")
    play OKA "FOKA_0029"
    "伦太郎""「原来如此。果然如我想象的一般，这也是“{color=#f00}机关{/color}”的阴谋啊！」"
    $stopvoc("OKA")
    play OKA "FOKA_0030"
    "伦太郎""「没办法，如果这也是命运石之门(steins gate)的选择的话。EL PSY CONGROO」"
    window hide
    #hide screen phone
    hide screen phonemenu
    show screen phoneblank
    show screen phonebtn
    "我放下拿着手机的手，再次向室内扫视，试图努力理解现在的状况。"
    "但是，果然只有疑问反而在不断地增加。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA04"),"True","lh/MAY_CMA04a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0005"
    "真由理？""「难道小冈伦你、把真由喜给忘记了？　真由喜我啊……」"
    $stopvoc("OKA")
    play OKA "FOKA_0031"
    "伦太郎""「别慌。你是椎名真由理。」"
    $stopvoc("OKA")
    play OKA "FOKA_0032"
    "伦太郎""「同时是这个未来道具ｌａｂ的创立者、也就是我这个狂气的疯狂科学家凤凰院凶真的人质啊，我还好好地记着呢。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0006"
    "真由理""「你能记得住真是太好了呢♪」"
#add $W(SW_CHA1PRI),PRI2_BG
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5
    with dissolve
    #with ImageDissolve(im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576),.5)
    "没错、这个看起来像初中生的女高中生名曰椎名真由理。"
    "乃是这个ｌａｂ的ｌａｂｍｅｍ之一、也就是ｌａｂｍｅｍNO.００２，同时也是我的青梅竹马。"
    "当然我也没打算把这给忘记掉。"
    "而且我刚才所说的，并不是——忘掉了。"
    "而是——搞不明白。"
    hide bg2
    with dissolve
#sub $W(SW_CHA1PRI),PRI2_BG
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh6 zorder (10-6) at right_t:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_CHAPRI),ChaOrder_2134
#call macrosys,CharaDisp62
    $stopvoc("DAR")
    play DAR "FDAR_0000"
    "至？""「怎么了，真由氏。发生什么事了么？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0007"
    "真由理""「那个啊，总感觉小冈伦怪怪的，所以问问他到底怎么了。」"
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA03"),"True","lh/DAR_AMA03a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("DAR")
    play DAR "FDAR_0001"
    "至？""「小冈伦感觉怪怪的？」"
    $stopvoc("CRS")
    play CRS "FCRS_0001"
    "红莉栖？""「你在说什么啊、真由理。冈部奇怪又不是一天两天了吧。」"
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("DAR")
    play DAR "FDAR_0002"
    "至？""「没错没错、就像牧濑氏所说的。如果冈伦不奇怪的话他也不叫冈伦了喔。」"
#add $W(SW_CHA2PRI),PRI2_BG
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5
    with dissolve
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh6
    with dissolve
    "从刚刚一看上去就感觉超闷热的家伙、说话总戳别人痛处的这位叫桥田至。"
    "通称桶子。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAKAR"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HAKAR"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HAKAR"])
#call macrosys,SetTIPScolorSingle
    "乃是稀世的{color=#f00}超级厨客（超级黑客）{/color}，也是我凤凰院凶真可靠的右手。"
    hide bg2 with dissolve
#sub $W(SW_CHA2PRI),PRI2_BG
    "然后是——。"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA03"),"True","lh/CRS_AMA03a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_CHAPRI),ChaOrder_1234
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0002"
    "红莉栖？""「话说回来冈部，这个是你提出来的吧，不要在那里像个呆瓜一样站着，快来帮忙啊！」"
    $stopvoc("OKA")
    play OKA "FOKA_0033"
    "伦太郎""「不对！　克莉斯蒂娜啊！　你到底要我说多少次才能明白！」"
    $stopvoc("OKA")
    play OKA "FOKA_0034"
    "伦太郎""「知道么？　吾乃可以令狂哭的小孩子都马上闭嘴的疯狂科学家凤凰院凶真，不是冈部伦太郎！我都说多少次了！」"
    $stopvoc("CRS")
    play CRS "FCRS_0003"
    "红莉栖２""「你才是啊，说了多少次别叫我克莉斯蒂娜！」"
    $stopvoc("OKA")
    play OKA "FOKA_0035"
    "伦太郎""「什么？　那么该怎么样叫你才好啊？」"
    $stopvoc("OKA")
    play OKA "FOKA_0036"
    "伦太郎""「复苏者(The Zombie)？　土（豪）十七？　还是说果然叫你助手会比较好？」"
    $stopvoc("CRS")
    play CRS "FCRS_0004"
    "红莉栖３""「所以说、叫我的名字啊！」"
    $stopvoc("OKA")
    play OKA "FOKA_0037"
    "伦太郎""「所以说你的名字不是就叫克莉斯蒂娜嘛。」"
    $stopvoc("CRS")
    play CRS "FCRS_0005"
    "红莉栖""「所以说！　我说了多少次我有一个好好的名字叫牧濑红莉栖啊！」"
    $stopvoc("OKA")
    play OKA "FOKA_0038"
    "伦太郎""「你还是那么会算这鸡毛蒜皮的小事呢、克莉斯蒂娜哟。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0006"
    "红莉栖""「唧……！」"
    "被她盯住了。"
    "还是那么容易为这点事情就生气的女人。"
    "但是，捉弄她太过分的话以后不知道会怎么报复我，到这个程度就算了吧。"
    "毕竟没有什么东西能有女人的执念这么可怕啊。"
    $stopvoc("OKA")
    play OKA "FOKA_0039"
    "伦太郎""「所以呢？」"
    $stopvoc("CRS")
    play CRS "FCRS_0007"
    "红莉栖""「什么？」"
    $stopvoc("OKA")
    play OKA "FOKA_0040"
    "伦太郎""「不是“什么”吧？」"
    $stopvoc("OKA")
    play OKA "FOKA_0041"
    "伦太郎""「17岁就从美国大学跳级毕业、在世界性的学术杂志『Science』上面发表研究论文的天才脑科学家、牧濑红莉栖女士你到底要我帮什么忙啊？」"
#resetFl_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh6 zorder (10-6) behind lh5 at right_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OTSU"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0003"
    "至""「说明台词{color=#f00}乙{/color}」"
    hide lh6 with dissolve
    $stopvoc("CRS")
    play CRS "FCRS_0008"
    "红莉栖""「为什么你总要用令我生气的语调来说话呢？」"
    $stopvoc("OKA")
    play OKA "FOKA_0042"
    "伦太郎""「我只是在阐述事实而已。」"
#add $W(SW_CHA1PRI),PRI2_BG
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5
    with dissolve
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5
    with dissolve
    "没错，刚才我说的全部都是事实。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NEURO"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NEURO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_NEURO"])
#call macrosys,SetTIPScolorSingle
    "在我面前的这个女人，是年纪轻轻就被世界所承认的{color=#f00}脑科学{/color}天才。"
    "在这个夏天，到日本逆留学的期间，因为她无论如何也要做我的弟子，无奈之下只能让她成为我的助手，以ｌａｂｍｅｍNO.００４之名被认可。"
    "不得不说的是她这个蛮横的态度。"
    "在海外的话这种性格也许可以蒙混过关，但也差不多该让她明白在日本这样是行不通的了。"
    "不过我凤凰院凶真，并不是为这么点事儿就吹毛求疵的心胸狭窄的男人，所以才闷声不吭的。"
    "先说好了，我并不是因为这个女人很黑很可怕才默不作声的。"
    hide bg2 with dissolve
#sub $W(SW_CHA1PRI),PRI2_BG
    $stopvoc("OKA")
    play OKA "FOKA_0043"
    "伦太郎""「那么我就再问一次，你们究竟是在闹腾什么？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0009"
    "红莉栖""「你说在干嘛是指？」"
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N2")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#call macrosys,TUNE_CHACOL_BG1
    "我扫视了一遍房间内的景象。"
#resetFlag SF_CHA5DISP
    hide screen phoneSD1
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA03"),"True","lh/FEI_DSA03a~ipad.png") as lh5 zorder (10-5) at right_q2:
        yalign .55
    with Dissolve(1)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA01"),"True","lh/RUK_CSA01a~ipad.png") as lh6 zorder (10-6) at left_q1:
        yalign .55
    with Dissolve(1)
#resetFlag SF_CHA7DISP
#call macrosys,InitCHA7
    hide lh7
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh7 zorder (10-7) at right_q1:
        yalign .55
    with Dissolve(1)
#resetFlag SF_CHA8DISP
#call macrosys,InitCHA8
    hide lh8
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") as lh8 zorder (10-8) at left_q2:
        yalign .55
    with Dissolve(1)
#call macrosys,CharaDispQ51627384
    $stopvoc("FEI")
    play FEI "FFEI_0002"
    "菲利丝２""「啊咧？　这里有木有微波炉喵？」"
    $stopvoc("RUK")
    play RUK "FRUK_0001"
    "琉华３""「啊，我记得现在是放在里面房间的。」"
#resetFlag SF_CHA7DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh7 zorder (10-7):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp73
    $stopvoc("MAY")
    play MAY "FMAY_0008"
    "真由理""「微波炉已经被小冈伦弄到不能使用了。」"
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB04"),"True","lh/RUK_CSB04a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("RUK")
    play RUK "FRUK_0002"
    "琉华３""「啊，原来是这样啊。」"
    $stopvoc("MOE")
    play MOE "FMOE_0002"
    "萌郁３""「那个……这个放在哪？」"
    "在这个绝不算大的房间里面，堆满了各种各样的东西，像是在宣告“这里就是研究室”一样。"
    "在这样的环境中，从刚才开始就有几个人在啪嗒啪嗒地来回走动。"
    "这个状况到底意味着什么呢。"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
    show screen phoneSD1
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG01N")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB03"),"True","lh/CRS_AMB03a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    $stopvoc("CRS")
    play CRS "FCRS_0010"
    "红莉栖""「所以说，这是你提出来的吧！」"
    $stopvoc("OKA")
    play OKA "FOKA_0044"
    "伦太郎""「所以说，我以前到底说了些什么？」"
    $stopvoc("CRS")
    play CRS "FCRS_0011"
    "红莉栖""「所！以！说！　为了庆祝新的未来道具完成从而策划举行这场宴会的家伙就是你吧！！」"
    $stopvoc("OKA")
    play OKA "FOKA_0045"
    "伦太郎""「所以说我说啊！　所以说……哎？　你说新的未来道具！？　你刚才是这样说了么？」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB03"),"True","lh/CRS_AMB03a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh6 zorder (10-6) at right_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("DAR")
    play DAR "FDAR_0004"
    "至""「是这样的喔。继电话微波炉（暂）以来的未来道具新品，从９号机到１１号机。」"
    $stopvoc("OKA")
    play OKA "FOKA_0046"
    "伦太郎""「什么、这也就是说……居然多了３台！？」"
    $stopvoc("DAR")
    play DAR "FDAR_0005"
    "至""「你在说什么呀，说做多点的不是冈伦你么。」"
    $stopvoc("OKA")
    play OKA "FOKA_0047"
    "伦太郎""「唔……原来如此、是这样一回事啊。」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5
    with dissolve
    "综合红莉栖和桶子说的话，我终于明白现在的状况了。"
    "也就是说他们完成了我下令制作的未来道具新品，现在就是为那个的完成而做庆祝的准备中——就是这么一回事吧。"
    "但是很遗憾的是，我并没有这样的记忆。"
    "看来在我不知道的时候，这样的命令被下达出去了。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_KIKAN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_KIKAN"])
#call macrosys,SetTIPScolorSingle
    "难道说这也是“{color=#f00}机关{/color}”做的好事吗。"
    "不、不对。"
    "那么。"
    hide bg2
    with dissolve
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh6 zorder (10-6) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("OKA")
    play OKA "FOKA_0048"
    "伦太郎""「桶子啊，我可以再问一个问题么？」"
    $stopvoc("DAR")
    play DAR "FDAR_0006"
    "至""「但是我拒绝。」"
    $stopvoc("OKA")
    play OKA "FOKA_0049"
    "伦太郎""「唔姆」"
    "被拒绝了啊。"
    "但是，像桶子这种网络用语的滥发只不过是像条件反射一样的东西，并不代表他本人的意志。"
    "不用介意继续询问吧。"
    $stopvoc("OKA")
    play OKA "FOKA_0050"
    "伦太郎""「现在是要举办宴会，这我是明白了。」"
    $stopvoc("OKA")
    play OKA "FOKA_0051"
    "伦太郎""「但是、啊，这明明是ｌａｂ的宴会为什么那些家伙会在？」"
    "我指着那些为这为那忙上忙下的家伙。"
    "如果是ｌａｂ的宴会的话，应该是仅限ｌａｂｍｅｍ们来参加。"
    "但是现在在这研究室里面的算上我足足有８个人。"
    "可根据我的记忆，ｌａｂｍｅｍ现在应该最多只到NO.００６。"
    "至少５分钟之前还是这样的。"
    "也就是说从刚才开始就开始忙这忙那的家伙中间，明显有着不是ｌａｂｍｅｍ的人混了进来这一事实。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JK"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JK"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JK"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0007"
    "至""「你要问为什么也……当然因为他们是ｌａｂｍｅｍ啊，{color=#f00}常考{/color}。」"
    $stopvoc("OKA")
    play OKA "FOKA_0052"
    "伦太郎""「你竟然说他们是……ｌａｂｍｅｍ？　难道在这里的全部都是？」"
    $stopvoc("DAR")
    play DAR "FDAR_0008"
    "至""「是这样喔，所以怎么了？」"
    $stopvoc("OKA")
    play OKA "FOKA_0053"
    "伦太郎""「没什么」"
    "原来如此啊。"
    "新未来道具的完成。"
    "伴随着完成的庆宴。"
    "不知道在何时增加的ｌａｂｍｅｍ。"
    "全部都是我所不知道的事情。"
    "这样的话也就是说。"
#assign $W(SW_BGMFADE),FADE_VERY2SLOW
    stop bgm
    $stopvoc("OKA")
    play OKA "FOKA_0054"
    "伦太郎""「哼哈、哼哼哼哼、嗯哼哼哼哼哼哼哼哼哈！！！」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB03"),"True","lh/DAR_AMB03a~ipad.png") as lh6 zorder (10-6) at right_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("DAR")
    play DAR "FDAR_0009"
    "至""「那个啊、牧濑氏。就像真由氏所说的，果然今天的冈伦真的是有点奇怪喔。」"
    $stopvoc("CRS")
    play CRS "FCRS_0012"
    "红莉栖""「啊、嗯，的确是这样呢。」"
    "根据我现在所掌握的情况，已经没有必要再去怀疑了。"
    "说到底，这些事实所说明的真相只有一个！"
    $stopvoc("OKA")
    play OKA "FOKA_0055"
    "伦太郎""「喝哈哈哈哈！　看来实验成功了！」"
    $stopvoc("DAR")
    play DAR "FDAR_0010"
    "至""「实验？」"
    $stopvoc("CRS")
    play CRS "FCRS_0013"
    "红莉栖""「你说实验……喂、难道是」"
    $stopvoc("OKA")
    play OKA "FOKA_0056"
    "伦太郎""「嗯，第六感真强呢，克莉斯蒂娜哟。」"
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N2")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#call macrosys,TUNE_CHACOL_BG1
    "我环视室内一周，为了让大家都听得见，我故意大声说道。"
    $stopvoc("OKA")
    play OKA "FOKA_0057"
    "伦太郎""「就是这样！　就在刚刚，我已经进行了D-MAIL实验！！」"
    $stopvoc("OKA")
    play OKA "FOKA_0058"
    "伦太郎""「然后到了现在，我终于确信我的想法是没有错的了！」"
    $stopvoc("OKA")
    play OKA "FOKA_0059"
    "伦太郎""「我、凤凰院凶真在这里宣言！」"
#setFlag SF_Phone_AutoDisable
    $stopvoc("OKA")
    play OKA "FOKA_0060"
    "伦太郎""「果然D-MAIL拥有改变过去的力量！！」"
    stop OKA
    hide screen phoneSD1
    hide screen phonebtn
    hide screen phonebtn2
    hide screen phone
    hide screen phonemenu
    window hide
    $renpy.hide_screen("phonebtn")
#resetFlag SF_PhoneSD_Disp
#messWindowCloseWait
#call macrosys,FadeOutWhite32OW
#PlayMovie op
    if video:
        $renpy.movie_cutscene("video/op"+movief)
#PlayMovieWait
#setFlag SF_MOVIE_OP
#call macrosys,InitGraph
#call macrosys,FadeInVery2Slow
    scene expression Solid("ffffff") with dissolve
    scene expression Solid("000000") with dissolve
#mwait FADE_VERYSLOW
#call macrosys,FadeOut0
#call macrosys,InitGraph
#call macrosys,InitSound
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    window hide
    $loadBG(1,"TIT001")
    pause 2
#setFlag SF_BG1DISP
#call macrosys,FadeInVery2Slow
#assign $W(LR_TMP00),300
#call macrosys,KeyWait_TIM
#call macrosys,FadeOutVery2Slow
#call macrosys,InitGraph
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    $loadBG(1,"BG03A4")
#setFlag SF_BG1DISP
#call macrosys,TUNE_CHACOL_BG1
    play bgm "BGM19"
#call macrosys,FadeInVery2Slow
    show screen phonebtn
#setFlag SF_PhoneSD_Disp
    window show
    show screen phoneSD1
    show screen phonebtn
    "归根结底，其根源乃是未来道具８号机——通称『电话微波炉（暂）』的研发。"
    "这个未来道具ｌａｂ对外宣称的，正如其名，乃是以『未来道具』的研发为目的，而由我狂气的疯狂科学家、凤凰院凶真所设立的ｌａｂ。"
    "要说为什么是『对外』的话，此乃由于『未来道具的研究开发』只不过是为了达成我真正目的的一个手段而已。"
    "吾等的真正目的，乃是制作这个世界的支配构造并将其替换，从而把混沌引入现世。"
    "为此才进行的未来道具的开发。"
    "但是在这个过程中，我们意外地开发出了不得了的东西。"
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG03A4D1")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
    "看来我也不用介绍了，那就是『电话微波炉（暂）』。"
    "原本这个『电话微波炉（暂）』，是把微波炉接上电话使得其可以拥有远程操作功能——最初的时候的确只是这样设计的。"
    "但是，直到几天前才搞清楚，原来它是有着意想不到的特殊用途的。"
    hide screen phonebtn
    hide screen phonebtn2
    show screen phoneblank
    pause 1
    show screen phoneblank
    pause 1
    show screen phone(interact=False)
    pause 1
    show screen phonemenu
    pause 1
    show screen phonemenu_mail
    pause 1
    show screen phone_inbox

#call macrosys2,PhoneWait_60
#assign $W(SW_PHONE_MODE),PhoneMode_DefaultOperatable
#call macrosys2,PhoneWait_60
#assign $W(SW_PHONE_MENUCUR),PhoneMode_DefaultOperatable_Mail
#call macrosys2,PhoneWait_30
    "所谓的特殊用途就是隐藏了『可以往过去发送邮件』这个令人吃惊的功能。"
    show screen phone_readmail(gc["MailData"][353],interact=False)
#assign $W(SW_PHONE_MAILMENUCUR),0
#assign $W(SW_PHONE_MODE),PhoneMode_MailMenu
#call macrosys2,PhoneWait_30
#call macrosys2,Disp_ReceiveBox
#call macrosys2,PhoneWait_60
    $targetmailid = gc["ScriptMacros"]["FMZ_From_OKA0302"]
#call macrosys2,SELECT_RECEIVED_MAIL
    "只不过是个邮件而已，你一定在这么想吧！"
    "能向过去发送邮件的话也就是说，能对于过去所发生的事情产生『说不定能产生影响』这种效果。"
    "比如，向过去的自己发送必中的六合彩号码，并叫自己一定要去买。"
    show screen phone_inbox
    pause 1
    show screen phone_readmail(gc["MailData"][352],interact=False)
#call macrosys2,DISP_RECEIVED_MAIL
#call macrosys2,PhoneWait_60
#call macrosys2,Return_ReceiveBox
#call macrosys2,PhoneWait_30
    $targetmailid = gc["ScriptMacros"]["FMZ_From_OKA0303"]
#call macrosys2,SELECT_RECEIVED_MAIL_NEXT
#call macrosys2,PhoneWait_30
#call macrosys2,DISP_RECEIVED_MAIL
    "如果过去的自己真的看到了这一封邮件而去买这个六合彩的话——。"
    show screen phone_inbox
    pause 1
    show screen phone_readmail(gc["MailData"][354],interact=False)
#call macrosys2,Return_ReceiveBox
#call macrosys2,PhoneWait_30
    $targetmailid = gc["ScriptMacros"]["FMZ_From_OKA0301"]
#call macrosys2,SELECT_RECEIVED_MAIL_NEXT
#call macrosys2,PhoneWait_30
#call macrosys2,DISP_RECEIVED_MAIL
#call macrosys2,PhoneWait_60
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DENWA_RANGE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DENWA_RANGE"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_D_MAIL"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_D_MAIL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_D_MAIL"])
    "将会如何呢。"
    "那是一个不能单单以邮件这个单薄的名词来解释的现象，而是一个很重大的发现，这你能理解了吧。"
    "什么，那种事情只不过是痴人说梦话而已？"
    "所以我才说凡人啊……虽然我很想这么说，不过算了，你会怀疑也不是毫无道理的。"
    "就连我最开始也是这样想的。"
    hide screen phonemenu
    show screen phoneblank
    show screen phonebtn
    "但是啊！"
    "所发生的事就是一切，这就是事实。"
    "比事实更加可信的东西是不存在的。"
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG03A4")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#call macrosys,TUNE_CHACOL_BG1
    "为此，我们在这里重复实验了好几天。"
    "然后今天终于找到了答案——"
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N1")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#call macrosys,TUNE_CHACOL_BG1
    $stopvoc("OKA")
    play OKA "FOKA_0061"
    "伦太郎""「果然D-MAIL拥有改变过去的力量！！」"
    "在此之前不断地重复实验。"
    "但是之前就算做了如此之多的实验也没有得出个确实的答案来。"
    "不过，这回可不一样了！"
    "要问为什么的话，我现在置身其中的这个状态乃是因为我往过去发送了邮件——也就是D-MAIL，从而使得过去的世界被替换了！"
    $stopvoc("OKA")
    play OKA "FOKA_0062"
    "伦太郎""「哼哼哼哼哼哼！」"
    $stopvoc("OKA")
    play OKA "FOKA_0063"
    "伦太郎""「哼嗯哈哈哈哈哈哈！！！　我们成功地制作出世纪大发明了！」"
    $stopvoc("OKA")
    play OKA "FOKA_0064"
    "伦太郎""「怎么样！　定是由于过于惊惧而说不出话了吧！」"
    "这是可以颠覆人类历史的发明。"
    "因为我嘹亮的宣言，导致在场所有的人都被我的气势压倒，因而什么都说不出来了吧。"
#assign $W(SW_BGMFADE),FADE_VERY2SLOW
    stop bgm
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB01"),"True","lh/RUK_CSB01a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("RUK")
    play RUK "FRUK_0003"
    "琉华３""「那个……还有其他不够的……」"
    "连话也说——。"
    hide lh5 with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSB01"),"True","lh/FEI_DSB01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0003"
    "菲利丝２""「有筷子么喵？」"
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB01"),"True","lh/MOE_ASB01a~ipad.png") as lh6 zorder (10-6) at left_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("MOE")
    play MOE "FMOE_0003"
    "萌郁３""「在这里……」"
    hide lh5
    hide lh6
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5) at right0:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0009"
    "真由理""「呐，甜点就用香蕉好么？」"
    $stopvoc("OKA")
    play OKA "FOKA_0065"
    "伦太郎""「可恶……」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    play bgm "BGM05"
    "真是太可恶了，这群愚蠢的人！"
    "比起这世纪的大发明，居然觉得眼前的饵食更加重要，真是多么令人叹气啊。"
    $stopvoc("CRS")
    play CRS "FCRS_0014"
    "红莉栖""「喂！」"
    $stopvoc("OKA")
    play OKA "FOKA_0066"
    "伦太郎""「呃？」"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG01N")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB03"),"True","lh/CRS_AMB03a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    "呼姆。"
    "就如我所想的，果然只有这家伙能好好理解我说的话。"
    "不管怎么说，这家伙可是参加了１星期之前广播会馆那场有关时间机器的讲座。"
    "不可能没有兴趣。"
    $stopvoc("CRS")
    play CRS "FCRS_0015"
    "红莉栖""「你刚才说的事情都属实？」"
    $stopvoc("OKA")
    play OKA "FOKA_0067"
    "伦太郎""「我所说的事情、是指？」"
    $stopvoc("CRS")
    play CRS "FCRS_0016"
    "红莉栖""「就是说、实验啊。你说的过去改变了那件事。」"
    $stopvoc("OKA")
    play OKA "FOKA_0068"
    "伦太郎""「当然。」"
    $stopvoc("CRS")
    play CRS "FCRS_0017"
    "红莉栖""「证据呢？」"
    $stopvoc("OKA")
    play OKA "FOKA_0069"
    "伦太郎""「我的经历就是证据。」"
    $stopvoc("CRS")
    play CRS "FCRS_0018"
    "红莉栖""「你说经历，那是什么经历？」"
    $stopvoc("OKA")
    play OKA "FOKA_0070"
    "伦太郎""「哼哼，你想我告诉你么？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB06"),"True","lh/CRS_AMB06a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0019"
    "红莉栖""「这个，嘛……」"
#/#mes2v FOKA_0071,$W(LR_LIP_OKA),VID_OKA,＠倫太郎＠「だったら、そこに三つ指をついてお願いします鳳凰院凶真様と言え。そうすれば教えてやらないことも」&a0;
    $stopvoc("OKA")
    play OKA "FOKA_0071"
    "伦太郎""「如果你真的想听的话，那就跪地请求，说求你了嘛凤凰院凶真大人，如果这样做的话我就告诉你吧。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC03"),"True","lh/CRS_AMC03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0020"
    "红莉栖""「呐，真由理，这些碗应该可以摆上来了吧？」"
    $stopvoc("OKA")
    play OKA "FOKA_0072"
    "伦太郎""「请听我说吧，求求你了。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB02"),"True","lh/CRS_AMB02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0021"
    "红莉栖""「你一开始这样说不就好了。」"
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") as lh6 zorder (10-6) behind lh5 at right_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("DAR")
    play DAR "FDAR_0011"
    "至""「冈伦弱爆了！」"
    "可恶！　这是何等的屈辱。"
    "但是这里得忍耐。"
    "现在得先让他们知道我是如何地伟大。"
#setFlag SF_Phone_AutoDisable
    "这样的话，自然助手也会对我心存畏惧吧。"
    $renpy.hide_screen("phonebtn")
#assign $W(SW_BGMFADE),FADE_VERY2SLOW
    stop bgm
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"IBGX072")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
    "助手和桶子询问了我关于我这几天的来龙去脉。"
    "作为交换，他们也把我所处的这个状况给我作出了说明。"
    "根据这一情况，我对于这个朦胧不清的状况稍稍有点明白了。"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG01N")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB01"),"True","lh/CRS_AMB01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    play bgm "BGM26"
    show screen phonebtn
    $stopvoc("CRS")
    play CRS "FCRS_0022"
    "红莉栖""「原来如此，看来你所改变以前的过去，和改变之后的过去——也就是我们所处的这个现在的过去，共通点有很多呢。」"
    $stopvoc("OKA")
    play OKA "FOKA_0073"
    "伦太郎""「嗯，与此相对，现实好像也有非常多的变化。」"
    "虽然已经知道了D-MAIL所附带的这个技能，但我们还是为了确认其是否属实，而进行了实验——通称“掌管过去的女神”作战。"
    "综合我们所说的话，到这里为止还没有特别大的差别。"
    "改变的部分是，在那之后我要求中断实验并且命令去制作新的未来道具。"
    "还有，此前还是6个人的ｌａｂｍｅｍ迅速增加至8人。"
    "主要就是这两点了。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC01"),"True","lh/CRS_AMC01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0023"
    "红莉栖""「但是果然不管怎么想都是很不可思议呢」"
    $stopvoc("OKA")
    play OKA "FOKA_0074"
    "伦太郎""「不可思议？　什么不可思议？」"
    $stopvoc("CRS")
    play CRS "FCRS_0024"
    "红莉栖""「这当然是，你的那个能力啊。」"
    $stopvoc("CRS")
    play CRS "FCRS_0025"
    "红莉栖""「那个叫什么来着？　好像是……」"
    $stopvoc("OKA")
    play OKA "FOKA_0075"
    "伦太郎""「没想到所谓的天才少女原来记忆力如此之差啊，克莉斯蒂娜哟。」"
    $stopvoc("OKA")
    play OKA "FOKA_0076"
    "伦太郎""「那我就再告诉你一次吧，掏干净你的耳洞好好地听着！」"
    $stopvoc("OKA")
    play OKA "FOKA_0077"
    "伦太郎""「这是特意为我准备的，目的是用来见证世界改变的力量！　其名曰魔眼“命运探知”！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0026"
    "红莉栖""「……果然，你那命名品味，就不能改一下么？」"
    $stopvoc("OKA")
    play OKA "FOKA_0078"
    "伦太郎""「这可不行。」"
    $stopvoc("CRS")
    play CRS "FCRS_0027"
    "红莉栖""「为什么不行？」"
    $stopvoc("OKA")
    play OKA "FOKA_0079"
    "伦太郎""「因为这是命运石之门的选择。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC05"),"True","lh/CRS_AMC05a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0028"
    "红莉栖""「莫名其妙。」"
    $stopvoc("OKA")
    play OKA "FOKA_0080"
    "伦太郎""「哼，所以你才一直只是我的助手啊。」"
    "用D-MAIL改变过去，也就是说被改变的时间点之后所发生的事情都会受到影响。"
    "到现在为止红莉栖他们的言行同样也可以看出，对于改变之前所发生的事情，他们的记忆已经消失了。"
    "要说为什么，这是因为这些事情“并没有发生”。"
    "如果是没有发生的事情，也就连被记忆的机会都没有了。"
    "这是当然的。"
    "然后，当然我自己能在被这个“被改变的过去”的延长线上的“现在”这里出现，看来只有我拥有“被改变的过去”之前的记忆。"
    "这就是，神所赐予我的特殊力量“命运探知”。"
    "只是以此为代价，我并不知道改变之后所发生的事情。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA01"),"True","lh/CRS_AMA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0029"
    "红莉栖""「算了，这样也好，所以你发送了什么回去？」"
    $stopvoc("OKA")
    play OKA "FOKA_0081"
    "伦太郎""「你说、发送了什么？」"
    $stopvoc("CRS")
    play CRS "FCRS_0030"
    "红莉栖""「所以说啊，你往过去发送了D-MAIL对吧？　我在问几天前你到底发送了什么回去啊。」"
    $stopvoc("OKA")
    play OKA "FOKA_0082"
    "伦太郎""「不知道。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA07"),"True","lh/CRS_AMA07a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0031"
    "红莉栖""「啥？」"
    "红莉栖忽然狂暴起来，提高了音调。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB04"),"True","lh/CRS_AMB04a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0032"
    "红莉栖""「等等！　你说不知道到底是怎么回事？」"
    $stopvoc("OKA")
    play OKA "FOKA_0083"
    "伦太郎""「哼哈哈哈哈哈！　就让我教教你这助手吧，克莉斯蒂娜！」"
    $stopvoc("OKA")
    play OKA "FOKA_0084"
    "伦太郎""「为了验证这一假说是否成立，我们必须进行多次试验！　而且那些实验都九杆子打不到一起！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB06"),"True","lh/CRS_AMB06a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0033"
    "红莉栖""「也就是说，你得意洋洋地发送了好多封邮件结果连自己也变得不明不白了吗？」"
    $stopvoc("OKA")
    play OKA "FOKA_0085"
    "伦太郎""「不、不是的！　实际上，在这实验的途中我的右手暴走了……咕、呃啊啊啊、又来——啊！！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMA07"),"True","lh/CRS_AMA07a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CHUNI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CHUNI"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("CRS")
    play CRS "FCRS_0034"
    "红莉栖""「啰嗦！　既然自称疯狂科学家的话，起码实验给我好好地做啊，你这个{color=#f00}厨二病{/color}！」"
    $stopvoc("OKA")
    play OKA "FOKA_0086"
    "伦太郎""「可恶……」"
    "明明就是个助手居然如此目中无人。"
    "但是在这里生气的话就太过于小家子气了。"
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N1")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#call macrosys,TUNE_CHACOL_BG1
    hide screen phonebtn
    hide screen phonebtn2
    show screen phoneblank
    pause 1
    show screen phoneblank
    pause 1
    show screen phone(interact=False)
    "我取出手机贴在耳旁。"
    $stopvoc("OKA")
    play OKA "FOKA_0087"
    "伦太郎""「……不必担心，没问题，这也是给予我的考验。」"
    $stopvoc("OKA")
    play OKA "FOKA_0088"
    "伦太郎""「……不怕，就这种事而已，也不是什么大事。」"
    $stopvoc("OKA")
    play OKA "FOKA_0089"
    "伦太郎""「……啊啊，这一切都是命运石之门的选择啊，EL PSY CONGROO」"
    hide screen phonemenu
    show screen phoneblank
    show screen phonebtn
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    "我刚收起电话，却发现不知道从什么时候开始真由理就站在我旁边了。"
    $stopvoc("MAY")
    play MAY "FMAY_0010"
    "真由理""「嘟嘟噜。呐呐、小冈伦小冈伦」"
    $stopvoc("OKA")
    play OKA "FOKA_0090"
    "伦太郎""「所以我说真由理啊，强调了多少次要叫我凤凰院凶真。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0011"
    "真由理""「但是小冈伦就是小冈伦喔。」"
    "……哎、算了。"
    "对这家伙已经这么说了５年，但直到现在她都不肯听。"
    "虽然我并不喜欢小冈伦这种称呼方式，可也只好平静地接受了。"
    $stopvoc("OKA")
    play OKA "FOKA_0091"
    "伦太郎""「有什么事吗，真由理？」"
    $stopvoc("MAY")
    play MAY "FMAY_0012"
    "真由理""「诶？」"
    $stopvoc("OKA")
    play OKA "FOKA_0092"
    "伦太郎""「诶什么诶啊？你是因为找我有事才叫我的吧。」"
    $stopvoc("MAY")
    play MAY "FMAY_0013"
    "真由理""「啊，说起来是这样呢。」"
    $stopvoc("MAY")
    play MAY "FMAY_0014"
    "真由理""「那个啊、那个……啊、对了对了！　快准备好了。」"
    $stopvoc("OKA")
    play OKA "FOKA_0093"
    "伦太郎""「准备？」"
    $stopvoc("MAY")
    play MAY "FMAY_0015"
    "真由理""「就是庆祝的准备，已经准备好了。」"
    $stopvoc("OKA")
    play OKA "FOKA_0094"
    "伦太郎""「啊啊……」"
#assign $W(SW_BGMFADE),FADE_VERY3SLOW
    stop bgm
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    "这么一说，直到刚才还一直在准备的ｌａｂｍｅｍ们全体都看向了我。"
    "说起来也是，现在在这里聚集了这么多的人也是为了这个吧。"
    "虽然是我不曾记得的事情，但事到如今就顺着它去吧。"
    "我特意拿着白大褂甩了一圈，飒爽地穿上之后，庄严地宣布。"
#setFlag SF_Phone_AutoDisable
    $stopvoc("OKA")
    play OKA "FOKA_0095"
    "伦太郎""「好！　我宣布第８９回圆桌会议现在开始！！」"
    $renpy.hide_screen("phonebtn")
#messWindowCloseWait
    scene expression Solid("000000") with fade
#call macrosys,InitGraph
#mwait 60
    $persistent.gd["EVData"][gc["ScriptMacros"]["EV_Z01A"]]["Check"]=True
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    $loadBG(1,"EV_Z01A")
#setFlag SF_BG1DISP
#call macrosys,FadeInVerySlow
    play bgm "BGM18"
    show screen phonebtn
    "然后几分钟以后。"
    "这个世界已经充满混沌了。"
#setFlag SF_Phone_AutoDisable
    "仅限于在这个ｌａｂ里面。"
    
    $renpy.hide_screen("phonebtn")
    show expression Solid("111") as bg2b:
        alpha 0.3
    show expression LiveCrop((1000,0,720,400),"bg/EV_Z01A@2x~ipad.jpg") as bg2:
        yalign 0
        xcenter.5
#assign $W(LR_FADE_TIM),FADE_NORMAL
#call macrosys2,EV_Z01A_CUTIN_1ST_STA
    $stopvoc("SUZ")
    play SUZ "FSUZ_0001"
    "扎着麻花辫的女人""「呐、牧濑红莉栖难道就是那个天才少女牧濑红莉栖？」"
    $stopvoc("CRS")
    play CRS "FCRS_0035"
    "红莉栖""「天、天才少女真不敢当。」"
    $stopvoc("SUZ")
    play SUZ "FSUZ_0002"
    "扎着麻花辫的女人""「为什么，像你这样的人也会成为这个ｌａｂ的成员？」"
    $stopvoc("CRS")
    play CRS "FCRS_0036"
    "红莉栖""「这个嘛，我也不是很清楚。」"
    show expression LiveCrop((780,330,720,400),"bg/EV_Z01A@2x~ipad.jpg") as bg2:
        yalign 0
        xcenter.5
        pause 0.01
#assign $W(LR_FADE_TIM),FADE_VERYSLOW
#call macrosys2,EV_Z01A_CUTIN_1ST_SCRL_1ST
    $stopvoc("MAY")
    play MAY "FMAY_0016"
    "真由理""「琉华君妈妈做的炸鸡块，真是很好吃呢。」"
    $stopvoc("RUK")
    play RUK "FRUK_0004"
    "琉华""「你能这么说，我想母亲大人也会很高兴的。」"
    show expression LiveCrop((1200,330,720,400),"bg/EV_Z01A@2x~ipad.jpg") as bg2:
        yalign 0
        xcenter.5
#assign $W(LR_FADE_TIM),FADE_VERYSLOW
#call macrosys2,EV_Z01A_CUTIN_1ST_SCRL_2ND
    $stopvoc("MAY")
    play MAY "FMAY_0017"
    "真由理""「呐呐，萌郁酱也吃一块尝尝吧。」"
    $stopvoc("MOE")
    play MOE "FMOE_0004"
    "萌郁""「啊……」"
    $stopvoc("MAY")
    play MAY "FMAY_0018"
    "真由理""「呐，真的很好吃吧。」"
    $stopvoc("MOE")
    play MOE "FMOE_0005"
    "萌郁""「嗯、嗯……」"
    hide bg2b
    hide bg2
    with dissolve
#call macrosys2,EV_Z01A_CUTIN_1ST_END
    show screen phonebtn
#setFlag SF_Phone_AutoDisable
    $stopvoc("OKA")
    play OKA "FOKA_0096"
    "伦太郎""「…………」"
    $renpy.hide_screen("phonebtn")
    show expression Solid("111") as bg2b:
        alpha 0.3
    show expression LiveCrop((0,0,720,400),"bg/EV_Z01A@2x~ipad.jpg") as bg2:
        yalign 0
        xcenter.5
#assign $W(LR_FADE_TIM),FADE_NORMAL
#call macrosys2,EV_Z01A_CUTIN_2ND_STA
    $stopvoc("DAR")
    play DAR "FDAR_0012"
    "至""「那个，可以拜托菲利丝炭你一点事情么。」"
    show expression LiveCrop((0,610,720,400),"bg/EV_Z01A@2x~ipad.jpg") as bg2:
        yalign 0
        xcenter.5
#assign $W(LR_FADE_TIM),FADE_VERYSLOW
#call macrosys2,EV_Z01A_CUTIN_2ND_SCRL_1ST
    $stopvoc("FEI")
    play FEI "FFEI_0004"
    "菲利丝""「喵喵？」"
#assign $W(LR_FADE_TIM),FADE_VERYSLOW
#call macrosys2,EV_Z01A_CUTIN_2ND_SCRL_2ND
    show expression LiveCrop((0,0,720,400),"bg/EV_Z01A@2x~ipad.jpg") as bg2:
        yalign 0
        xcenter.5
    $stopvoc("DAR")
    play DAR "FDAR_0013"
    "至""「我希望菲利丝炭能对我使用传说中的秘技“望着你的眼我混我混”。」"
#assign $W(LR_FADE_TIM),FADE_VERYSLOW
#call macrosys2,EV_Z01A_CUTIN_2ND_SCRL_1ST
    show expression LiveCrop((0,610,720,400),"bg/EV_Z01A@2x~ipad.jpg") as bg2:
        yalign 0
        xcenter.5
    $stopvoc("FEI")
    play FEI "FFEI_0005"
    "菲利丝""「今天的菲利丝啊，可不是ＭａｙＱｕｅｅｎ的女仆哦喵。」"
#assign $W(LR_FADE_TIM),FADE_VERYSLOW
#call macrosys2,EV_Z01A_CUTIN_2ND_SCRL_2ND
    show expression LiveCrop((0,0,720,400),"bg/EV_Z01A@2x~ipad.jpg") as bg2:
        yalign 0
        xcenter.5
    $stopvoc("DAR")
    play DAR "FDAR_0014"
    "至""「这里求通融。」"
#assign $W(LR_FADE_TIM),FADE_VERYSLOW
#call macrosys2,EV_Z01A_CUTIN_2ND_SCRL_1ST
    show expression LiveCrop((0,610,720,400),"bg/EV_Z01A@2x~ipad.jpg") as bg2:
        yalign 0
        xcenter.5
    $stopvoc("FEI")
    play FEI "FFEI_0006"
    "菲利丝""「不行喵。」"
    hide bg2b
    hide bg2
    show screen phonebtn
#call macrosys2,EV_Z01A_CUTIN_2ND_END
    show screen phonebtn
    $stopvoc("OKA")
    play OKA "FOKA_0097"
    "伦太郎""「你们到底在搞什么飞机啊！　到底是什么呀，这充满混沌的圆桌会议！」"
    "明明圆桌会议是决定ｌａｂ之方向的重要会议！"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(1,"BG02N2")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA01"),"True","lh/MAY_CMA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    $stopvoc("MAY")
    play MAY "FMAY_0019"
    "真由理""「不对的哦，小冈伦。」"
    $stopvoc("OKA")
    play OKA "FOKA_0098"
    "伦太郎""「到底有什么不对的？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0020"
    "真由理""「这个呢，并不是圆托会议，是宴会的哦。」"
    "不是圆托是圆桌会议啊。"
    "但是即使修正了她说的话，大概对真由理来说也是对牛谈琴，这里就无视吧。"
    $stopvoc("MAY")
    play MAY "FMAY_0021"
    "真由理""「所以说呀，今天我们不说难懂的事情哦。」"
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh6 zorder (10-6) at left_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("DAR")
    play DAR "FDAR_0015"
    "至""「没错没错，说到底提出举行庆祝的还是冈伦吧。」"
    $stopvoc("OKA")
    play OKA "FOKA_0099"
    "伦太郎""「呼姆」"
    "说到底为什么我会提出举行庆祝呢。"
    "虽然是我自己说的，但我却一头雾水。"
#setFlag SF_Phone_AutoDisable
    $stopvoc("OKA")
    play OKA "FOKA_0100"
    "伦太郎""「但是如果你们太吵的话，说不定会惹得Ｍｒ.Ｂｒｏｗｎ怒吼哦。」"
    $renpy.hide_screen("phonebtn")
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(1,"BG05N3")
#assign $W(SW_BG2PRI),PRI2_BG
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BG2_FadeInTIM
#call macrosys,TUNE_CHACOL_BG2
#call macrosys,CharaClearAll
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    "这里不得不说明一下的是。"
    "这个未来道具ｌａｂ位于秋叶原外围的一幢２层的古老杂居大楼里，而我们则栖身在大楼的２层。"
#messWindowCloseWait
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    $loadBG(1,"BG04A2")
#setFlag SF_BG1DISP
#call macrosys,TUNE_CHACOL_BG1
#assign $W(SW_BG2PRI),PRI2_BG
#assign $W(LR_TMP01),BG_VERYSLOW
#beginAnimation
#assign $W(SW_BG2SIZE),2000
#assign $W(SW_BG2POSX),(SCR_SIZ_X/2)
#assign $W(SW_BG2POSY),(SCR_SIZ_Y/2)
#assign $W(SW_BG2DISPMODE),BGDISPMODE_ZOOM
#assign $W(SW_BG2ALPHA),0;
#commitAnimation
#assign $W(LR_THD_BG2_FADETIM),FADE_SLOW
#call macrosys,THD_BG2_FadeOut
#flagOnWait LF_THD_BG2_MOVEEXEC
#flagOnWait LF_THD_BG2_FADEEXEC
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    "所谓的Ｍｒ.Ｂｒｏｗｎ，是位于一层的『显像管工房』的老板，话说显像管那玩意到底现在还有没有市场需求还真难说。不过这家店是一间只负责处理显像管电视相关事宜的极为特殊的店，镇守的店长是个看上去很可怕的大叔。"
    "当然，不管Ｍｒ.Ｂｒｏｗｎ看上去是多么地残暴，只要有我的隐藏之力在手，那大叔根本就是小菜一碟。"
    "虽说如此，但惹他愤怒的话对我们也没好处。"
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG05N3")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
    "要说其原因，那就是因为Ｍｒ.Ｂｒｏｗｎ他乃是这个杂居大楼——『大桧山大楼』的所有者。"
    "我们之所以能在这个大楼里面以几乎免费的价格占据着这整个一层，当然是与我这个领袖人物超凡的魅力有很大的关系。"
    "也就是说他、Ｍｒ.Ｂｒｏｗｎ相当有看人的眼光，不过同时性格有些喜怒无常。"
    "我想说的就是，如果闹腾得太厉害把他惹怒了，要求提高房租的话我可受不了。"
    "至今已经不知道因为同样的理由被他威胁过多少次了。"
    "吵吵闹闹的可不是上策。"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N2")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    show screen phonebtn
    $stopvoc("SUZ")
    play SUZ "FSUZ_0003"
    "扎着麻花辫的女人""「店长的话，现在这个时间不在店里所以不用担心哦。」"
    $stopvoc("OKA")
    play OKA "FOKA_0101"
    "伦太郎""「什么？　这是真的么？」"
    $stopvoc("SUZ")
    play SUZ "FSUZ_0004"
    "扎着麻花辫的女人""「嗯，他说把店交给我之后，就出去了。」"
    "这个扎着麻花辫的女人一边抓着零食一边说道。"
    "这个扎着麻花辫的女人——这个名为阿万音铃羽的女人，乃是显像管工房最近雇用的打工战士。"
    "既然打工的都这样说了，大概就可以放心了吧。"
    $stopvoc("OKA")
    play OKA "FOKA_0102"
    "伦太郎""「所以呢打工战士，你现在在干什么啊？」"
    $stopvoc("SUZ")
    play SUZ "FSUZ_0005"
    "铃羽""「什么干什么，我在跟你们一起庆祝啊？　我也是那个……那个、怎么说那单词来着，ｌｕｂｅｒｍｅｎ？」"
    $stopvoc("OKA")
    play OKA "FOKA_0103"
    "伦太郎""「你是想说ｌａｂｍｅｍ吧？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA02"),"True","lh/SUZ_AMA02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("SUZ")
    play SUZ "FSUZ_0006"
    "铃羽""「没错没错，就是那个什么ｌａｂｍｅｍ啦。」"
    $stopvoc("OKA")
    play OKA "FOKA_0104"
    "伦太郎""「这样说的话，你好像也是ｌａｂｍｅｍ了啊。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMB03"),"True","lh/SUZ_AMB03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("SUZ")
    play SUZ "FSUZ_0007"
    "铃羽""「什么“这样说的话”，真是失礼啊，不是冈部伦太郎你叫我加入的吗？」"
    $stopvoc("SUZ")
    play SUZ "FSUZ_0008"
    "铃羽""「从今天开始，你就是ｌａｂｍｅｍNO.００８了。这样说的」"
    $stopvoc("OKA")
    play OKA "FOKA_0105"
    "伦太郎""「啊、啊啊……是这样吗。」"
    "原来如此。这家伙是ｌａｂｍｅｍNO.００８啊。"
    "算了，虽然我不知道到底发生了什么事情才会把这家伙纳入ｌａｂｍｅｍ的，不过这也是命运石之门的选择啊。"
    "值得一提的是，我并不很清楚这家伙的情况，不过慢慢去了解吧。"
    "为了完成给世界带来混沌之目标，有时也需要不拘小节。"
    $stopvoc("OKA")
    play OKA "FOKA_0106"
    "伦太郎""「所以呢，回答我的问题，你到底在这里干嘛？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA01"),"True","lh/SUZ_AMA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("SUZ")
    play SUZ "FSUZ_0009"
    "铃羽""「不是说了吗，作为ｌａｂｍｅｍ在参加这庆祝活动啊。」"
    $stopvoc("OKA")
    play OKA "FOKA_0107"
    "伦太郎""「我并不是说这个，店长不是拜托你看店吗？」"
    $stopvoc("SUZ")
    play SUZ "FSUZ_0010"
    "铃羽""「嗯，是被拜托了啊。」"
    $stopvoc("OKA")
    play OKA "FOKA_0108"
    "伦太郎""「这个被拜托了的人，现在在这里摸鱼不是很不妙么？」"
    $stopvoc("SUZ")
    play SUZ "FSUZ_0011"
    "铃羽""「不会啦，因为今天店已经打烊了。」"
    $stopvoc("OKA")
    play OKA "FOKA_0109"
    "伦太郎""「什么？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_AMA02"),"True","lh/SUZ_AMA02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
#setFlag SF_Phone_AutoDisable
    $stopvoc("SUZ")
    play SUZ "FSUZ_0012"
    "铃羽""「因为啊，店长都说了把店拜托给我，所以说就算关店也是我的自由啊？」"
    $renpy.hide_screen("phonebtn")
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG05N3")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#mwait FADE_VERYSLOW
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG05N4")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_FAST
#call macrosys,BgOverWrite
#mwait FADE_VERYSLOW
    "这家伙……！"
    "这回答太出乎意料简直让我吓一跳！"
    "这就是被宽松教育所毒害的家伙么！"
    "……Ｍｒ.Ｂｒｏｗｎ，看来你真的没什么看人的眼光啊。"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N2")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA02"),"True","lh/MAY_CMA02a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    show screen phonebtn
    $stopvoc("MAY")
    play MAY "FMAY_0022"
    "真由理""「呐？　总之就是这个原因，今天大家一起快乐地开ｐａｒｔｙ吧。」"
    $stopvoc("MAY")
    play MAY "FMAY_0023"
    "真由理""「可以的吧，小冈伦？」"
    $stopvoc("OKA")
    play OKA "FOKA_0110"
    "伦太郎""「好吧，你要这样做的话我也没办法了。」"
    "虽然并不是我本意，但是给部下一点休息的时间也是有必要的。"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG01N")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMC01"),"True","lh/FEI_DMC01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    $stopvoc("FEI")
    play FEI "FFEI_0007"
    "菲利丝""「那么，就先把那些难懂的话题放在一边，再一次干杯喵！」"
    $stopvoc("FEI")
    play FEI "FFEI_0008"
    "菲利丝""「大家，拿起杯子喵！」"
    $stopvoc("OKA")
    play OKA "FOKA_0111"
    "伦太郎""「等、等等！　这种事情应该由我来」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMA02"),"True","lh/FEI_DMA02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0009"
    "菲利丝""「干杯！！！」"
    $stopvoc("")
#call macrosys,Set_VOspeaker_REAR
#   SetSavePoint
#setFlag SF_MESSAVEPOINT_SSP
#assign $W(LR_LIP_MIX),($W(LR_LIP_DAR)|$W(LR_LIP_MAY)|$W(LR_LIP_CRS)|$W(LR_LIP_MOE)|$W(LR_LIP_RUK)|$W(LR_LIP_SUZ))
    $stopvoc("GOS")
    play GOS "FGOS_0000"
    "labmem全体""「干杯！！」"
    "可恶，明明ｌａｂ的创立者是我的说……！"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMA01"),"True","lh/FEI_DMA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("")
#call macrosys,Set_VOspeaker_Default
    $stopvoc("FEI")
    play FEI "FFEI_0011"
    "菲利丝""「嗯？　凶真、怎么了喵？」"
    $stopvoc("OKA")
    play OKA "FOKA_0112"
    "伦太郎""「没、没什么，什么也没有。」"
    "今天我就姑且网开一面放过他们吧。"
    "这种程度就愤怒，我凤凰院凶真并不是这么心胸狭窄的人。"
    "而且我对这个叫做菲利丝的女人也毫无办法……。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMA03"),"True","lh/FEI_DMA03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0012"
    "菲利丝""「嗯，果然你看上去很奇怪喵。」"
    $stopvoc("OKA")
    play OKA "FOKA_0113"
    "伦太郎""「没有这回事，我一直都是很正常的。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMC02"),"True","lh/FEI_DMC02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0013"
    "菲利丝""「哈哈！　难道凶真你，还在为那时候的事情……」"
    $stopvoc("OKA")
    play OKA "FOKA_0114"
    "伦太郎""「什么？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMC03"),"True","lh/FEI_DMC03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0014"
    "菲利丝""「不用遮掩的喵。果然，那场“神圣大血战”(Grand Crusade)时受的伤还在……！」"
    "受伤……？"
    $stopvoc("OKA")
    play OKA "FOKA_0115"
    "伦太郎""「你、你说什么，那种程度的伤对我来说……」"
    $stopvoc("FEI")
    play FEI "FFEI_0015"
    "菲利丝""「你骗人喵！　你可蒙不过我菲利丝的双眼！　别说了让我看看喵。」"
    $stopvoc("OKA")
    play OKA "FOKA_0116"
    "伦太郎""「不要！！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMC04"),"True","lh/FEI_DMC04a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0016"
    "菲利丝""「凶真……」"
    $stopvoc("OKA")
    play OKA "FOKA_0117"
    "伦太郎""「不要……不要来碰我。」"
    $stopvoc("FEI")
    play FEI "FFEI_0017"
    "菲利丝""「果然，凶真在那时候为了救菲利丝，使用了那个“被封印的秘术”……」"
    "被封印的秘术是啥啊！"
    "退一万步来说，那“神圣大血战”什么的更加是听都没听说过！"
#add $W(SW_CHA1PRI),PRI2_BG
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5
    with dissolve
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAID"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAID"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MAID"])
#call macrosys,SetTIPScolorSingle
    "这个叫做菲利丝的女人，是真由理在秋叶原打工的那家十分有人气的{color=#f00}女仆咖啡馆{/color}『ＭａｙＱｕｅｅｎ＋喵喵⑯』的人气头牌女仆。"
    "桶子他们也是她的狂热粉丝，但是我觉得跟这个妄想力爆棚的家伙交流非常困难。"
    "这家伙一直都是这样，先插嘴把我的话抢走，然后自顾自地加上各种“设定”，然后再接二连三说个不停，她拥有这种能力。"
    "能力名『ｄｉｖｉｎｇ１０』。"
    "这是何等恐怖的力量。"
    "而且，要是跟这家伙继续对话下去，恐怕连我平时的言行举止也会被认为是妄想。"
    "先说好了，我那些话可都不是妄想，而是真实的。"
    "跟她那些东西混为一谈可不行。"
    "在继续深入下去之前，先改变话题才是上策。"
    hide bg2
    with dissolve
#sub $W(SW_CHA1PRI),PRI2_BG
    $stopvoc("OKA")
    play OKA "FOKA_0118"
    "伦太郎""「说起来菲利丝啊，你也是ｌａｂｍｅｍ来的么？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMB01"),"True","lh/FEI_DMB01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0018"
    "菲利丝""「是喵！　侍奉于漆黑的黑暗“七钥之守护神”与“古老盟约”的达成，煞费了我一番苦心，终于如愿以偿作为ｌａｂｍｅｍNO.００７得到了承认喵。」"
    "赶紧无视，无视。"
    $stopvoc("OKA")
    play OKA "FOKA_0119"
    "伦太郎""「但是，你为什么要加入ｌａｂｍｅｍ？　让我听听理由吧。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMC03"),"True","lh/FEI_DMC03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0019"
    "菲利丝""「这是因为喵」"
    $stopvoc("OKA")
    play OKA "FOKA_0120"
    "伦太郎""「这是因为？」"
#/#mes2v FFEI_0020,$W(LR_LIP_FEI),VID_FEI,＠フェイリス＠「このラボに入ることで、フェイリスから妹を奪ったあの憎き“黄金の黄昏団(ゴールデン・ダスク)”に一矢報いるために……」&a0;
    $stopvoc("FEI")
    play FEI "FFEI_0020"
    "菲利丝""「加入这里是因为我想向那个把菲利丝的妹妹抢走的“金色黄昏小队”(golden dusk)报一箭之仇……」"
    $stopvoc("OKA")
    play OKA "FOKA_0121"
    "伦太郎""「原来如此，我知道了。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMA03"),"True","lh/FEI_DMA03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0021"
    "菲利丝""「啊、凶真！　我还没有说完喵！」"
    "现在我可没有时间再和菲利丝胡搅蛮缠了。"
    "我转身背向了菲利丝。"
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N2")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
    "然后，跟面前的人对上眼了。"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMA01"),"True","lh/RUK_CMA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("RUK")
    play RUK "FRUK_0006"
    "琉华""「啊，冈部师父。」"
    $stopvoc("OKA")
    play OKA "FOKA_0122"
    "伦太郎""「嗯，是琉华子啊。」"
    "漆原琉华。"
    "跟真由理同年级，同时也是我的弟子，还是ｌａｂｍｅｍNO.００６……应该是这样的。"
    "虽然看上去是个清纯美丽的大和抚子——但是，"
#call macrosys2,CAP1_OTOKO_STA
    "是男的。"
#call macrosys2,CAP1_OTOKO_END
    "连准备宴会的时候，也比谁都要来得勤快。"
#call macrosys2,CAP1_OTOKO_STA
    "但是，是男的。"
    "嗯？　不、等等……"
    $stopvoc("OKA")
    play OKA "FOKA_0123"
    "伦太郎""「呼姆」"
    "我仔细地端详着琉华子的脸。"
#call macrosys2,CAP1_OTOKO_END
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMA03"),"True","lh/RUK_CMA03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("RUK")
    play RUK "FRUK_0007"
    "琉华""「哎？　那、那个，冈部师父？」"
    $stopvoc("OKA")
    play OKA "FOKA_0124"
    "伦太郎""「我不叫冈部。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMB04"),"True","lh/RUK_CMB04a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("RUK")
    play RUK "FRUK_0008"
    "琉华""「真对不起，凶真师父。」"
#setFlag SF_Phone_AutoDisable
    $stopvoc("OKA")
    play OKA "FOKA_0125"
    "伦太郎""「我看看啊，看上去是没什么变化嘛……」"
    $renpy.hide_screen("phonebtn")
#resetFlag SF_PhoneSD_Disp
#messWindowCloseWait
#call macrosys2,FadeOutKaisouSTA
#call macrosys,InitGraph
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    hide lh5
    with Fade(0.5, 0.5, 0.5, color="#fff")
#setFlag SF_BG1DISP
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_DLA02"),"True","lh/RUK_DLA02a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaSet51
#call macrosys,SET_DOF3_SHORT
#call macrosys2,FadeInKaisouSTA
    
    "我发D-MAIL改变过去，是在几个小时之前的事。"
    "想成为女孩子——琉华子向我们坦白了自己这个冲击性的梦想。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_POCKET_BELL"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_POCKET_BELL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_POCKET_BELL"])
#call macrosys,SetTIPScolorSingle
    "对这个怎么想都不可能实现的梦寄托了最后一丝的希望，琉华子向母亲的{color=#f00}ＢＰ机{/color}发送了某些信息。"
    hide lh5 with Fade(0.5, 0.5, 0.5, color="#fff")
label L_SGFD_AAA01_PHONE_MAIL_01_RECEIVE:
    $targetmailid = gc["ScriptMacros"]["FM_AAA01_RECV_MOE01"]
    if phonemailring!= "":
        play se phonemailring
    $RcvMail(targetmailid)
#messWindowCloseWait
#call macrosys2,FadeOutKaisouEND
#call macrosys,SET_DOF3_LONG
#call macrosys,InitGraph
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    $loadBG(1,"BG02N2")
#setFlag SF_BG1DISP
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMA03"),"True","lh/RUK_CMA03a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaSet51
#call macrosys2,FadeInKaisouEND
    show screen phonebtn
#setFlag SF_PhoneSD_Disp
    $stopvoc("RUK")
    play RUK "FRUK_0009"
    "琉华""「那个……怎、怎么了？　我的脸上有什么脏东西么？」"
    $stopvoc("OKA")
    play OKA "FOKA_0126"
    "伦太郎""「琉华子，我可以问你件事儿么？」"
    $stopvoc("RUK")
    play RUK "FRUK_0010"
    "琉华""「好、好的，请问是什么呢？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_POCKET_BELL"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_POCKET_BELL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_POCKET_BELL"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("OKA")
    play OKA "FOKA_0127"
    "伦太郎""「你向你母亲的{color=#f00}ＢＰ机{/color}发送的信息是……」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMA01"),"True","lh/RUK_CMA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_POCKET_BELL"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_POCKET_BELL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_POCKET_BELL"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("RUK")
    play RUK "FRUK_0011"
    "琉华""「向母亲的{color=#f00}ＢＰ机{/color}发送信息、么？　应该没有……」"
    $stopvoc("OKA")
    play OKA "FOKA_0128"
    "伦太郎""「没有发送信息？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_POCKET_BELL"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_POCKET_BELL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_POCKET_BELL"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("RUK")
    play RUK "FRUK_0012"
    "琉华""「是的，以前倒是不知道，不过我的母亲现在应该是没有{color=#f00}ＢＰ机{/color}的……」"
    $stopvoc("OKA")
    play OKA "FOKA_0129"
    "伦太郎""「这样啊。」"
    "原来如此。"
    "我还担心如果有万一的话该怎么办呢，看来是杞人忧天了。"
    "看样子琉华子的身体应该没有发生变化。"
label L_SGFD_AAA01_PHONE_MAIL_02_RECEIVE:
    $targetmailid = gc["ScriptMacros"]["FM_AAA01_RECV_MOE02"]
    if phonemailring!= "":
        play se phonemailring
    $RcvMail(targetmailid)
    "既有点安心也有点遗憾的感觉……"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMA02"),"True","lh/RUK_CMA02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("RUK")
    play RUK "FRUK_0013"
    "琉华""「真、真对不起凶真师父。」"
    $stopvoc("OKA")
    play OKA "FOKA_0130"
    "伦太郎""「为什么琉华子你要道歉？」"
    $stopvoc("RUK")
    play RUK "FRUK_0014"
    "琉华""「因为，凶真师父，看起来一副失望的表情。」"
    "这家伙对别人细微的心情变化还是那么敏感啊。"
#call macrosys2,CAP1_OTOKO_STA
    "但是是男的。"
#call macrosys2,CAP1_OTOKO_END
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMA02"),"True","lh/RUK_CMA02a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC03"),"True","lh/MAY_CMC03a~ipad.png") as lh6 zorder (10-6) at right:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("MAY")
    play MAY "FMAY_0025"
    "真由理""「真是的，这样是不行的哦，小冈伦。不可以欺负琉华君。」"
label L_SGFD_AAA01_PHONE_MAIL_03_RECEIVE:
    $targetmailid = gc["ScriptMacros"]["FM_AAA01_RECV_MOE03"]
    if phonemailring!= "":
        play se phonemailring
    $RcvMail(targetmailid)
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMA06"),"True","lh/RUK_CMA06a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("RUK")
    play RUK "FRUK_0015"
    "琉华""「真由理酱，我、我并没有被欺负……」"
    $stopvoc("OKA")
    play OKA "FOKA_0131"
    "伦太郎""「就是这样、真由理。而且琉华子乃是我的弟子，稍稍做点过分的事情还是可以的。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMB04"),"True","lh/RUK_CMB04a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("RUK")
    play RUK "FRUK_0016"
    "琉华""「稍、稍稍过分的事情是……」"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG01N")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC04"),"True","lh/CRS_AMC04a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA04"),"True","lh/DAR_AMA04a~ipad.png") as lh6 zorder (10-6) at right:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5|BUF_CHA6)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_NORMAL
#call macrosys,Disp_NextScreen
    $stopvoc("DAR")
    play DAR "FDAR_0017"
    "至""「我惊！　难道冈伦你对那方面的事情有兴趣？　这样的话我以后得小心了。」"
    $stopvoc("CRS")
    play CRS "FCRS_0038"
    "红莉栖""「冈部、你这家伙……」"
    $stopvoc("OKA")
    play OKA "FOKA_0132"
    "伦太郎""「白痴！　我并不是这个意思！」"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N2")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMB03"),"True","lh/RUK_CMB03a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC02"),"True","lh/MAY_CMC02a~ipad.png") as lh6 zorder (10-6) at right:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5|BUF_CHA6)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_NORMAL
#call macrosys,Disp_NextScreen
    $stopvoc("RUK")
    play RUK "FRUK_0017"
    "琉华""「什么啊，稍稍有点遗憾……」"
    $stopvoc("OKA")
    play OKA "FOKA_0133"
    "伦太郎""「啥？」"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG01N")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMC06"),"True","lh/CRS_AMC06a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB04"),"True","lh/DAR_AMB04a~ipad.png") as lh6 zorder (10-6) at right:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5|BUF_CHA6)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_NORMAL
#call macrosys,Disp_NextScreen
    $stopvoc("DAR")
    play DAR "FDAR_0018"
    "至""「呃？」"
    $stopvoc("CRS")
    play CRS "FCRS_0039"
    "红莉栖""「哈？」"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N2")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CMA03"),"True","lh/RUK_CMA03a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMC02"),"True","lh/MAY_CMC02a~ipad.png") as lh6 zorder (10-6) at right:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5|BUF_CHA6)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_NORMAL
#call macrosys,Disp_NextScreen
    $stopvoc("RUK")
    play RUK "FRUK_0018"
    "琉华""「啊！　讨厌！　我刚刚又说起了奇怪的事情……」"
    $stopvoc("MAY")
    play MAY "FMAY_0026"
    "真由理""「什么什么？　琉华君，你刚刚说了什么？」"
    $stopvoc("RUK")
    play RUK "FRUK_0019"
    "琉华""「什、什么也没有说，什么也……」"
    $stopvoc("MAY")
    play MAY "FMAY_0027"
    "真由理""「真的么？」"
    $stopvoc("RUK")
    play RUK "FRUK_0020"
    "琉华""「是真的啦！」"
    "唔、就当没听见吧……"
    "先不说这个……"
label L_SGFD_AAA01_BRA_01_STA:
    if isread("FM_AAA01_RECV_MOE01"):
        jump L_SGFD_AAA01_BRA_01_A
    if isread("FM_AAA01_RECV_MOE02"):
        jump L_SGFD_AAA01_BRA_01_A
    if isread("FM_AAA01_RECV_MOE03"):
        jump L_SGFD_AAA01_BRA_01_A
    jump L_SGFD_AAA01_BRA_01_B
label L_SGFD_AAA01_BRA_01_A:
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    jump L_SGFD_AAA01_BRA_01_END
label L_SGFD_AAA01_BRA_01_B:
label L_SGFD_AAA01_PHONE_MAIL_04_RECEIVE:
#call macrosys2,SelfStop_SkipMode
    $targetmailid = gc["ScriptMacros"]["FM_AAA01_RECV_MOE04"]
    if phonemailring!= "":
        play se phonemailring
    $RcvMail(targetmailid)
#call macrosys2,PhoneWait_60
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
label L_SGFD_AAA01_PHONE_MAIL_04_TRIGGER_STA:
    $stopvoc("OKA")
    play OKA "FOKA_0134"
    "伦太郎""「好烦！　从刚才开始你在搞什么飞机啊！！」"
#flagOnJump SF_PhoneTrigger,L_SGFD_AAA01_PHONE_MAIL_04_TRIGGER_EXEC
label L_SGFD_AAA01_PHONE_MAIL_04_TRIGGER_END:
    jump L_SGFD_AAA01_PHONE_MAIL_04_TRIGGER_NOTHING
label L_SGFD_AAA01_PHONE_MAIL_04_TRIGGER_EXEC:
#call macrosys2,Finish_SelfStop_SkipMode
#call macrosys2,Finish_MailTrigger
    jump L_SGFD_AAA01_PHONE_MAIL_04_TRIGGER_FINISH
label L_SGFD_AAA01_PHONE_MAIL_04_TRIGGER_NOTHING:
#call macrosys2,Finish_SelfStop_SkipMode
#call macrosys2,Finish_MailTrigger
    hide screen phonebtn
    hide screen phonebtn2
    show screen phoneblank
    pause 1
    show screen phone(interact=False)
    pause 1
    show screen phonemenu
    pause 1
    show screen phonemenu_mail
    pause 1
    show screen phone_inbox
    pause 1
    show screen phone_readmail(rml[0])
    pause
#call macrosys2,PhoneWait_30
#call macrosys2,DISP_RECEIVED_MAIL_DIRECT
#call macrosys2,Wait_Finish_MailView
    jump L_SGFD_AAA01_PHONE_MAIL_04_TRIGGER_FINISH
label L_SGFD_AAA01_PHONE_MAIL_04_TRIGGER_FINISH:
    hide screen phone_readmail
    show screen phoneblank
    show screen phonebtn
    jump L_SGFD_AAA01_BRA_01_END
label L_SGFD_AAA01_BRA_01_END:
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02NS2")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_AMB01"),"True","lh/MOE_AMB01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    $stopvoc("OKA")
    play OKA "FOKA_0135"
    "伦太郎""「喂、指压师我在叫你。」"
    $stopvoc("MOE")
    play MOE "FMOE_0007"
    "萌郁""「啊……」"
    $stopvoc("OKA")
    play OKA "FOKA_0136"
    "伦太郎""「如果你有什么想说的，大声说出来就可以了。」"
    $stopvoc("OKA")
    play OKA "FOKA_0137"
    "伦太郎""「明明就在眼前，不要再用手机发邮件！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_AMB03"),"True","lh/MOE_AMB03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MOE")
    play MOE "FMOE_0008"
    "萌郁""「对不起……我、不擅长面对面说话……」"
#add $W(SW_CHA1PRI),PRI2_BG
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5
    with dissolve
    "闪光的指压师——因为可以连续以恐怖的速度发出邮件攻击，因此我对她的能力如此命名。"
    "名字好像是叫做桐生萌郁。"
    "她是在秋叶原『Ａｒｃ Ｒｅｗｒｉｔｅ』杂志编辑部打工的女人。"
    "跟她是偶然相识，正巧昨天被她知道了D-MAIL的存在，就顺势以ｌａｂｍｅｍNO.００５的身份把她招入了……"
    "不过在这个过去被改变过的“现在”，她到底是因为什么才加入ｌａｂｍｅｍ的，还是个谜团。"
    "关于此，说不定以后就会顺其自然地知道了，但也可能反之。"
    "总之现在应该没有问题。"
    hide bg2
    with dissolve
#sub $W(SW_CHA1PRI),PRI2_BG
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_AMB01"),"True","lh/MOE_AMB01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#UDGE_RM_AAA_FEI01_ENA
#call macrosys,CharaDisp51
    $stopvoc("MOE")
    play MOE "FMOE_0009"
    "萌郁""「然后我想说，冈部君……」"
    $stopvoc("OKA")
    play OKA "FOKA_0138"
    "伦太郎""「所以说，从刚才起我就在强调我不叫冈部而是叫凤凰院凶真！」"
    $stopvoc("OKA")
    play OKA "FOKA_0139"
    "伦太郎""「真是的，你们还真净是些……」"
    $stopvoc("MOE")
    play MOE "FMOE_0010"
    "萌郁""「冈部君，关于刚才你所说的……」"
    $stopvoc("OKA")
    play OKA "FOKA_0140"
    "伦太郎""「唔唔唔……」"
    "这就是那个么？"
    "难道她是在蔑视我？"
    "如果是这样的话，可得狠狠地……"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_AMA01"),"True","lh/MOE_AMA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
#mwait 60
label L_SGFD_AAA01_PHONE_MAIL_05_RECEIVE:
#call macrosys2,SelfStop_SkipMode
    $targetmailid = gc["ScriptMacros"]["FM_AAA01_RECV_MOE05"]
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==True:
        pause
        $renpy.choice_for_skipping()
    $RcvMail(targetmailid)
    #call macrosys2,Finish_MailTrigger
    
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_AMB01"),"True","lh/MOE_AMB01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
label L_SGFD_AAA01_PHONE_MAIL_05_TRIGGER_STA:
    $stopvoc("OKA")
    play OKA "FOKA_0141"
    hide screen phonebtn
    hide screen phonebtn2
    show screen phoneblank
    pause 1
    show screen phone(interact=False)
    "伦太郎""「姆？」"
#flagOnJump SF_PhoneTrigger,L_SGFD_AAA01_PHONE_MAIL_05_TRIGGER_EXEC
label L_SGFD_AAA01_PHONE_MAIL_05_TRIGGER_END:
    jump L_SGFD_AAA01_PHONE_MAIL_05_TRIGGER_NOTHING
label L_SGFD_AAA01_PHONE_MAIL_05_TRIGGER_EXEC:
#call macrosys2,Finish_SelfStop_SkipMode
#call macrosys2,Finish_MailTrigger
    jump L_SGFD_AAA01_PHONE_MAIL_05_TRIGGER_FINISH
label L_SGFD_AAA01_PHONE_MAIL_05_TRIGGER_NOTHING:
#call macrosys2,Finish_SelfStop_SkipMode
    show screen phone_readmail(rml[0])
#call macrosys2,PhoneWait_30
#call macrosys2,DISP_RECEIVED_MAIL_DIRECT
#call macrosys2,Wait_Finish_MailView
    jump L_SGFD_AAA01_PHONE_MAIL_05_TRIGGER_FINISH
label L_SGFD_AAA01_PHONE_MAIL_05_TRIGGER_FINISH:
    "……身体一下子没有力气了。"
    "没用的，对这家伙说什么也是没用的。我有这种感觉。"
    hide screen phonemenu
    show screen phoneblank
    show screen phonebtn
    $stopvoc("OKA")
    play OKA "FOKA_0142"
    "伦太郎""「你真就那么想知道关于新的未来道具的事情？」"
    $stopvoc("MOE")
    play MOE "FMOE_0011"
    "萌郁""「……嗯」"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N2")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMB01"),"True","lh/FEI_DMB01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    $stopvoc("FEI")
    play FEI "FFEI_0022"
    "菲利丝""「什么喵什么喵？　难道终于要开始发表新的未来道具了么喵？」"
    $stopvoc("OKA")
    play OKA "FOKA_0143"
    "伦太郎""「什么啊、菲利丝。你也想知道吗？」"
    $stopvoc("FEI")
    play FEI "FFEI_0023"
    "菲利丝""「因为啊，就是因为这个才特意在最不凑巧的时候抽身过来集合的喵。」"
    $stopvoc("OKA")
    play OKA "FOKA_0144"
    "伦太郎""「不凑巧？」"
    hide lh5 with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMB01"),"True","lh/FEI_DMB01a~ipad.png") as lh5 zorder (10-5) at right:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMA01"),"True","lh/DAR_AMA01a~ipad.png") as lh6 zorder (10-6) at left_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("DAR")
    play DAR "FDAR_0019"
    "至""「怎么了？　难道菲利丝炭你，遇到什么大麻烦了？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMC01"),"True","lh/FEI_DMC01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0024"
    "菲利丝""「啊、没有，什么也没有喵。」"
    $stopvoc("DAR")
    play DAR "FDAR_0020"
    "至""「真的么？　如果不嫌弃的话，只要你开口我随时都可以帮忙哦。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMA01"),"True","lh/FEI_DMA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0025"
    "菲利丝""「谢谢喵！　但是，真的真的没有什么事啦，希望你们不要在意喵。」"
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_AMB03"),"True","lh/DAR_AMB03a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_FLAG"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_FLAG"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_FLAG"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0021"
    "至""「真奇怪呢……如果是工口游戏的话，这时候就会竖起『桶子君好厉害♪』的{color=#f00}Flag{/color}吧？」"
    "桶子你够了，工口游戏脑也要适可而止。"
    "话说你脑补的东西全部都泄露出来了喂。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMC01"),"True","lh/FEI_DMC01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0026"
    "菲利丝""「先不管这个，未来道具的事情呢喵」"
    $stopvoc("RUK")
    play RUK "FRUK_0021"
    "琉华""「那个、我也想知道的说。冈部师……不对是凶真师父所做的未来道具的事情。」"
#assign $W(SW_BGMFADE),FADE_VERY3SLOW
    stop bgm
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    "不知道从什么时候起，ｌａｂ里的所有人都在看着我。"
    $stopvoc("OKA")
    play OKA "FOKA_0145"
    "伦太郎""「哼……哼哼哼……」"
    $stopvoc("OKA")
    play OKA "FOKA_0146"
    "伦太郎""「哼嗯哈哈哈哈哈！　是吗是吗！　看来你们作为ｌａｂｍｅｍ的自觉终于开始觉醒了！」"
    $stopvoc("OKA")
    play OKA "FOKA_0147"
    "伦太郎""「那么就给我听好了！　新的未来道具就是！」"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC01"),"True","lh/FEI_DSC01a~ipad.png") as lh5 zorder (10-5) at right_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0027"
    "菲利丝""「就是？」"
    hide lh5 with dissolve
    $stopvoc("OKA")
    play OKA "FOKA_0148"
    "伦太郎""「就是……」"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA01"),"True","lh/RUK_CSA01a~ipad.png") as lh5 zorder (10-5) at left0:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("RUK")
    play RUK "FRUK_0022"
    "琉华""「就是？」"
    hide lh5 with dissolve
    $stopvoc("OKA")
    play OKA "FOKA_0149"
    "伦太郎""「……」"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB05"),"True","lh/MOE_ASB05a~ipad.png") as lh5 zorder (10-5) at left_l:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MOE")
    play MOE "FMOE_0012"
    "萌郁""「就是？」"
    hide lh5 with dissolve
    $stopvoc("OKA")
    play OKA "FOKA_0150"
    "伦太郎""「桶子，你来说！」"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB06"),"True","lh/DAR_ASB06a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0022"
    "至""「你自己不说啊喂。」"
    play bgm "BGM22"
    $stopvoc("OKA")
    play OKA "FOKA_0151"
    "伦太郎""「我刚刚不是说过了嘛，因为D-MAIL的实验导致我这几天的记忆跟实际情况不一样啊。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0023"
    "至""「啊哦、原来如此」"
    "虽然我太想去说明了，不过我连要说做了什么未来道具也不知道，这也没办法吧。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0024"
    "至""「话虽如此，可连自己的提议都不记得的话，果然吧，总感觉很不可思议呢。」"
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSB04"),"True","lh/RUK_CSB04a~ipad.png") as lh6 zorder (10-6) at left_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("RUK")
    play RUK "FRUK_0023"
    "琉华""「诶？　冈部师父、难道丧失了记忆？」"
#resetFlag SF_CHA8DISP
#call macrosys,InitCHA8
    hide lh8
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB03"),"True","lh/MAY_CSB03a~ipad.png") as lh8 zorder (10-8) at right_t:
        yalign .55
    with Dissolve(.5)
#assign $W(SW_CHA8ALPHA),0
#call macrosys,CharaSet84
#resetFlag SF_CHA7DISP
#call macrosys,InitCHA7
    hide lh7
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh7 zorder (10-7) at right_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp73
#call macrosys2,CHA_SwapLoad47
#SetSavePoint
#setFlag SF_MESSAVEPOINT_SSP
#setFlag LF_IMTHD_CTRL
#setFlag LF_IMTHD_EXEC_ALT1
#CreateThread THIS,IMTHD_MAY_01
    $stopvoc("MAY")
    play MAY "FMAY_0028"
    "真由理""「不是哟、琉华君。小冈伦呢、是那个，怎么说来着。ｅａｔｉｎｇ……」"
#resetFlag LF_IMTHD_CTRL
#flagOnWait LF_IMTHD_EXEC_ALT1
    $stopvoc("OKA")
    play OKA "FOKA_0152"
    "伦太郎""「是“ｒｅａｄｉｎｇ ｓｔｅｉｎｅｒ”」"
#resetFlag SF_CHA7DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh7 zorder (10-7):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp73
    $stopvoc("MAY")
    play MAY "FMAY_0029"
    "真由理""「没错没错，就是那个“很想做啊”的东西（注：ｓｔｅｉｎｅｒ发音与日文很想做啊接近）」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0025"
    "至""「真由氏真由氏，刚才的“很想做啊”那句话，求再说。」"
#resetFlag SF_CHA7DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh7 zorder (10-7):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp73
    $stopvoc("MAY")
    play MAY "FMAY_0030"
    "真由理""「很想做啊？」"
    
#call macrosys2,DAR_HANADI_1
    $stopvoc("DAR")
    play DAR "FDAR_0026"
    "至""「跪求稍稍把眼睛向上翻一翻。」"
    hide lh6 with dissolve
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB03"),"True","lh/CRS_ASB03a~ipad.png") as lh6 zorder (10-6) at left_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("CRS")
    play CRS "FCRS_0040"
    "红莉栖""「还不打住，你个ＨＥＮＴＡＩ！！」"
#resetFlag SF_CHA7DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC02"),"True","lh/MAY_CSC02a~ipad.png") as lh7 zorder (10-7):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp73
    $stopvoc("MAY")
    play MAY "FMAY_0031"
    "真由理""「很想做啊。」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC02"),"True","lh/MAY_CSC02a~ipad.png") as lh5 zorder (10-5) at right:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC02"),"True","lh/CRS_ASC02a~ipad.png") as lh6 zorder (10-6) at left:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("CRS")
    play CRS "FCRS_0041"
    "红莉栖""「真由理你也是，不做也可以的！」"
#resetFlag SF_CHA7DISP
#call macrosys,InitCHA7
    hide lh7
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSB02"),"True","lh/FEI_DSB02a~ipad.png") as lh7 zorder (10-7) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp73
    $stopvoc("FEI")
    play FEI "FFEI_0028"
    "菲利丝""「不对喵！　你应该以一副更加渴望的表情说才行喵！」"
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC04"),"True","lh/CRS_ASC04a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("CRS")
    play CRS "FCRS_0042"
    "红莉栖""「喂，连你也这样！」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB02"),"True","lh/MOE_ASB02a~ipad.png") as lh6 zorder (10-6) at right:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("SUZ")
    play SUZ "FSUZ_0014"
    "铃羽""「喂喂，刚才那句话，到底是什么意思嘛？」"
    $stopvoc("MOE")
    play MOE "FMOE_0013"
    "萌郁""「不知道……」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    "不好。"
    "虽说是自觉地集合起来了，但他们实在是太没统一性了，根本说不到一起。"
    $stopvoc("OKA")
    play OKA "FOKA_0153"
    "伦太郎""「总之桶子啊！　新未来道具的说明就靠你了！」"
    "总之先大喊一声让大家注意力集中起来。"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SAHSEN"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SAHSEN"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SAHSEN"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0027"
    "至""「这样啊，{color=#f00}对不住鸟{/color}」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0028"
    "至""「我看看，那么就首先介绍……」"
#messWindowCloseWait
    play se "SGSE110"
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N1")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
    "桶子从帘子隔开的对面——也就是开发室里乱放的纸箱中拿出了几样东西，放在了桌子上。"
    "这看上去就非常可疑的……不、非常有独创性的物体平放在狭窄的桌子上面。"
    "有些烦恼该以什么顺序来介绍这些可疑的……哦不，是有魅力的东西，这里就先按照桶子讲解的顺序来吧"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BIT"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BIT"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BIT"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TAKECOP"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_TAKECOP"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_TAKECOP"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ORA2"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ORA2"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ORA2"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SNAKE"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SNAKE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SNAKE"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GOEMON"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GOEMON"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GOEMON"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CYALUME"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_CYALUME"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_CYALUME"])
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GADJET_BALL"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_GADJET_BALL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_GADJET_BALL"])
#messWindowCloseWait
#assign $W(SW_MESMODE),MESMODE_FULL
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HOMING_DIVA"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_HOMING_DIVA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_HOMING_DIVA"])
#call macrosys,SetTIPScolorSingle
    "９号机『{color=#f00}哭成泪人的女神的回归{/color}』。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BIKKURI_MEGANE"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BIKKURI_MEGANE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BIKKURI_MEGANE"])
#call macrosys,SetTIPScolorSingle
    "１０号机『{color=#f00}吓人一跳小眼镜{/color}』。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BALLOW_ARE"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BALLOW_ARE"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BALLOW_ARE"])
#call macrosys,SetTIPScolorSingle
    "１１号机『{color=#f00}马路野郎滑板{/color}』。"
#messWindowCloseWait
#assign $W(SW_MESMODE),MESMODE_NORMAL
    $stopvoc("OKA")
    play OKA "FOKA_0154"
    "伦太郎""「这简直是……」"
    "果然，听完说明的我顿时无语地皱起了眉头。"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMA03"),"True","lh/MAY_CMA03a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0032"
    "真由理""「怎么了、小冈伦，头很疼么？」"
    $stopvoc("OKA")
    play OKA "FOKA_0155"
    "伦太郎""「没那回事！」"
    $stopvoc("OKA")
    play OKA "FOKA_0156"
    "伦太郎""「到底在搞什么啊，这些奇奇怪怪的未来道具是怎么回事！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CMB03"),"True","lh/MAY_CMB03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0033"
    "真由理""「奇奇怪怪？」"
    $stopvoc("OKA")
    play OKA "FOKA_0157"
    "伦太郎""「没错。不管这个还是那个，全都是些没什么用的东西嘛。」"
    hide lh5 with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0029"
    "至""「我可说好了，这些相关的东西全都是冈伦你提议的。」"
    $stopvoc("OKA")
    play OKA "FOKA_0158"
    "伦太郎""「哇靠多么牛逼出色的发明品啊！　真不愧是凤凰院凶真！真被我自己的才能给吓到了！」"
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh6 zorder (10-6) at left_t:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_CHAPRI),ChaOrder_2134
#call macrosys,CharaDisp62
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_OTSU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_OTSU"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("CRS")
    play CRS "FCRS_0043"
    "红莉栖""「自演{color=#f00}乙{/color}」"
    $stopvoc("OKA")
    play OKA "FOKA_0159"
    "伦太郎""「嘿？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0030"
    "至""「嘿？」"
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC02"),"True","lh/CRS_ASC02a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("CRS")
    play CRS "FCRS_0044"
    "红莉栖""「啊、没……」"
#add $W(SW_CHA2PRI),PRI2_BG
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5
    with dissolve
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_ATTCHANNEL"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_ATTCHANNEL"])
#call macrosys,SetTIPScolorSingle
    "我从以前开始就开始怀疑这女人了，有时候忽然一句{color=#f00}＠ｃｈａｎｎｅｌ{/color}用语就甩出来了。"
    "平时装出一副正常的样子，果然这家伙其实是＠ｃｈ众吧。"
    hide bg2
    with dissolve
#sub $W(SW_CHA2PRI),PRI2_BG
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA01"),"True","lh/SUZ_ASA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("SUZ")
    play SUZ "FSUZ_0015"
    "铃羽""「呐、冈部伦太郎，这个可以摸摸看么？」"
    "打工战士指着这一连串的新未来道具说道。"
    $stopvoc("OKA")
    play OKA "FOKA_0160"
    "伦太郎""「也对呢，你们也是ｌａｂｍｅｍ之一，没关系的吧。」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA02"),"True","lh/SUZ_ASA02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("SUZ")
    play SUZ "FSUZ_0016"
    "铃羽""「太好了！　嘿，大家，可以玩玩看了！」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    "铃羽一声令下，其他家伙也相继拿到了新作研究道具，开始试玩了。"
    "要说起来，我们ｌａｂ生产出来的未来道具成为此等受欢迎的对象，还是第一次吧。"
    "在１星期之前ｌａｂｍｅｍ明明还只有真由理和桶子。"
    "然而好好想一下，制作这些未来道具的人竟然不是我，这一点有些后悔。"
    "不，实际上其实就是我。"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA01"),"True","lh/RUK_CSA01a~ipad.png") as lh6 zorder (10-6) at right:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("MAY")
    play MAY "FMAY_0034"
    "真由理""「呐呐、琉华君。有这个伞的话，就算是遗忘在哪里了也不要紧吧？」"
    $stopvoc("RUK")
    play RUK "FRUK_0024"
    "琉华""「嗯……不过，这只是一把塑料伞而已，考虑到制作成本。直接再买一把比较……」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA02"),"True","lh/MAY_CSA02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0035"
    "真由理""「那个、在这里打开可以吧？」"
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA03"),"True","lh/RUK_CSA03a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("RUK")
    play RUK "FRUK_0025"
    "琉华""「啊、那个很危险的，请不要咔啪一下打开。」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB02"),"True","lh/DAR_ASB02a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(SW_CHA5EX),Ext_DAR_x02
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0031"
    "至""「请不要咔啪一下打开、什么的！　明明应该没有那方面兴趣的，但你这样说的话，好不甘心，但是好兴奋啊呼哧呼哧！」"
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA07"),"True","lh/CRS_ASA07a~ipad.png") as lh6 zorder (10-6) at left_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("CRS")
    play CRS "FCRS_0045"
    "红莉栖""「所以说，ＨＥＮＴＡＩ发言给我自重啊，我早说过了吧。」"
    "话说这还真是……"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA06"),"True","lh/SUZ_ASA06a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC01"),"True","lh/FEI_DSC01a~ipad.png") as lh6 zorder (10-6) at right:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("SUZ")
    play SUZ "FSUZ_0017"
    "铃羽""「啊咧？　这个眼镜，感觉不管戴不戴上，变化都不大呢。」"
    $stopvoc("FEI")
    play FEI "FFEI_0029"
    "菲利丝""「真的喵？　让菲利丝也试试喵。」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA05"),"True","lh/DAR_ASA05a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(SW_CHA5EX),Ext_DAR_x05
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0032"
    "至""「等！　眼镜娘菲利丝什么的，简直稀奇！」"
    "死桶子，兴趣满满啊。"
    "算了，反正是庆祝宴会今天就网开一面……"
    $stopvoc("CRS")
    play CRS "FCRS_0046"
    "红莉栖""「等一下！　桐生小姐、你在干什么！？」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    $stopvoc("OKA")
    play OKA "FOKA_0161"
    "伦太郎""「姆？」"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG01N")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB02"),"True","lh/MOE_ASB02a~ipad.png") as lh5 zorder (10-5) at right:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASC05"),"True","lh/CRS_ASC05a~ipad.png") as lh6 zorder (10-6) at left:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5|BUF_CHA6)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    $stopvoc("MOE")
    play MOE "FMOE_0014"
    "萌郁""「做什么……我想让这个动起来……」"
    "我看向让红莉栖焦急的源头，在房间的一角指压师正拿着滑板比划着什么。"
    "根据刚才的说明，那个滑板应该是……"
    stop bgm
    $stopvoc("OKA")
    play OKA "FOKA_0162"
    "伦太郎""「克莉斯蒂娜，现在立刻马上制止那个女人！　不要让她拿着那种东西在房间里面测试！」"
    $stopvoc("CRS")
    play CRS "FCRS_0047"
    "红莉栖""「不行呀！　桐生小姐！　再这么下去的话，房间里面会洒满可乐的……！」"
    $stopvoc("MOE")
    play MOE "FMOE_0015"
    "萌郁""「啊……？」"
#messWindowCloseWait
    play se "SGSE208"
#call macrosys,WaitSE1start
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG_WHITE")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_MASKINV
#assign $W(SW_BG2MASKNO),MASK10
#assign $W(SW_BG2MASKFADERANGE),Init_FLANGE
#assign $W(LR_FADE_TIM),BG_NORMAL
#call macrosys,BgOverWrite
    $stopvoc("MOE")
    play MOE "FMOE_0016"
    "萌郁""「哎呀！！」"
    "太迟了……"
    $stopvoc("CRS")
    play CRS "FCRS_0048"
    "红莉栖""「哇哟啊啊啊！！」"
    $stopvoc("FEI")
    play FEI "FFEI_0030"
    "菲利丝""「怎、怎么了喵？　这到底是哪一出喵！？」"
    "碳酸饮料在房间之中乱喷，滑板在墙壁上面飞来飞去。"
    "在一瞬间实验室内充满了凄惨的呻吟声。"
    with vpunch
    with hpunch
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG01N")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB03"),"True","lh/MOE_ASB03a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#/#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#/#assign $W(LR_SCR_FADETYPE),BGFADETYPE_MASK
#/#assign $W(LR_SCR_MASKNO),MASK04
#/#assign $W(LR_SCR_MASKFADERANGE),Init_FLANGE
#/#assign $W(LR_FADE_TIM),FADE_VERYSLOW
#assign $W(SW_BG2FADETYPE),BGFADETYPE_MASK
#assign $W(SW_BG2MASKNO),MASK04
#assign $W(SW_BG2MASKFADERANGE),Init_FLANGE
#assign $W(LR_FADE_TIM),BG_NORMAL
#call macrosys,BgOverWrite
#setFlag SF_CHA5DISP
#call macrosys,Disp_NextScreen
    $stopvoc("OKA")
    play OKA "FOKA_0163"
    "伦太郎""「你这个……指压师！　看你到底做了什么好事！」"
    $stopvoc("MOE")
    play MOE "FMOE_0017"
    "萌郁""「对不……起，我会好好打扫的。」"
    $stopvoc("OKA")
    play OKA "FOKA_0164"
    "伦太郎""「这是应该的！」"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N1")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA02"),"True","lh/RUK_CSA02a~ipad.png") as lh5 zorder (10-5) at right_t:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh6 zorder (10-6) at center:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA7DISP
#call macrosys,InitCHA7
    hide lh7
    show expression ConditionSwitch("renpy.music.get_playing(channel='SUZ')",DynamicDisplayable(mouthanime,"SUZ_ASA03"),"True","lh/SUZ_ASA03a~ipad.png") as lh7 zorder (10-7) at left_t:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5|BUF_CHA6|BUF_CHA7)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    $stopvoc("RUK")
    play RUK "FRUK_0026"
    "琉华""「十分凉爽……的说。」"
    $stopvoc("MAY")
    play MAY "FMAY_0036"
    "真由理""「唔哇、碳酸原来这么厉害啊，真由喜大吃一惊。」"
    $stopvoc("SUZ")
    play SUZ "FSUZ_0018"
    "铃羽""「真是的……人家全身都被搞到湿透了。」"
    "话说回来。"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ALA01"),"True","lh/DAR_ALA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0033"
    "至""「啊、阿万音氏，刚刚的“被搞到湿透了”那句话，求再说嗷！！」"
#setFlag SF_Phone_AutoDisable
    "桶子你给我自重啊。"
    $renpy.hide_screen("phonebtn")
#resetFlag SF_PhoneSD_Disp
#messWindowCloseWait
#call macrosys,FadeOutSlow
#call macrosys,InitGraph
#mwait FADE_VERYSLOW
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    $loadBG(1,"BG02N2")
#setFlag SF_BG1DISP
#call macrosys,TUNE_CHACOL_BG1
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DMC02"),"True","lh/FEI_DMC02a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaSet51
#call macrosys,FadeInSlow
    play bgm "BGM13"
    show screen phonebtn
#setFlag SF_PhoneSD_Disp
    $stopvoc("FEI")
    play FEI "FFEI_0031"
    "菲利丝""「喵喵！　原来都已经这个时间了喵。」"
    "正是宴会高潮的时候，菲利丝慢慢地站起身来。"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA01"),"True","lh/FEI_DSA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0032"
    "菲利丝""「再见喵，菲利丝差不多也该回店里去了喵。」"
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB03"),"True","lh/DAR_ASB03a~ipad.png") as lh6 zorder (10-6) at left_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("DAR")
    play DAR "FDAR_0034"
    "至""「哎、菲利丝炭，马上就要走了么？」"
    "桶子的声音里满满的失落。"
    "确实从时间上来说，也并没有多晚。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC01"),"True","lh/FEI_DSC01a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0033"
    "菲利丝""「菲利丝呀，店里还有事情不得不得回去做的喵。」"
#resetFlag SF_CHA7DISP
#call macrosys,InitCHA7
    hide lh7
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA01"),"True","lh/MAY_CSA01a~ipad.png") as lh7 zorder (10-7) at right_t:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp73
    $stopvoc("MAY")
    play MAY "FMAY_0037"
    "真由理""「菲利丝酱真是辛苦了。」"
    "顺便说一下菲利丝酱是真由理对菲利丝的特别叫法。（注：真由理对菲利丝的称呼的“菲”比正常少一个元音）"
label L_SGFD_AAA01_PHONE_MAIL_06_RECEIVE:
    $targetmailid = gc["ScriptMacros"]["FM_AAA01_RECV_MOE06"]
    if phonemailring!= "":
        play se phonemailring
    $RcvMail(targetmailid)
#add $W(SW_CHA3PRI),PRI2_BG
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5
    with dissolve
    "就如刚才所说的，真由理和菲利丝在同一家店『ＭａｙＱｕｅｅｎ＋喵喵⑯』里打工，她在那里叫做『真由喜・喵喵』。"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAID"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MAID"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MAID"])
#call macrosys,SetTIPScolorSingle
    "她这种笨笨的样子我还以为也就是勉强能在{color=#f00}女仆咖啡馆{/color}里面工作吧，但是实际上好像干得挺不错，这简直出乎意料。"
    hide bg2
    with dissolve
#sub $W(SW_CHA3PRI),PRI2_BG
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSC03"),"True","lh/FEI_DSC03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("FEI")
    play FEI "FFEI_0034"
    "菲利丝""「真由喜也不能一直玩喵，作业、可是有很多的喵。」"
#resetFlag SF_CHA7DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh7 zorder (10-7):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp73
    $stopvoc("MAY")
    play MAY "FMAY_0038"
    "真由理""「啊呜，作业什么的明天再做的说，是吧、琉华君？」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA04"),"True","lh/MAY_CSA04a~ipad.png") as lh5 zorder (10-5) at left:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA03"),"True","lh/RUK_CSA03a~ipad.png") as lh6 zorder (10-6) at right:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("RUK")
    play RUK "FRUK_0027"
    "琉华""「啊、对不起。我的作业已经做完了……」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC04"),"True","lh/MAY_CSC04a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("MAY")
    play MAY "FMAY_0039"
    "真由理""「哈呼，琉华君真是好学生呢。」"
    $stopvoc("OKA")
    play OKA "FOKA_0165"
    "伦太郎""「真由理啊、好好学习吧，因为这就是学生的本分啊。」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0035"
    "至""「今天份的“轮不到你来教训我”这就凑够数了吧？」"
    $stopvoc("OKA")
    play OKA "FOKA_0166"
    "伦太郎""「哼！　在学校里面教授的知识，我可不需要。」"
    $stopvoc("OKA")
    play OKA "FOKA_0167"
    "伦太郎""「要说为什么的话，就因为我是凤凰院凶真啊。」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB07"),"True","lh/CRS_ASB07a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0049"
    "红莉栖""「这理由成立你妹啊。」"
label L_SGFD_AAA01_PHONE_MAIL_07_RECEIVE:
    $targetmailid = gc["ScriptMacros"]["FM_AAA01_RECV_MOE07"]
    if phonemailring!= "":
        play se phonemailring
    $RcvMail(targetmailid)
    "说到底，对我面前的这个女人来说，就如字面意义，是一点儿也不需要学习。"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG01N")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='FEI')",DynamicDisplayable(mouthanime,"FEI_DSA01"),"True","lh/FEI_DSA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    $stopvoc("FEI")
    play FEI "FFEI_0035"
    "菲利丝""「那么大家！　再见喵♪」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    "全员目送菲利丝到门口直至她消失。"
    "然后，就好像掐准了时间一样，这次轮到红莉栖站了起来。"
#messWindowCloseWait
#call macrosys,Pull_Present_Screen
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02A2")
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#assign $W(LR_POST_SCREEN),(BUF_BG2|BUF_CHA5)
#assign $W(LR_SCR_FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,Disp_NextScreen
    $stopvoc("CRS")
    play CRS "FCRS_0050"
    "红莉栖""「好了，那么我也差不多该」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASA01"),"True","lh/CRS_ASA01a~ipad.png") as lh5 zorder (10-5) at right:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh6 zorder (10-6) at left:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("MAY")
    play MAY "FMAY_0040"
    "真由理""「诶、克莉斯酱也要回去了么？」"
    $stopvoc("CRS")
    play CRS "FCRS_0051"
    "红莉栖""「不，我还有2个未来道具要完成。」"
    $stopvoc("OKA")
    play OKA "FOKA_0168"
    "伦太郎""「什么！？　居然在此之上还要制作新的未来道具？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_ASB06"),"True","lh/CRS_ASB06a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0052"
    "红莉栖""「所以说，这全部都是你提出来的啊。」"
    $stopvoc("OKA")
    play OKA "FOKA_0169"
    "伦太郎""「所以说，还要我说多少次我不知道。」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_AMB05"),"True","lh/CRS_AMB05a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0053"
    "红莉栖""「不管情况变了还是没变，你说的就是你说的啊，不要再啰啰嗦嗦的。」"
    "可恶，真是强词夺理。"
    $stopvoc("CRS")
    play CRS "FCRS_0054"
    "红莉栖""「总之，既然不管怎么都要解决资金困难，就给我少废话！」"
    $stopvoc("OKA")
    play OKA "FOKA_0170"
    "伦太郎""「资金困难？」"
#messWindowCloseWait
    play se "SGSE110"
#call macrosys,WaitSE1start
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    "虽然我很想问问她这一番话的含义，但是红莉栖已经跟真由理她们说着话，走进了帘子里的开发室。"
    "资金困难。"
    "克莉斯蒂娜确实是这么说的。"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("OKA")
    play OKA "FOKA_0171"
    "伦太郎""「喂、桶子，刚才那是怎么回事？」"
    $stopvoc("DAR")
    play DAR "FDAR_0036"
    "至""「你问我是怎么回事，不就是字面的意思么。」"
    "按照这个说法，看来这次捣腾了这么多未来道具，主要原因似乎是ｌａｂ的资金困难。"
    "确实未来道具ｌａｂ常年缺少资金，但是搞成这样子的话无疑是有某些原因的。"
    $stopvoc("OKA")
    play OKA "FOKA_0172"
    "伦太郎""「这个原因到底是……」"
    "到底是什么啊，正当我快问出来的时候。"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh5 zorder (10-5) at right:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") as lh6 zorder (10-6) at left:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("DAR")
    play DAR "FDAR_0037"
    "至""「…………」"
    $stopvoc("MAY")
    play MAY "FMAY_0041"
    "真由理""「小冈伦……」"
    "就算什么也不说，桶子和真由理的眼睛也告诉我这一切了。"
    "都是你的错，一类的。"
    $stopvoc("OKA")
    play OKA "FOKA_0173"
    "伦太郎""「说、说起来，到底剩下那些未来道具是、是些什么啊？」"
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("DAR")
    play DAR "FDAR_0038"
    "至""「那就是……」"
    $stopvoc("OKA")
    play OKA "FOKA_0174"
    "伦太郎""「那就是？」"
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp62
    $stopvoc("DAR")
    play DAR "FDAR_0039"
    "至""「还是不说了」"
    $stopvoc("OKA")
    play OKA "FOKA_0175"
    "伦太郎""「什么？」"
    $stopvoc("DAR")
    play DAR "FDAR_0040"
    "至""「反正你都不知道了，做出来之后再看不也是个乐趣么？　那样更有意思嘛。」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JK"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_JK"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_JK"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0041"
    "至""「啊、那么就干脆自己想想看吧？　反正是你自己想去做的东西，这种事很简单吧{color=#f00}常考{/color}。」"
    "可恶，就算你这么说，想不到的东西就是想不到啊。"
    "而且，你越是这么说我就越在意啊。"
    $stopvoc("OKA")
    play OKA "FOKA_0176"
    "伦太郎""「那么桶子啊，不如我们这么做吧。在２个道具里面，你选一个告诉我吧？」"
    $stopvoc("DAR")
    play DAR "FDAR_0042"
    "至""「很遗憾的是对于另外的那一个，连我也不知道是什么东西喔。」"
    $stopvoc("OKA")
    play OKA "FOKA_0177"
    "伦太郎""「连桶子也？」"
    $stopvoc("DAR")
    play DAR "FDAR_0043"
    "至""「嗯，只有那个不是冈伦而是牧濑氏提出来的。」"
    $stopvoc("OKA")
    play OKA "FOKA_0178"
    "伦太郎""「克莉斯蒂娜提出的……」"
    $stopvoc("DAR")
    play DAR "FDAR_0044"
    "至""「就是这样了，自己去想想吧。」"
    "克莉斯蒂娜的提案吗。"
    show expression im.AlphaMask("bg/BG_BLACK~ipad.jpg",im.Scale(im.MatrixColor("mask/mask17.png",im.matrix.invert()),1024,576)) as bg2 behind lh5
    with dissolve
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NEURO"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_NEURO"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_NEURO"])
#call macrosys,SetTIPScolorSingle
    "也就是说，是她擅长的{color=#f00}脑科学{/color}领域相关的东西么。"
    "这样的话，作为可能性来说……"
    "……不行，完全没有头绪。"
    "唉，连自己想做的东西都想不出的话，助手想做的东西肯定想不出来啦。"
    hide bg2
    with dissolve
    $stopvoc("OKA")
    play OKA "FOKA_0179"
    "伦太郎""「哼……」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSC02"),"True","lh/MAY_CSC02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("DAR")
    play DAR "FDAR_0045"
    "至""「啊、什么？　难道你已经知道了？」"
    $stopvoc("OKA")
    play OKA "FOKA_0180"
    "伦太郎""「哼哈哈哈哈！！　这不是变得有趣起来了嘛！」"
    "事到如今，未来道具的内容是什么不是最先要考虑的。"
    "原因不用多问，就算是资金困难的情况下也做出了5个新的未来道具。"
    "看来马上就能得到充沛的军费了呢。"
    $stopvoc("OKA")
    play OKA "FOKA_0181"
    "伦太郎""「你们啊！　未来道具的未来可是一片光明啊！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSA03"),"True","lh/MAY_CSA03a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("DAR")
    play DAR "FDAR_0046"
    "至""「什么啊、已经放弃了啊。」"
    $stopvoc("MAY")
    play MAY "FMAY_0042"
    "真由理""「看来已经放弃了呢。」"
    $stopvoc("OKA")
    play OKA "FOKA_0182"
    "伦太郎""「不要在意细节！　比起这个我们来庆祝吧！　宴会现在开始！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='MAY')",DynamicDisplayable(mouthanime,"MAY_CSB02"),"True","lh/MAY_CSB02a~ipad.png") as lh5 zorder (10-5):
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh6 zorder (10-6):
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("DAR")
    play DAR "FDAR_0047"
    "至""「等等、什么现在开始啊，现在不是都已经快要结束了么。」"
    $stopvoc("MAY")
    play MAY "FMAY_0043"
    "真由理""「小冈伦你没事么？」"
    hide lh5
    hide lh6
    hide lh7
    hide lh8
    with dissolve
    $stopvoc("OKA")
    play OKA "FOKA_0183"
    "伦太郎""「来、琉华子和指压师，也一起干杯吧！」"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='RUK')",DynamicDisplayable(mouthanime,"RUK_CSA03"),"True","lh/RUK_CSA03a~ipad.png") as lh5 zorder (10-5) at right:
        yalign .55
    with Dissolve(.5)
#resetFlag SF_CHA6DISP
#call macrosys,InitCHA6
    hide lh6
    show expression ConditionSwitch("renpy.music.get_playing(channel='MOE')",DynamicDisplayable(mouthanime,"MOE_ASB02"),"True","lh/MOE_ASB02a~ipad.png") as lh6 zorder (10-6) at left:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDispW5162
    $stopvoc("MOE")
    play MOE "FMOE_0018"
    "萌郁""「啊……」"
    $stopvoc("RUK")
    play RUK "FRUK_0028"
    "琉华""「冈、冈部师父……」"
    $stopvoc("OKA")
    play OKA "FOKA_0184"
    "伦太郎""「哼哈哈哈哈！」"
#messWindowCloseWait
    play se "SGSE110"
#call macrosys,WaitSE1start
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02N1")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB04"),"True","lh/CRS_BSB04a~ipad.png") as lh5 zorder (10-5) at right_l:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
#setFlag SF_Phone_AutoDisable
    $stopvoc("CRS")
    play CRS "FCRS_0055"
    "红莉栖""「喂、冈部你吵死啦！」"
    $renpy.hide_screen("phonebtn")
#assign $W(SW_SEFADE),FADE_VERYSLOW
#stopSE 0
#assign $W(SW_SEFADE),FADE_VERYSLOW
#stopSE 1
#assign $W(SW_BGMFADE),FADE_VERYSLOW
    stop bgm
    scene expression Solid("000000") with fade
#call macrosys,InitGraph
#resetFlag SF_PhoneSD_Disp
#assign $W(SW_SEFADE),FADE_NORMAL
#stopSE 0
#assign $W(SW_SEFADE),FADE_NORMAL
#stopSE 1
#assign $W(SW_BGMFADE),FADE_NORMAL
    stop bgm
#call macrosys,InitSound
#call macrosys,FadeIn0
#call macrosys2,Init_SGFD
    return
label IMTHD_MAY_01:
#call macrosys,Thd_WaitVoiceStart
#assign $T(THD_WORK39),1400
#IMTHD_WaitTIM
#assign $W(LR_POST_CHAPRI),ChaOrder_1234
#call macrosys,Thd_CharaDisp73
#resetFlag LF_IMTHD_EXEC_ALT1
    return
