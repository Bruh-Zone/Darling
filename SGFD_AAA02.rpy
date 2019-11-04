label SGFD_AAA02:
#messWindowCloseWait
#call macrosys2,SET_SCR_VALUE
#call macrosys2,Init_SGFD
    $date="8/6"
    $day = "FRI"
label L_SGFD_AAA02_RM_AAA_RUK01_RECEIVE_STA:
    $targetmailid = gc["ScriptMacros"]["RM_AAA_RECV_RUK01_01"]
#assign $W(LR_RM_ID),RMID_RUK
#assign $W(LR_RM_CHANCE),0
    if phonemailring!= "":
        play se phonemailring
    if persistent.skipmail==True:
        pause
        $renpy.choice_for_skipping()
    if targetmailid != "":
        $RcvMail(targetmailid)
        $targetmailid=""
label L_SGFD_AAA02_RM_AAA_RUK01_RECEIVE_END:
#call macrosys2,FINISH_CHECK_RM_RECEIVE
#call macrosys,FadeOut0
#call macrosys,InitGraph
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    $loadBG(1,"IBGX048")
#setFlag SF_BG1DISP
    play bgm "BGM07"
#call macrosys,FadeInVerySlow
#mwait FADE_VERYSLOW
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG05A2")
#assign $W(SW_BG2PRI),PRI2_BG
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_VERYSLOW
#call macrosys,BG2_FadeInTIM
#mwait FADE_VERYSLOW
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    $loadBG(1,"BG02A2")
#setFlag SF_BG1DISP
#call macrosys,TUNE_CHACOL_BG1
    show screen phoneSD1
    show screen phonebtn
    hide screen phonebtn
#assign $W(SW_PHONE_PRI),PRI_EFFECT
    show screen phone(interact=False,transit=False)
#assign $W(SW_PHONE_MODE),PhoneMode_Default
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BG2_FadeOutTIM
#setFlag SF_PhoneSD_Disp
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
#assign $W(SW_PHONE_PRI),PRI_PHONE
    $stopvoc("OKA")
    play OKA "FOKA_0185"
    "伦太郎""「喂，听到没有？　出大事了！」"
    $stopvoc("OKA")
    play OKA "FOKA_0186"
    "伦太郎""「实际上……不、不是那样，比那个更麻烦的事情发生了」"
    $stopvoc("OKA")
    play OKA "FOKA_0187"
    "伦太郎""「你给我听好……Lab被人夺走了」"
    $stopvoc("OKA")
    play OKA "FOKA_0188"
    "伦太郎""「所以不是说过了嘛，发生大事了」"
    $stopvoc("OKA")
    play OKA "FOKA_0189"
    "伦太郎""「什么！？　不是，虽然这么说，但敌人手段相当高明。要是正面闯入的话，即使是本大爷亲自出马，能够平安无事的可能性也非常低」"
    $stopvoc("OKA")
    play OKA "FOKA_0190"
    "伦太郎""「哼，你还真会说……都说到这份上了，我也只能上了」"
    $stopvoc("OKA")
    play OKA "FOKA_0191"
    "伦太郎""「啊啊……我要闯进去了，如果平安无事的话，就在老地方那家店请你喝一杯」"
    $stopvoc("OKA")
    play OKA "FOKA_0192"
    "伦太郎""「EL PSY CONGROO」"
    hide screen phonemenu

    show screen phoneblank

    show screen phonebtn
    "收起手机，我下定决心试着正面突入敌阵中心。"
#messWindowCloseWait
    stop bgm
    play se "SGSE110"
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02A1")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#call macrosys,TUNE_CHACOL_BG1
#mwait FADE_SLOW
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG03A4")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#call macrosys,TUNE_CHACOL_BG1
#/#mes2v FOKA_0193,$W(LR_LIP_OKA),VID_OKA,＠倫太郎＠「おい、クリスティーナよ！　後で後でと言って、いったいいつになったらＤメールを……」&a0;
    $stopvoc("OKA")
    play OKA "FOKA_0193"
    "伦太郎""「喂，克莉斯蒂娜哟！　你老说再等等再等等，到底要什么时候才发D-Mail……」"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB03"),"True","lh/CRS_BSB03a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0056"
    "红莉栖""「吵死了！！」"
    $stopvoc("OKA")
    play OKA "FOKA_0194"
    "伦太郎""「什……」"
    $stopvoc("CRS")
    play CRS "FCRS_0057"
    "红莉栖""「我现在忙着做新的未来道具，刚才不是说过了吗！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='CRS')",DynamicDisplayable(mouthanime,"CRS_BSB04"),"True","lh/CRS_BSB04a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("CRS")
    play CRS "FCRS_0058"
    "红莉栖""「在完成之前，禁止使用D-Mail！　所以，在那之前别烦我！　明白了没！」"
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02A1")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#call macrosys,TUNE_CHACOL_BG1
    play se "SGSE110"
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG02A2")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#call macrosys,TUNE_CHACOL_BG1
    "……也犯不着摆出这么可怕的样子说吧。"
    "明明这个研究所是我创立的说。"
label L_SGFD_AAA02_RM_AAA_RUK01_REPLY_END:
    $gd["RCVmailData"][gc["ScriptMacros"]["RM_AAA_RECV_RUK01_01"]]["late"]=True
#RandomMail_End
    $stopvoc("DAR")
    play DAR "FDAR_0048"
    "至""「一句话就把冈伦轰出来了，牧濑△（好有型)」"
#resetFlag SF_CHA5DISP
#call macrosys,InitCHA5
    hide lh5
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5 zorder (10-5) at center:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    play bgm "BGM05"
    "因为突然出现的声音我抬头看了看，只见桶子正站在那窃笑。"
    $stopvoc("OKA")
    play OKA "FOKA_0195"
    "伦太郎""「不是被轰出来，这叫战略性撤退」"
    $stopvoc("OKA")
    play OKA "FOKA_0196"
    "伦太郎""「话说桶子，你什么时候来的？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IMAKITA"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_IMAKITA"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_IMAKITA"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0049"
    "至""「{color=#f00}今北产业{/color}」"
    "看来，是在我闯进敌阵的时候来的。"
label L_SGFD_AAA02_RM_AAA_MOE01_RECEIVE_STA:
    $targetmailid = gc["ScriptMacros"]["RM_AAA_RECV_MOE01_01"]
    $LR_RM_CHANCE_2=33
    call JUDGE_RM_AAA_MOE01_ENA
#call macrosys2,JUDGE_RM_AAA_MOE01_ENA
    call CHECK_RM_RECEIVE
    "比起这个还是先搞定克莉斯蒂娜。"
    call CHECK_RM_RECEIVE
    "当然，我也不是不理解那家伙想表达的意思。"
    call CHECK_RM_RECEIVE
    "身为研究者，自己的研究工作被打扰是难以言喻的苦痛。"
    call CHECK_RM_RECEIVE
    "无奈了。"
    call CHECK_RM_RECEIVE
    "虽然D-Mail的实验十万火急，但现在并不是以身犯险的时候。"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0050"
    "至""「然后呢，怎么办？」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0197"
    "伦太郎""「既然没法实验，就算呆在这也没什么意义呐」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0198"
    "伦太郎""「你有什么打算，桶子？　再去一趟ＭａｙＱｕｅｅｎ？」"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0051"
    "至""「那当然，虽然我很想这么说，不过刚刚才去过哟」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0199"
    "伦太郎""「原来如此，你大概是在ＭａｙＱｕｅｅｎ凉够了所以想来这玩玩工口游戏吧，结果发现开发室不能用，就是这样的情况吧？」"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MMORPG"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MMORPG"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MMORPG"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0052"
    "至""「很遗憾，猜错了。今天不是工口游戏而是{color=#f00}ＭＭＯＲＰＧ{/color}喔，今天发布了新任务嘛」"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0053"
    "至""「据说有以前的怪根本都没法跟它比的超强力的龙出现了」"
    call CHECK_RM_RECEIVE
    "桶子口若悬河地讲了讲那个新的龙什么的，我就随随便便应付了几句。"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MMORPG"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_MMORPG"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_MMORPG"])
#call macrosys,SetTIPScolorSingle
    "桶子玩的是工口游戏还是{color=#f00}ＭＭＯＲＰＧ{/color}，老实讲，对我来说无关紧要。"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0054"
    "至""「话说啊冈伦。就在刚刚，好像秋叶原出大乱子了，你知道不？」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0200"
    "伦太郎""「不、不知道，发生啥了？」"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0055"
    "至""「现在，不是有个挺流行的叫『幻象』的乐队么？　诶，冈伦你不知道啊？」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0201"
    "伦太郎""「别把我当傻子，这种程度还是知道的」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0056"
    "至""「是么？　真意外」"
    call CHECK_RM_RECEIVE
    "幻象。"
    call CHECK_RM_RECEIVE
    "好像是，现在人气爆棚的朋克乐队。"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHOW"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SHOW"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SHOW"])
#call macrosys,SetTIPScolorSingle
    "听说去年在涉谷的现场表现十分火爆，今年还正式出道了。与此同时被选中演唱『{color=#f00}雷Net翔{/color}』的动画主题曲，一下子就人气暴涨。"
    call CHECK_RM_RECEIVE
    "就在几天前，菲利丝说过这个。"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0202"
    "伦太郎""「然后呢，那个幻象乐队怎么了？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BSI"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BSI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BSI"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0057"
    "至""「在秋叶原上演{color=#f00}电波骑劫{/color}了喔」"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BSI"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BSI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BSI"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("OKA")
    play OKA "FOKA_0203"
    "伦太郎""「居然是，{color=#f00}电波骑劫{/color}？」"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0058"
    "至""「是的，好像是新曲的宣传活动之类的」"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_UPX"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_UPX"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0059"
    "至""「从ＰＣ用的显示器到{color=#f00}ＵＰＸ{/color}的街头大屏幕，秋叶原所有的显示屏上都在播放他们的ＰＶ，那场面真是大骚动」"
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BSI"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BSI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BSI"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("OKA")
    play OKA "FOKA_0204"
    "伦太郎""「{color=#f00}电波骑劫{/color}吗……」"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0060"
    "至""「不过说实在的，幻象乐队也真是变得有名了呐，一年前明明还是默默无闻的」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA06"),"True","lh/DAR_ASA06a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0061"
    "至""「话说，到现在还幻象幻象的，总感觉有点那啥，我在２年前就已经听腻了」"
    call CHECK_RM_RECEIVE
    "桶子继续着地狱级的啰嗦，不过老实说我基本一句都没听进去。"
#call macrosys2,LAST_CHECK_RM_RECEIVE
    "要说原因，这时候我的大脑已经被某些事情给占据了。"
label L_SGFD_AAA02_RM_AAA_MOE01_RECEIVE_END:
#call macrosys2,FINISH_CHECK_RM_RECEIVE
label L_SGFD_AAA02_RM_AAA_MOE01_REPLY_END:
    $gd["RCVmailData"][gc["ScriptMacros"]["RM_AAA_RECV_MOE01_01"]]["late"]=True
#RandomMail_End
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA05"),"True","lh/DAR_ASA05a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0062"
    "至""「喂冈伦，你在听吗？」"
    $stopvoc("OKA")
    play OKA "FOKA_0205"
    "伦太郎""「桶子啊，就是它！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0063"
    "至""「哈？」"
    "我直直地盯着桶子的眼睛。"
    "甚至可以看清他眼镜下的瞳孔在放大。"
    $stopvoc("DAR")
    play DAR "FDAR_0064"
    "至""「它，是什么？」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BSI"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_BSI"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_BSI"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("OKA")
    play OKA "FOKA_0206"
    "伦太郎""「就是它啊，那个{color=#f00}电波骑劫{/color}，难道我们做不出来吗？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB06"),"True","lh/DAR_ASB06a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    "这家伙到底在说啥啊……桶子看着我的眼神表达了这个意思。但是，我毫不退缩地继续说道。"
    $stopvoc("OKA")
    play OKA "FOKA_0207"
    "伦太郎""「听好了桶子，我们要做的事是什么？」"
    $stopvoc("DAR")
    play DAR "FDAR_0065"
    "至""「制作奇怪的未来道具然后拿来玩？」"
    $stopvoc("OKA")
    play OKA "FOKA_0208"
    "伦太郎""「错！　我们在这个未来道具研究所真正要做的事情是，破坏暗中操控世界的支配构造，并且将混沌引入这个世界！」"
    $stopvoc("OKA")
    play OKA "FOKA_0209"
    "伦太郎""「之所以要制造未来道具，正是为了那个而打下基础啊！！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0066"
    "至""「啊，说起来好像是呢。所以呢，这有什么值得注意的么？」"
    $stopvoc("OKA")
    play OKA "FOKA_0210"
    "伦太郎""「可恶，你这不明事理的家伙！　就是那个啊，不是经常出现的么。你想想，在电视上经常出现的，像是演说那样的！」"
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SION"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_SION"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_SION"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0067"
    "至""「啊，懂了。就是所谓的那个啊，{color=#f00}西翁万岁{/color}什么的」"
    $stopvoc("OKA")
    play OKA "FOKA_0211"
    "伦太郎""「嘛……就是那个」"
    "在世界的支配构造被改变的黎明时分，这种事情有让世人得知的必要，为此，现在开始准备也是有必要的。"
    $stopvoc("DAR")
    play DAR "FDAR_0068"
    "至""「原来如此呐，冈伦想说的东西大概明白了喔」"
    $stopvoc("OKA")
    play OKA "FOKA_0212"
    "伦太郎""「所以呢、做不做得到？」"
    $stopvoc("DAR")
    play DAR "FDAR_0069"
    "至""「嘛、大概能做得到吧？」"
    $stopvoc("OKA")
    play OKA "FOKA_0213"
    "伦太郎""「什么！？」"
    "因为他回答得实在是太干脆了，我忍不住反问了一句。"
    "从情节的展开上来说，这时候应该是绞尽脑汁，最终将我们全部的力量都倾注进去进行挑战，这样的走向才对。"
    "不过既然他说真能做得出来，那是再好不过了。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA03"),"True","lh/DAR_ASA03a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0070"
    "至""「但是，如果要做那个的话器材也是一个大问题」"
    $stopvoc("OKA")
    play OKA "FOKA_0214"
    "伦太郎""「我先说清楚啊，现在Lab可没有空余的钱」"
    $stopvoc("DAR")
    play DAR "FDAR_0071"
    "至""「这种事情我当然知道喔。但是，如果这样的话……我想想，这样的话，最多就是对使用模拟信号的广播进行电波骑劫而已吧？」"
    $stopvoc("OKA")
    play OKA "FOKA_0215"
    "伦太郎""「姆唔……」"
    "根据桶子的说明，要对数字广播的回路进行干扰，就现状而言是相当困难的。"
    "那么，要是只干扰模拟信号回路的话是否能够大规模实现呢？老实说这也相当困难。"
    $stopvoc("DAR")
    play DAR "FDAR_0072"
    "至""「为了拦截模拟信号，电波输出功率如果不能到达一定程度的话就做不出来哦」"
    $stopvoc("DAR")
    play DAR "FDAR_0073"
    "至""「简单来讲，仅靠这个Lab里现有的东西的话，我看看……顶多就是在秋叶原中播放任意影像，再远就不行了」"
    "这个时代还用模拟信号的电波……而且地域还限定在秋叶原。"
    "真是令人失望的规模啊。"
    $stopvoc("DAR")
    play DAR "FDAR_0074"
    "至""「嘛，就是这样了，非要这么做的话……」"
    $stopvoc("OKA")
    play OKA "FOKA_0216"
    "伦太郎""「不，这样就够了」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA04"),"True","lh/DAR_ASA04a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0075"
    "至""「这样就够了……难道你真的想要做不成？」"
    $stopvoc("OKA")
    play OKA "FOKA_0217"
    "伦太郎""「没有什么难道，就是要这么做」"
    "现在说没有意义然后放弃了，这很简单。"
    "但是这样的话，就永远不会有进步！"
    $stopvoc("DAR")
    play DAR "FDAR_0076"
    "至""「真的要做？」"
    $stopvoc("OKA")
    play OKA "FOKA_0218"
    "伦太郎""「那当然，正是这些看起来没有意义的东西、徒劳的东西，却会成为伟大成就的的基石！」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA02"),"True","lh/DAR_ASA02a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0077"
    "至""「我先说清楚了，这个即使规模很小也算犯罪哦。就算如此也要？」"
    $stopvoc("OKA")
    play OKA "FOKA_0219"
    "伦太郎""「什么！？　原来是这样的么？」"
    $stopvoc("DAR")
    play DAR "FDAR_0078"
    "至""「什么？　难道你想说你不知道？」"
    $stopvoc("OKA")
    play OKA "FOKA_0220"
    "伦太郎""「怎、怎么会不知道！」"
    "之前是不知道。"
    "犯罪。"
    "我先说清楚，我仅仅是以破坏世界的支配构造为目的的，一点都不想变成罪犯。"
    "给世界带来混沌，但前提是合法。"
    $stopvoc("DAR")
    play DAR "FDAR_0079"
    "至""「那，果然还是放弃了吧、ｏｋ？」"
    $stopvoc("OKA")
    play OKA "FOKA_0221"
    "伦太郎""「呒唔唔……」"
#assign $W(SW_BGMFADE),FADE_VERY3SLOW
    stop bgm
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    $stopvoc("DAR")
    play DAR "FDAR_0080"
    "至""「哎，我就知道结果还是变成这样」"
    $stopvoc("OKA")
    play OKA "FOKA_0222"
    "伦太郎""「你……说啥？」"
    $stopvoc("DAR")
    play DAR "FDAR_0081"
    "至""「你看嘛，不管怎么说冈伦是个胆小鬼，不好的事还是不会做的吧」"
label L_SGFD_AAA02_RM_AAA_FEI01_RECEIVE_STA:
    $targetmailid = gc["ScriptMacros"]["RM_AAA_RECV_FEI01_01"]
    $LR_RM_CHANCE_2=37
    call JUDGE_RM_AAA_FEI01_ENA
    call CHECK_RM_RECEIVE
    "刚刚这家伙说了什么？"
    call CHECK_RM_RECEIVE
    "难道这家伙、说我是胆小鬼？"
    call CHECK_RM_RECEIVE
    "我是胆小鬼、他是这么说的么？"
    call CHECK_RM_RECEIVE
    "……看来桶子是说了不该说的话啊。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB01"),"True","lh/DAR_ASB01a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0082"
    "至""「就是这样了，我要找个地方凉快去……」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0223"
    "伦太郎""「等下」"
    play bgm "BGM25"
    call CHECK_RM_RECEIVE
    "我叫住正打算离开的桶子。"
    call CHECK_RM_RECEIVE
    "用沉重，而且冰冷的口气。"
    call CHECK_RM_RECEIVE
    "现在不管拥有怎样的力量，都不能阻止我了。"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0224"
    "伦太郎""「ＧＯ了」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB04"),"True","lh/DAR_ASB04a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0083"
    "至""「哈？」"
    call CHECK_RM_RECEIVE
    "是因为没听清吗，桶子呆站着一动不动。"
    call CHECK_RM_RECEIVE
    "对着那样的桶子，我又慢慢地说了一遍，让他听清楚。"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0225"
    "伦太郎""「没有听见吗？　ＧＯ了」"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0084"
    "至""「什么叫ＧＯ……难道是说要做？」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0226"
    "伦太郎""「没有什么难道，就是要这么做」"
    call CHECK_RM_RECEIVE
    "先说清楚，我不是因为被他叫做胆小鬼才赌气去做的。"
    call CHECK_RM_RECEIVE
    "而是因为我凤凰院凶真，并不会为这种程度的胁迫而屈服。"
    call CHECK_RM_RECEIVE
    "要问为什么，因为这一切都是命运石之门(teins;Gate)的选择啊！"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0085"
    "至""「不……了个是吧」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0227"
    "伦太郎""「我说要做的话就要做！　即使这是，违背了神的旨意的」"
    call CHECK_RM_RECEIVE
    "要是事有不妙不用不就行了。"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASA01"),"True","lh/DAR_ASA01a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0086"
    "至""「话说啊，就算做出来你要放什么？　反正冈伦肯定也没想那么多吧？」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0228"
    "伦太郎""「那种东西，等到时候再想就行了。总之现在最优先的是把东西做出来，没问题吧，我可靠的右手(My Favorite Right Arm)哟」"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0087"
    "至""「是是，知道了喔，作为代替，我就看情况地使用Lab的东西了」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0229"
    "伦太郎""「啊啊，没问题，赶紧做」"
label L_SGFD_AAA02_RM_AAA_RUK02_RECEIVE_STA:
    
    $LR_RM_CHANCE_2=11
    call JUDGE_RM_AAA_RUK02_ENA
    call CHECK_RM_RECEIVE
    "这样的话就又有新的道具、１４号机的筹划了。"
    call CHECK_RM_RECEIVE
    "到时，不得不再开一次圆桌会议来命名呐。"
    call CHECK_RM_RECEIVE
    "总之，现在在这里要做的事情已经全部做完了。"
    call CHECK_RM_RECEIVE
    "之后就交给助手和桶子，我去秋叶原视察好了。"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0088"
    "至""「嗯好吧，估计牧濑氏的工作告一段落的时候就抓紧完成吧」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0230"
    "伦太郎""「那么之后的事情拜托桶子你了，我出去一下」"
    call CHECK_RM_RECEIVE
    $stopvoc("DAR")
    play DAR "FDAR_0089"
    "至""「啊，冈伦」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0231"
    "伦太郎""「什么事？」"
#resetFlag SF_CHA5DISP
    show expression ConditionSwitch("renpy.music.get_playing(channel='DAR')",DynamicDisplayable(mouthanime,"DAR_ASB02"),"True","lh/DAR_ASB02a~ipad.png") as lh5:
        yalign .55
    with Dissolve(.5)
#call macrosys,CharaDisp51
    stop bgm
    call CHECK_RM_RECEIVE
    if persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DAIJOBU"]]["Check"]!=1:
        $persistent.gd["TIPSData"][gc["ScriptMacros"]["TIPS_DAIJOBU"]]["Check"]=1
        show screen tips_pop(i=gc["ScriptMacros"]["TIPS_DAIJOBU"])
#call macrosys,SetTIPScolorSingle
    $stopvoc("DAR")
    play DAR "FDAR_0090"
    "至""「{color=#f00}那样的装备没问题吗？{/color}」"
    call CHECK_RM_RECEIVE
    $stopvoc("OKA")
    play OKA "FOKA_0232"
    "伦太郎""「放心吧，没问题」"
#messWindowCloseWait
#resetFlag SF_BG2DISP
#call macrosys,InitBG2
    $loadBG(2,"BG01A")
#assign $W(SW_BG2FADETYPE),BGFADETYPE_ALPHA
#assign $W(LR_FADE_TIM),BG_SLOW
#call macrosys,BgOverWrite
#call macrosys,TUNE_CHACOL_BG1
#call macrosys2,LAST_CHECK_RM_RECEIVE
    "我转身背向窃笑的桶子，向着炽热的天空之下迈出了脚步。"
label L_SGFD_AAA02_RM_AAA_FEI01_RECEIVE_END:
label L_SGFD_AAA02_RM_AAA_RUK02_RECEIVE_END:
#call macrosys2,FINISH_CHECK_RM_RECEIVE
label L_SGFD_AAA02_RM_AAA_FEI01_REPLY_END:
    $gd["RCVmailData"][gc["ScriptMacros"]["RM_AAA_RECV_FEI01_01"]]["late"]=True
label L_SGFD_AAA02_RM_AAA_RUK02_REPLY_END:
    $gd["RCVmailData"][gc["ScriptMacros"]["RM_AAA_RECV_RUK02_01"]]["late"]=True
#RandomMail_End
#messWindowCloseWait
#call macrosys,FadeOutWhiteNormal
#call macrosys,InitGraph
#mwait FADE_SLOW
#resetFlag SF_BG1DISP
#call macrosys,InitBG1
    $loadBG(1,"BG05A2")
#setFlag SF_BG1DISP
#call macrosys,TUNE_CHACOL_BG1
#call macrosys2,FadeInLFLERE2_LEFT
#mwait FADE_SLOW
#flagOnJump LF_DEBUG,L_SGFD_AAA02_DEBUG_END
    return
label L_SGFD_AAA02_DEBUG_END:
#call macrosys,FadeOutNormal
#call macrosys,InitGraph
#call macrosys,InitSound
#resetFlag SF_PhoneSD_Disp
#call macrosys,FadeIn0
#call macrosys2,Init_SGFD
    return
