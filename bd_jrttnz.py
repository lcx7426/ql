"""
————————需要py3.10版本，新版青龙可运行————————
time: 2023.7.23
cron: 1 7 * * *
new Env('今日头条自定义配置版本');
今日头条刷视频，非黑号一天4块左右
抓包：点击宝箱，开宝箱看视频，连续看两三个都可以。
返回找这个url: https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?
url参数 = ？后面的所有内容
cookie参数 = cookie所有内容
x-argus和x-ladon和user-agent在请求头里面找
注：url不要前面域名那一节，只要问号？后面的内容，从luck开始

"""

# 账号配置
################################################
# 卡密
km = ''
# url参数
url = ''
# cookie参数
cookie = ''
# x-arfus参数
argus = ''
# x-ladon参数
ladon = ''
# user-agent
ua = ''
################################################

# 任务配置
################################################
# 视频之间延迟,默认最少等待50秒，最高60秒
ycmin = 50
ycmax = 60

# 看头条任务次数
read_nums = 20

# 看广告次数
gg_nums = 10

# 宝箱视频次数
bx_nums = 144

# 连续视频次数
lx_nums = 330

# 是否运行异常时重新运行 True/False
run_yc = False
################################################

# 任务选择
################################################
# 要运行的任务配置 True 不运行配置 False。
# 多任务可能会增加黑号几率，自己配置是否运行

# 每日签到
run_mrqd = True
# 小说签到
run_xsqd = False
# 吃饭补贴
run_cfbt = False
# 头条任务
run_ttrw = False
# 广告任务
run_ggrw = False
# 宝箱任务
run_bxsp = False
# 连续任务
run_lxsp = False

################################################

try:
    import marshal, lzma, gzip, bz2, binascii, zlib;

    exec(marshal.loads(bz2.decompress(
        b'BZh91AY&SYc\x9dHk\x00\x05"\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x10\xff\x03\xee\xf3\xef\xbb\xb7\xbd-\xd6\xfbu\xf6\xd7\xba\xe6\xeeZ\xf7\x1d\xdd\xf5}\xce\xf7\xcf}\xed\xf5{\xaey_,\xf7\xdf>\xf7\xce\xedw\xde\xd7=\xeb7}\xee\xbc\xdd{\xbcwo\xbd\xd7\x96\xe2\x14\xdbMOA=S\xc4\xf4\xa6z\x98&\x8f)\x9aL\x8cM0\xd4\xd1\x8dG\xa5=24\xf5\x1e\xa1\x84z\x87\xa84\xf56S\xd4\xc8\xcdM\x1e)\xea`&\x8fI\x88\xf2\x9aO\xd4\xd0M\xe9O&\x8d4\xc9\xe4\x8d=L\x93z\x88\xf4\xcay\xa9\x8d\x1a\x18\x8c\x86#P`F\xd2l\xa6\xc9C\xa9\xa4\xfd&\x99\xa9\x84\x9f\xa4\xd34\x9a5<\'\xa15<\x13L\x8d\xa9\xe8\x8d12y#\x14\xfdCA\x89\xa1\xa3\xca4\xc4\xc9\xb511\x1a0S\xc9\xea4\x9eL\x93\xf1S\xc6\xa9\xe2c\x13S\xc8\xd2f\xa3d\xd3)\xb0S\xd4\xf41\'\xa4\xcd&\xa7\xea\x9e$\xfdOD\xda\xa6\x134\xc4\xf5"\x14\xf0M\xa2f\xa6\x99&m)\xe3Jxi\xa2d\xc4\xd4\xf2\x9f\xa6\xa7\xa96\xa7\xb4Si\xa9\xeax\x14\xd9\xa9\xa9\xe6\x9a\xa1\xec\xa9\xeaxS\xd4\xf2\x1bMM\x1eL\xa6\xd3F\x83\x08\x13\xd1\x95=\xe8\x9a4\xa6\xd3h\xa3\xcaz1\x1bI\x9a\x9ajx\x9e\xa9\xb5\x1e\t=\'\xb56\x83A5<L\xa7\x89\x89\x94Jx\x1a\x9bJy\xa6\x93i\xa9\xa9\xe3S4\x9aM\xa3\x10\xf4)\xfa\t\x91\x8ay\'\x88\xf56\x04\r\xa9\x93LM\x03$\xf56\x9a4&&\x9bI\x91\x88M\xa9\xfa\xa6\xd1\xa6F\x99\x18I\xfa\t?H\xc3Q\xa65451\xeai\xa6S\xdaL\x13h\xa7\x89\xe8\x98SOL\x98\xa2D\xfd\x14\xf1\x92\x9f\xa4`\xd4<\xa6\xa7\xb4\xd57\xa3#ML\xd3S\xc8\xc1\xa9\xa4\xf4i\xa0LI\xe3HF\xcaf\xd4\xf4\x9a\x9ay4\xf4Ljd\xcd&\xa6\xd4\xd8\x13jji\xb4\xc9\xa3\xd2i\xeabf\xa9\xa6\xc9\xea\x8f\xd1\x13\xf4M\xa9?S\xca\x9e\xd3SF!\x86\x80\x99&d\x9b\t7\x92\x10\xca`\n<\x8dM\x93\xc96\xa6M\x14\xfc\x94\xf4d\xc9\x845\x1e\xa3\xd4\xfdF4\x02f\x90\xd1\xa8\xfd\x11\xead\xd1\xa6M6\xa6&M\xaa<jjy\x06\x83\x11\xb4\x99O#\x08\xf54\xd4\xf22\x9ai\xe2yM\xa5=O\x06\x83Tm6\x812\x9bOT\xc9\xe2\x1bRm2\x1bS4\xa6lX\x90\x07\x8c\x12\xfeHs\xc8\x91`\x18\x10\x03\x17\x84D\xe8\x80\x9d(\xf7\xa2\xc7\x88bZ\x89\x91\x8cZ\x16N \x0cR\x82+\x861I\xe8\'\xe5"\x19\xd2\xc0\x9f<-^\xed\x93\xa4s\xeeQ\x18c\xdfY\xc2\x08\xe9\x80\xc5\x00\xc5\xb1\xb2\xeb\xa4\xc6\xaf\x11\xf6\t\xd2\xe1\xd5)/\xd5I\xcf?\x8d\xb1\xec\x1cr3`\xcf>\tv\xfc\x06\x81\xbc\xb8\xf3<\x9b\xc6m\xe0\xef)\x1a\xe8%\x9b\xce\xc3|\x93\xb54\xbce\xdb\xe4\r\xc2z\x16\xb6\xefx,\xc0\xb1\x0bF\xce*\x9aB\x05[\xd6\r\xae\xfe\xffkg\x8a\xc7\xb9\x84\x95\'1\xdb\\J\x85l\xcc\x08nq\xe6\x08\xff\xc9[\xa8\xae\'\xdal|\x92Y\xbd\xc9!\xdb\xe3\xd9o\xec\x7f\n\x8a\x00Jj\x1c\xbd\\6\xc8\xea\x0cj\xfbJY\x86eN{\'N\x15\x9c;cl\xddP\xaf\x97;\x9a\xce\xfal\xf08UfM\x19}\xe7\xd3M\xee"\x99\x7fp\xb3C{F-\xa3\xa8\xd5,\xe2B7\xc8\x9a\xe5\xe2\x00\x0bG{\xf4%$\xf6\x8bb\xbc\xd4-5U\x93\xfe.\xfc*\xaa\xb8\xc4\xb9$\x1a\xc8DU\xcd}<o-\xb8\x15\xdb\x9d\xee\xd7\n\xd3|\xc4r\nsd\xc8\xe82:\xa3\xc09\xb5\xac)\x0b\'\xdd\xe6\x12\x18\xe6K\x84\x8f`\x83h\x8f\xb9\x04U\x92\x1f\xd6\'\xf01\xd6\xe4\x04UGH\x11\xf9\x83\x12\t\xac\x1d\x17\x18\x83\xcfZc%8\x91\xb7\x19\x11\x9b\xea ^\x1c\xb6t\xc9\x95\x97+\xd4\xa8\xc7\xe6ox[\t\xc2\xbc\xec?\x16T$\x90^_N\xbd\x970{\xe1\x17\x1e\xbc\x1d\x84\xb3|B\xc2\x16T{\xa0\xe8\x0f\xe9\xae\x00=\x83.W&\xb3\xe2"\x91\xc3J\x02:}Yo%\xfc\xdf\x17\xa8\xf0\xfejv$\xaa5\xbcy\xc4\xb6*\xce1\xe8 J\x8fGC\x92\x9f\xda\xde\xb8\xcd\xc1\xc4nB\xb2\x18\xd8\x17\xe2\xaf\xa1Wv\x0e\xf8\x8b\x04W\\9\xeaT u5GQ\xcf\xefQB\x05\t\x95\x1btA\\N\xf26\x8d1\x9biVTi>\xbe\x0f\x83\xb6\x844\xff"\x9e\xe0\x0c\xff]\t*\xf9\x86\x0c\x9d>\x94\x99Tq6\xc5\x0e\xc9X\x95\x94o\xbd\xd6a\xf4\xaaa\xb0\xfc\xe6Rp\xf8\x16\x8f\x01\x99\x8d\xe5\xf2\xec\x98\x1e/\x8b\xe7\x7fv^\xfb\x0b\x80\x9a\x8a\xd9z\x1a\xc6\xfa\x1c\xd2\xd9\xbd~\x07\xc8\xa4\xa6\x12?\x85\xdfkc\xf3\x07\xd5\x05MS}\x01y\xd8\xc4\x18:\x95\xf0\x87\x8d~\xee/Ip\r\xc7\x99\x19\xb8\x80\xa4\xa72\r=\xd5\x80\x93nj\xb6\x9aU(\xc7\xd1\xfd;\x01\xe8(\xeeO}\xaein\xbd\xfd\x94$\\\x93B\xd8\xc5\xb9FU\xb1)\x9eu\xfcp\x07WI\x81oSm e Y\xe7|\xf1<\x13\xcf\xbe\xfeE\xba\xe5\xa6\\\x10S\x8e\xe4\xce\nV\x9a\x82\xfb\xa7\xfe\xaaW!\xa9\xc9\xd7S\xea\xf9\xe3\xba[\xa7\xfe\n\xe0\x05\xdf\xbf\x9fm\xe5Q5\xf8\xcb\n3{\xfe.e\xab.\xd4\xc1W,}\xe3\xd4\x94\xb8\xd0\xbe\x91\x0e\x9f\x86\xc2\x9a;\x9c\xac\xed\n\xa2*1\x1d\x87<\x024M\xa4\xcd\xa4\xb2\x0c\xc0\xf2\xbc\xd6Z\x18\xecF%\xe6\xdci\xf4\x01\x91\x1c\xc7\xb5\x7f`\x08Ut\x0e\xd26\x17\xa8\x1e\xa5\x0e\x1dK\x90\x1b\xbfKTp9\xbb\x0c\x08Y\xcf\xa0V{\x98#\xfb\xc9\xbeA\x89v\xad\x9a\xb5G\xf7\xe4\xa4 `\xd8\xa4o7K\x95\xe3l\x01#]i\x9c\x9c63\x16\xea]9j\xac/\x0b\xac\x99\x9a\\^E\xe3\xad\xfe=\x12\x99V\xdf?\xf2FG\x81\xd9\xce5\'|!\xd2\xe7k\xa5?\x05\x80\'\xcb\xc7M\xcc\x0eu\xb5\xdez\xa7"\x8a\x84T~c\xd8\xd5\x0f=\xd3is7|\xaf\x074h>$\x18\xab\x19\x01\x86\xbd[\xb0\xa7\x81\xe2\xf6\xe0F\xd5\xc8\x8f\x9bd\xdbPch\xaf8\xd2\x9cR\x03\x7f==\x93\x06<M\xa4\x81\xa8NM}\xe5x\xb9\xcb\xf0\xaf\xf9\x84\x99\xe1NU\x15\x1dP\xc7\xb9\xd2\xba\xd77\x00\xf7\xd8\x93\xfc\xe5\xb7\xf9\x9a5\xf9d\xf0\xa0}\x93\x07\x8d!\xc3v\\\x19@\xe8\xbdG\xa4\xd6+2\xdd\xc7_\xacE\x9e\x0c\x9c\xcd\tV\xe1\xe4\xcb&f|9-I\xa3\xb3\xf3o\x97j~\x8bYG \xae\xce+"(\xe5\xc3\x10\xa0@Z\x10\x96y\xac\x90\xc9:\xee\xd23.\xf7\xeb\x80\xd6\xd4\x97n\xab\xad\xbb\x97L~\xf2/\x10-\x16\n\x94\xdd\x90n\xe7\x03\xe5\x1aY1\xc7\x88\x15\xb9 X\x05T\xbd:\x1eA\x9fCe\x9a\xdbV\x15\x94\x05s/cx\x96\xda\xfb\xfc8=\xceU83\x08\x89K\x02\xe0\xea\xe6\xa0w\xa5~\xb7R\xee+\xd1\xb3\x89\xcf/\xe6*\xeb\x0b\xabY\x01\x15\x8d\xde\xa7+\xe3@\xa0\xcc\xe1\x0c\xe7\xd6\xe4\xeb\xfa\xc3\xa2\x94,\xc3!\xfa\xd2D\xbc\xe8D\x14\xa69m\xce\xee\xec\xf8\xbb\xe2\xfa\xe8\xe5\xf3h\x89=8\xe9\xb3T\xa2\xec\xd7T\xcd6\x1c\xdd\x13\xd4F\x94O\x19r\x9f\xc8l\x0bXx.\xf9>\xe5\x9f\xb9\xdd\xdd\xf79\x92a\xe2*%)g\x9bw\xa1\xb1\xb44\xf9M\xac\x1e\xd1Cb\xfe;\x7f\xbe\xafZ\x1a\x04\xdc5\xeewXE\xea4\x08\xb8j\xedK\x8f\xfb\x12\x1b\x07\xf5&\xaa\x8f)\xb4\x83\x08\x04\x86\xbc\xf0mb\x1fM5s+\xfd\x9e>\n#\xc7\x7f-\xfb\xf7j\x08\xdbv\xf2\x12\xd2\xdd\t\x9c\xe9\x97\xbd\xf6d;W\xab\xcdF\xb3\xab\x16x\'E\xc2\x91T*\xc7\xeb\xd2\xb6\xf3\xc7\xbe\xb0\x80l\xaa\\\x9cH\xb2\xa6\x8bZ\x0c{<\x0f\xaf\xdf\xa8^t\xce\x13v^\xdc\xf7\xc7\xce\x84\xf8~\xec#W=L\xfd\x86k\x95\xcf|\xd0\xc3d\xac\xda-b\xb3\xb5a8M\xe6\xecv\xd1\xe1\x8b\x01V\xbd\x80\xef\xa6\xc7k\xbb\x18r\x88\xbe\x9fY\xe6\xf5\x19\xfb\r\x7f\xf2\x9e\x04-J\xf8\x91\x82v\xac\x81Z6\xcd\xa8\x87\x93\xafU\xa9\x08\x91\xa4\xad\xa9<\x0e\xbbES\xf7vQDv8\xb9\xd8\x85-2\xc9/\x06\xb8s\x9c\xf4\x84k\x87\xfa\xd9\xe4\x17V\x05\x83\xdc\xd6\xa4.#`_:YmN\xab@\xee\x8eLMm-\xa1\xbfD\xd6aZS\xda\xf7C\xcf0Y~\xbf\x83\x87\xafW\xd6R\xd0\x17\x86p"A2\xb2\xf0\x1bF\xa4|\x85\xe2M\xbaO\xf9\xfa\t\xab \xa0\x84\x0b\xc3\xdb\xec\xf0_\xc7\xcc\xe3\xac.G\x93\x85\xe4\x83\xcb\xa9m&A\xd1M\'\xe5E!\x93\xb6\xab_\x10e\xe3\xd4\xf9\x14\x1f5\xc6\xb9\xd2\xc0\r\xa2\xdc\xc8\xff\xd3\xe6\xd7j\xd7@\xfe\xaa\xf8\xda\xa0\xa1\x8a\xef\x04\xcd\x9d \x1bB\xf6+\x1e~\xb5:\xc9G\xc3y\x86\xd6\x04\x1dV5l\x98[\x88\x9a\nYjj\xb2\x89}\x17\xb3\xed\x9a\xbb1,DB\x10K\x18\xfa\x1f8MF\x01h\x8e\xfa\x81\x0by\xc4K\x96t\xaeY\xb0Hb8\x962s`\x9e\xc3\xe9-\xd9\x99\x80f\xcbl\xecl{\xfbN\x9ax~7\xcc\x1e\xe6Bp\x8e\xd7\xc5\x9f\x9e>S\xe6Y\x07\xc2O\x04\'\xc6\xa4[\nqc8\x13D\xf1\x0e\xec\xf56\xd9\x1fna\x997\xaa\x8a\xf6\x19\xde\x1e\xb6\xc3\xbe\xa6\xd9\ti\r\xad\xbe\xc5Km\xac\xd0.&\x94\x11\x82#\x14\xe0Al/\xceQ\xc4\x81\x8eO%E?B\x9cL\x03\xbeJ\xe7\r2\xff\x13\xc3W\xa8\xa5\x92k\xa3\x1d4(`\x9d\xb9=N\xc8\xafS\xdd\xf7nm\xd2z(\x83+\xf7i\xfa\xde\x93\xd2\x8dtw\xc8\xd0\x8c\x9e#\x86\xecn\x92\xc3\xb7\x80~\xdeI\xbc\xa3\x10\\\xfe\xdab\x88\xb8\x05\x10_\x7f%\xa0\x8be\xaa\x16\xda\x13-\xd9\x1a\xc5K\x95\xb3\xf5Wt\x0c\x12\x1aM\x1fI>\xf4\x19\x1d\xf5\xa6^\x10\xbd\xc7D\xfc\xc1\xe4\xa9%\x1a\xf0c\x15,\xc6\xda/:\xcb\xa0Mu+\xd7\x19\xe2\xeb~c%,`\xa6u\xec\xfa\xd7\x8e\x01\xb1\x1fZs9\xd9J\xfb\xfe\x860\xe9\xd9h,4x\x00w\xdf\x8e\xb2f\xb9Y\x12\xa8\xc2\x89\xf0\xc5\xbc\x1f\xc3\x9e\xccv?\x91\xf6?\xc5\xaa\xc6v\x81\xb3\r\x96\xf1\x9b\x18\xa9)\xd9\x9c.\xd1S\x1dW\x199\x06u\xaa\x05\xd2\x8e\xdbv\x0c:\xe2\xdas{\x07\x81\xbcX5a\xe1,\x99\n2\x9a\xf8\xe7S\x13\x8f\'|Xt\x91\x8asOwL\xad\r\x88\xd0BP\xaa\x8b\xe3zA\x14\xed\xcd\x1b\x85\x17\xbbT\x83\xa3sW\xaf9\xe8\xae\x95\xcc\x92\xd8\xdd\xeek=\x0c\xd0\'ZF\x94\xd4\xee\xb0\\7\x90\xb5\xb9R\xdb<\xe7P\x88\x9aE\xc3\x99\x8c=\xdc\xde\xbcvG[\x95X\x05j+\xb6\xfeS\xa09\xffR\x94\x1d\xee\x99\x89 \\\x13\x1e\x07\x8e_A\x0c2a\x8f\xb6C]\x142ar#\xd9t.\xc0\xba\xe58\xaeyh\x8aa\xcd\xe0\xfb\xfa\xc1+\x8d\xc5\x05"\x91\x1e\x08\xd9\x8a\x9d\xdes(\xb0\xec\x8b\xae\xa0\x88\xe1/\xf3\x03ld\x99\x17\x93\x95\xfd\xb79\xd8\xb6\xd6\xf9sW\t\x93\x08LLGw\xf6VpK\xa2\x144\x97\xbb\x94m\xb7<\x19\xc1\xd7\xcc\xac#`!\xe2\xe8\x8b\xd2&B[\xf9\xd5F\xd1$\xa8m\xb1E\xae\xac&\x969/\x0b\xe0\xaf\x1d\x9a\xd1\x0b,\xbam\xd0FP\x00\xe0\x1f{\xeb\xb2\xae\x96\x98\xc2\x8c6>\xfak\xb2\xfb\xcaa(\x8a\x8fVz\xab\xe5\xa2\x95\x14\x8f\xde\xab\xb8\xdakQ_o`\x94\x93\x9bR\xc9U9\xbe`r\xbd\x1c\x8bM\xc7\x95\x8d\xa4;\x07\xda\xdb\x06\xdafQ\x046\xe55\x10\xd8\xc7\x85\x83\xfa/\xb0e\xa7Gzzs`\xae\x87\xad\x14\x0f\xb0\xf9\xfe\x85\x99\x88\xea\xa1<\xfa{ck\xc7\x83\xfa\x15\xa0\xca\xd6\x9a\xf9\xc3\xa7y\x9d\x10\x9cF\x9d\xec\xb0\xa1-\x9c\xee\xdb(\xfb\x9d\x0cd\x00\xe6\xc1\xd4?m\xdc[\xe0\xc7;\xd1&\x08m\xfe\x87Le\x00\x11\xc5z>\xa7M\xe1\xd9\x86\x81\xda\x84\xf3DY,\xd6\xec\x19\x19L\xa1\xb7\x05\\\x00\xf6E#\xb0N\xd6\xa6\xd8B\x9fD\x1e\xbf\x16\x85wN\x17\x8f\xab\xcf(l\xa8j\xfb\xaf\x9f\xd19EbIe\xe3\xd1\xff\xb5\xa8\xda\x8f\x9b:!\xde\xc6l\xfc\xa7\xf1\x81\x9aQ\x848\xcaw\xdf\x9e\xe5Q\xe3\xbfnA\x1b\xb7\x8b\xc75|6\xd6f\xe7\x93\xe6\xf2\x82!\xb5V\x99\xa0\xc8A\x02\xe2J\xad\xe2\xd1\xd0\x1e\xc1o\x14C\x06\x1a\xa2]\xd1\xd3\xb9>\xc1\x85\x05\xfe.\xbb\x1d\xf1gh\xea\x97\x86\x97\x1d\x12\xbc\r\xa6\xa0>)\xbc\xe9\xc6\x13"B\x80s\xf1\x871t\xa4\xdb\xb1\x0eN\xa2\x03\x00ue\x1d\xba\xb5\x0c\xfa\xfd{\xc0\x0b\x95\x98\xbdn\xc4\xe5\xfd\\\xce\xb8\xcboV\x14o\x88\xe0<\x96\x80\xdc\xfd[\xcd:\x1d#=\xa1\xa0$y\xf3\xadD_\x1b[\xf8\xc2/\x1e\x83\x01\xc9\xf1\xd3\xef\x7f\xd3\xea5I\xfc\xb26\x85\x9b\x80>o\x17\xda\xfcI\xd6z\xd6\x14\xe8\x19\xb8\xa3j;\xa2>\x9f\x19\xeb[\x97\x82\xf7f\xf7+\xee\x97\xbb\x8c\xd6N.|\x03\'$Z\xc3\xe7\xed\xebJ\xc9-\x12\xf63\x9d\x13yo\x8d\\\x01\x8c\x8aS7\x1f\xd9\xcc\xaf+\xed\xc9\xf8\xd5\xcb\x16lt\xce9\x1a%\x17\xf1Xu\x88Z\r+,\xb4|P\x10\xc9)\xfb\xf8\xac\x1eP\xd2=\xcdK3*\xba\xa31xP\xd9\xdaL.\xf5Wk\x83\xd6\xa9\x9e\xfd\xd7V\xb7>\x00\xce\xfe\xd6\xbbT\xd2\x01\x02kY\x18\x95&\x11\xd6\xc5\x9cZ\xc3\xadn\xb0\xc9l1\xdf\x92:\x0f\x7f~\xbb\xa5R7\x10\xb0\xa2\xda7\x7f\x88\xfb\x8c\xc6\xbd^2\xc9\x14\xe7\xb7\xd6\x9e\x1dQ\x16-R,\xf9\x07\xb2%\xac\xcb#\xde\xff\x0fC2)\xca_\xc4H\x8a\xc4\xe5{*\x807\xf6\xd8\xb9D\xdd\xf2g\xbd\x9f-\xf8\x96t\xd5\xc38P\xc2\x03\xd8#a\xca\xba\xde\xfbW\x8e\xf2\xf6\x94\x94\xe8\x0c\xfe\xbcQQd\xc4Sb\x18PF\x97\xa8]o\xb4\xde\xe6>\x8f\xe1\xe5\xcf>e\xc5\xf9C\x9f\'#f\xfe\xdc\'\x08\x1ed<\xa3S\xe4\xa4\xf5Z\x1d;\xd6S\x11\xd8\x85RA+\xc2_\xae\xfc;\xef}&\x80=L~Q;w;w\xaf\x9f1\x8c\xf3\x97\xc59\x83j\x05yYs\xda#d\x8f\xe2I"^\xafc0\x16\x15\xc5dX6\x1e\x89\xc0\xe7\x86F\xb3H{V\xca\xa8\xd9\x10\x8c\x1d@\xc6(\xc1\xa0\xde\xdah\xe10\xf9\xe6\x87\xfb;\xd6\x956\x02\x0c\x88N\xadl\xf4{F(\xdeL\xa1\x8d\xb4c\xd4\xbc\x9c\x93vD\x8a\x98\xf3\xf6eI\xa2\xe7\x9cu\xcd\xa0Op\xc7\xfd\xa9\xbf.*\x9a\xce\x1e\xab\xdb\xba\xa4i\xd95db\xdb\xe9G\xcf$W)\xdaiG\xc8\xe5I\xd0\xc4\xfc\xda\xdb\xa7!\xa3\x9d\xe5\x8f\x0f\x84\x12Z\x8b\r\xac\x9e16\xef`x\xe2\xa9;\xa0\xee\x1e\x97\x07\xbe\xba\xa3_L\xa3d\x93\n\x89\xd2\xb6~\x0e\xec\xc2\xe6"\xed\x1c\xdcB:\xefeycn\xfe\x18Y\x7f\xc1>\x8eE\x0e\x1b]Y\xb6\xe9H\xda0\xacV\xc5\xf7\x1e\x8d\xe3K\xd2"\x9c\x90[\xd1\x87\xec\xb1\xbe\\\xb1\xe9&\xa2J\xeb\x89jSS\x05=\x85\x1fhk\xc0\xd1\xbc\xd6\xdf\n\x87\xf0\xcf\xff79u\xdd\x94\xd5\x10\x04\x9a[@\xc2f\x8cb%xJ5\xa1!\xaelf\xe0eSZ#\xadB\xf8;5\xd2\x83m\x9f\xe9\'z\xc1\x11\x15AF\xd5=x\xd8K\xb5\x9c1\x12pL\xfd>\\\xa6\xef\xfdK4!\xf0EI\xf2\x02\xb89\xa8\xbe\xf7&\x92\xe7fi\xb2\xaf\x19\x8b=\x9e\xb7\x9dG\xceg\xf4\xf1w\xbb\x98U-\xad\x88gw\xda\xe9\xe1\xb0\xeb\x15\x18\xc1\xb7\xad\xa8\xea\xc0r\x0f\x06\xc1\x9cZ\xb1\xc8\x7f+\xa7\xb0P\x98P\xcaL\xf9\xe4ke\xc7\x93\xbe%F\xb8\xf9\xba\x1f_\xcb\xf4\xee\\\xa5L\xa7M5\xb6\xb0\x01\xa1\xce\xdc\xab\xeaR\xd2\xb9\xb0\x9b\xea\x87\x0e\xd83\x96L2r\xedz\x18\x9eq\xd6\x9ej\x7f\xecI\xe8Bpne+\xbbr\x7fX*\x00\x96s\x85A\n-\x16\xed\xed\x86\xb9\x99F\x84,c\xf2\x06\x1a\xdc\x1e\x8f\xefA\x06\x13\x8e\xd0\xda\xb8\xf8\xdc\xf7*\xa2\xe8??Vi\xe5\xa4nVz\x94[p3\xce\xc1|b\x81b6m6\x85iR\x9d\xefu\x01w.\x9e\xbagZ\xad\x7f/\x0c\xa2jyWy\xf5~\r\x9d\r\xf3Nb\xb3\xd8OJ\xb5\xd5BJ&~\xfe\xc3\x8b\xb5\r\xf2\xa4\xdc\t,\xab\xb4\x04\xd3\xe1|\xad\xef8;\xceG\x11]\x0f\xb0\xaf\xb0\xd9\xcf\'\xdd\x1b\x00nZ\xcate\xcf\xe0\xa1\xd4\x9d\xe1JFDq\xa0\x85#\xda[\x80\xd2\xe0\x96\xd1\xf9\xb1\x14\xfd0\xe9\xe6\x0e\x1e5\x1a\xcf\xb8\x11\x81\xd3=\xe3P\xfb\x83\x01\xd2\x99\xbe\xd5\x84\xd93?.\xad\xc3g\xed\xf5(\xe8\xed\xfcM\xb5\\\x8a\xde\xd4\x04`\xf6E+\xf5\x89\xb7\x1e\x1b|\xf8{R:s\x9cn\x8d\xb3\xb8\x9a\tx\xff\x97O\x15\xf3\xd1+\xea\xcb\xf0\xbb\xfc\xd7\x00+\xc9 \x01\xce\x81b@,dW`\xcfW\x18Y_\xe8yT8\xf0P[\x8e\x16\x99\xb8$F\xa6\xf1L\x8b\xa4\x7f\x1b\xed\x9d\xf2\xb9{\xfa\x1d\xad\xad\xd9b\x12-\xe8DJ\x8a\x0b\xe2\x0c^h\xc0\x1c\xa2\x04\xdc\xed\xfd#\xab?#]~\xa3V[p\xb3?\xb5m6A\xc9x\xa7\x14\xbb\xa6\xdcP\x87:Hp\xa1\x89\x10`\xbd\xca\x1e_`\x86\xa30\xa7\x96\rd\xad\x87x\x03]\xd9\xcdx~[J\x01o2\xbc\xa1y\x88,\xa0\xc1\xf5\x9c\xa2\xeas\xf4\xb4*n\xf0+\xf1N\xd6\xeb<\x05\xc9p\x08\xddF\xb8\xe8\xd0\xedG+ \x922\x82\t\xeaY\xda\x04\x98\x85"\xd1>r\xc45c6;\xcb/w\xfd\xfe\x9cP\xc4E\xd3\x9eb\xe7\xb0\xe8\x80?\xb0\x80\xae\xbe\x8f\xd9\x91\xd9\xc4p\x7f\x15\xd677\x89.\xdcml\xe6\x9dI/\xa1}\x8b:\x143\xfe$\x1f\x99\xdbJ\xdbs\xa2\xc7\x80\x8eB#n\x91\x84\xdd\x16\xfcl\x19&\xc8dS\xb9.L\xe74?\xedx\xda\t\xa4e\xe6Y3\xbf\x8f\xc8\xab\xbe\x9eK\x8e\xeaJ\xf8e\xe6\xabj~r\xcb\x98,m`%\x9ez\xaeh\xc3\xdc\xbd\xdf\x8cG\x9a\xfc2\xf2\x957\x1b\xa16h\xee\xb4M\x0e!,\x1aTm\x83\x19\xc7OA\xa5\xeb\xf0\x15`\xe6\x10\xfc\x86\x81O\xe4\xef\n\xe3b^r\\\xe4v\xc1\x99[\xf1\xbeQ\xdez\xdd\xe4*\xc4\xc9\xeaq3\xc2\x90\x7f F`8\x9cmKb\xc0k\x01\xe6\xbd\xc4\x12\xd0_,h\x0e%lob\x8a\xa9\xde\xeb\xdb\x08u\xcf\x0e\xf3\x90\xd1/P\xa0`d\xd0-\x895\x163\xa6I\xc9j\x8d\xdaT\xe1\x0c\x8aR("\xd9\xe7\xb2tR\xca\x12\xf7\xe12x\x85\xf2\xfb\xac\x81\xc8+\x1c\x0c)(\x99\xfb\xc0;\x9e\xbc{\xb6\xceV\xa5\xae\xc3\xc2\xb9@N\xd4\xf9d\xd0\xbbv\x12\x08\xdd\x18\x88\x8b:\xc8B\xb3K\xdf\x07Oj\xd2\x85\xfa\xad;\xc0\xcf;\x14\xaa\x9a,\x99\xd3\xfcc\\\xd3\xb2\xd80\xbeF\x1a\x00b8o\xb57\xbf\xe4\x14\xca\xfd\x99\xa0\x1f>\x93\x8b(/\xf8\xab2Y\xcfZ\x1d\xbcY^u\xa3v\xf5\xdd\x01I\xa9\xe8\xaf\xaa?\xbbi\xe2\xec\xf3\x8b\t\xb5\xfb\xc6Z\x103\xd0c\x9cS\xd9\xb2\x8c\xea\t\xa1%d\x91\xfd*\x17\xaa\xf6\xb8E\x12\x8c\x8a\xfel\x1et~#\x18\xa2\xfc\ru\xf5\xdf\x89\x80\x89h\xee\x8d\xd2%\xfat\x01\xba+\x8d\xb6\x00\xa6\xbeF\x1c\xe2\x0e\xd2M\xe7\xdf\xcaK}n\x1f\xf0o\xea#\xd3\xa3\x84l\xe4\xect \\\xea\x0cN\x1b\xec\x16A\xef\xdd\xddo\xaa\xf7\x02\xc7\x9a\xee\xef\xc2d\x84\xe9?\x84\xdd).\x0b\xcfv \x1d?\xacN\x17\xb7\xca&\xdf\xdc\xab\xc9\x0c\x7f\xbc]\x94*2\xfea:\xa9\xf6S\xaf\x966\x0f\x01\xbc=\x84\xe8\xf3\x1c\xfd\x8e\xc2X3\xe2f\xe8a\xe1\xcb=\xb3:?=>\x0b4\x91\xd7\x1cU\xe4\xdb\xba\xb0\xba\xeb\xcc\x0f*\xe5\x1dg\x0f\x1a\xbd\x96\xb5\x1e\x92(_\xbaqpp\x8cF\x8e`\xa0F\x86\xfb9\xb18\xea\rT\xdeD+\xdc\x91\x15\xb8|\xf7\x89y\xf24`)B*\xa5\x9f\xa1\xba\x89\x91o\xa5\xe0\xf2\xcd\xcc\x05\x01\x06\xe4\x9b\x87\x9b!\xd2&a7\xe4\x7f\x0e\x9e\xb75l\x87\xa6\x82\x92\\\x8d\xc9\xe7\xbd\xa0\xfe6\xba\xe5\x7fBp\xa2\xb8:\xe0\xd2\xf9\xb8\xc2\x08(Yp\xf6\x89\xf3y\xc4\xcf(\xca\x1eY\xb1\xcaL]\xb0\x9d\x1f\x83Eg\x8bW\x1b\xa1=\x19\xc9\x00\xb4\xcd\x94M`__\x1f\x08\xbb\xfe\xce=\xa7\xfep{\xac\xd7M\x84\xc0C`M\x03F*wW\x7fy\xd8\x91/"L\xdfw<\x14l\xc4\xb4F\x08\x84\x18\xbe\xe1\x90\x1a0}gNL\xd5\xe9\x84Z\x06+4\x99\xacr8s\xb6\x19\xd7z\xc1\xe7B\xf0Dx~2\n\xf9\xeeF\xa2\x84E)\xb1\xed\xaf\xa6P\x0e%\x1c\xe2\x05\xd1\xfa\x16\x15\x86\xa8\xbf\xcfVf\x01\xc8\x03z\xa0z\x11\xd3\x86\xf8^\x0e\xc9Tg\xdf\xf8*AR\xbd\x17\xb6\x93L\x08\xddp\xd7\x1b\xb3w=\xa5\x11w\xa9\xe3\x8aO^\xce\x84^\xd5\xba\xe9\xb8I\xbb\x8f\xe0\x10\x9dC\xc2\xd1QJ\xe0r\xd9\xf0[\r:\x80\xb1\x8e\x89\x8fD\xad\xbc>N\x10\xdd?LO\xb2\xd6\xf0\xd9m\xf5q\xcduP\xec\x97q fR\xc8\xadt\xc9\xd18BKM\xd7v\x13\xc0\x1es\x05-\xea\xe1N1\xe2\xf4b\xab\x9dc\x1b\x81\x1c\xfb*\x81}\x9fJ\xfa\x1d\xff\x07&\xec\xc7\x7f\x8f\x92\xea\xad\xf2\xa6\xe3\x11\xbb\xf0S5t!\x10\xc9\x93<~G\x8f\xadX\x88\t\xa2R\xf4Y6\xd7\xfa\x9ey\x8a\x13\x84\xcd\x8b\xd5o\xdf\x17 \xf4\xe0\xe2\xbc^\xc6\x02\xda~\x8bL\x91\xa0\xf0nj~\x16z \xd7\x8e\t!\x1a\xa3?\x11To\x91\xc0\xc5L\x9em\x7f\xdfil\xff&Y\xb1\xc6\x05\xf7\xb1\x7f#;T\xa38\xe5\xf62I\x96=\x95`\xfeD7\xba\xb3\xc0\xeb0c\x1d$\xa77/\xeb\x1f\x90\r@\xf35\xfc\xc9,3\x08\xf1\xf8\xa6\xa1W\xb2\xe1\x88\xe4\xd3\x90\xd1\xc7\xbe\xac\xeb\xd3\x0f6\x0f\xb7\x15\xc0\xd3\xcb#\n=\xd5n\xa5D\xc0\xcc\x18Z\x0c\xc0\xec\xe6\xde\xbc\x18\xb1n\xe4&\x0f\xc3@)3)r0\x14\xf5G\xdd\xf5\xfah!\x16\x1d\xbcj\xcc\xc4\xd1\x82(({\xdc\xd5\xa3\x85\x05\xf0\xd1&\x16\xd4\xe6\x1d\xcf5Xy\x06\x0f\xc1%E\x9a\x96\xe3\xf9]\x9c\xa3\xb3O\x04\x11\x98E\x06\xe1(\x1e\xfd\xac\xb3V\x98O! \xfb\x98\xba\xe43iB\xda\xed8\xb0\xba\xa0\x0b9[\x9d ZI\xe1\xffa\x14\xe4S\x1ejcE\xc2\x92\x930\x91\x9a\xf4iR\xd2\x98\x89\xf6\xca\xbamNP\r~Q\xfa\x06p\xf55\xb0\x86H\x1f\xda\xe8\x97\x02J\xf6\xe86\xdc\x89\xe3.\xb9LjPI\nP;\x8c\xac!\xc0\xe78]\xf8\x05h\xde\xdc\xa6K\\c\x1f\xa6o\xa3\xa2\x0c\t\xce\xf0\xeco\xe3\x05\xc3\xa4\x8e\x94\x0b\xc8\x8bZ\xc3p\xa3\xf0\xdf\xa2F\x1c\x0bk\xee\x002^\\\xa6\x97\xa0UZ\x15\xbe\xbd\x8f\xc6\xd6\xaf\x08o\xa9?\xd7/\x94k\xdcqh\xd5y\x1a\xb1$\x84\x9a|+\xc3\xae+\xb7\xb1\xb8\xd8Z\xc8\x98\x17^{BF\xe7s!<L\xdd=\x840E\x99\xfc\xb8\xb7#\xc2*\xa4\xab\xfb\xa8\x8a\xbb\x84J\xcd\x8d\xa55\x87T\x9c\xc3\x00\xdb\xe2Mpf\xf7\xb5&\xab\xe3\x9d\xc76g9Hb\xa8\x1d\x01\xff/-\x11\xc2\r\x01L\xd3C1F\x9c\x96\xe4-\x19xv\xc0\xaf\'\xd2\x80:\xa2w\xc1\xe6\r\xd28)yG\xc3[\x8c.\x07\xc5\x04I9O\xaf5\x07;\x100\xf0d\xd4\xc9\xe0F\xc3\xc8Q@\\Ut\x17\xe4\x1c\xd7X\xbb\xef\x00\xaf\xe1@\xda\x06\x90u\xaa\xa4\xd5)*\xe3\xde\xb2\xbei\xbd\xce\xdcC_\x85\xa5\xe3\tA\x94F\x8f(\x8fw\xc2)u\xed\xa731\xe0{\x96\xc1\x08\xd6\xf0\x983\xdeaR=r,)]x?\xc9s\x930\x1d\x18tx|b\xc9\xc3\x98_8X\x94 \xf7\x1b\xf4\xf8 \x86\x970\x08\xfc\xe2\xd4\x80\xdeo\xffB\x0f\xec1C\xad\xec\xa2\xc5(*ug\xd8\x97}%\x10\xe9*2\xabS\x82\xc4\x8c\x82\x0f\xa4{S\xa8\x0b\x80\xe4\xd42~\xb1\xd5\xfa\xc0/\x0f\x05(C\xc5N\x8dG\xba\xb7]Z\x00V\xcb\x8d\xeecY\\jU\xd1\x0ch\xfd4\xed;\x82\x92\xe6o\x08|c\x12"\xb1\x9e.\xf2\xf1v\x0b~\xfbS<\x8bWh.\xcf:>\xbf\x0b\x19\xb3\x14\x03\x9d\xba\xa7\x1e\xf3WT\x88\x99\x9f9\xdc05\xdf\x05\x93\x1e$\x99l\x12\xcb9l\xf3\xb4\xfa\xb6\xe7\xc3\xd7\x8d\xfbB\xd9w\xc1\xc3\x19\xb3\xfa\xa2gfF6\x8b\x86\xeb1\x827\xb8%\x0c\r.B\x1a\xae<\xf09o\x05\xa9Y\xe9\xf6\xf3[_J\x16\xbd\xe8\x07P\x9cv\xb3\x1coB\x1e~\xd7K5\xb5:\xf5Y\x83\xfb\xdb\x17LY\xf4\x93\x11\x0bq\xfd\xa2\xd1\x87\x7f\x98\xddY\x98\xc1|\x94\x8eO\x7f\x9e;\x9eqG\x0eue\x14b\xf4\xdd\x997f\xd2\x89M\x8e/\xee\xd2\x13$\xecm\x1d\xae\x080^\'U\x1a_\'~\xbd:d$s\xc2!\xe3\x9c\xda\xfc:\x17W!\xc7nb\x05\xfe7\xf28\xb9\xdeA\x89\xe2\xbb69\xb1\x16,\x1b\xf7\xf5H\x15z\x10\xb7;p{\xc7\x06i\xd1\xe4\x95\xb8\x81\x8f];LY\xfc\xbf]\xa5l\xff\x08H\xcb\xfc\x12\xbb_\xa8?1\\\xe8xD\x0b Q\xd9\x16\xb8U0\x99\xce\xaf\xd6\xafs\x1f\xb6h/\x17\x85\xeb\x1c[\xc7\xea6}d\x93\xc2\xbc\x1c\xa7\x90\xd7B/V\x9a\xa2o\x8d\xb0\x87\xda\xc2\x06\xd8\x80\x9bd\xd5%\xed\x96.\xb1~\xbb\xab8J\xbel\x80\rzlk\xe8\xca\xa6*\xf7bL_\xf3\xe8\xe3s\xeb\x13g~b\xfe\x1c\xa5]\x1e\x98\xd2I\xea\xd5\xbc\xf4q\xfb\xa2\n\x11\xcd\xcf\xa0~V\xa0P\xc3K\xd6\xe4\xc0\x9c\xb3\x93\x9b\xa8\xbd\xe9\x81;v\x8b9\xf5\x8d\xac\x7f\xa8\xb0\xd5\xf7R%j\xd0\x00d\xea\xcf9\x8a\xb2\x8e\xf0\x1c\xb3P\xfb\x86\x03\xae\xb2\x10\x9d\xdbw\xe2p#\xb3\xe8\xdc\x17\xd2\x85l\xd4]N\xffeY\x16\x07\x13H\x82\x81\x9e\xe7\xe8(=\x16H\xfe\x98U\xabw\xf8\x98$t\xfd\x0b1\xcc\x8e\x9d4\xa8\xc3\xbd\xe1\x82R\xf9<\t\x1fJi\x12\xf2\xea\x9f\xef,\xc3\xe5\xb0\xc9y@s\x8a\x00\xab(frU\xad\ru\x15ws\xb8\x1b?\x18\x86\xdb\xcc\xe6\xca\xd3\x89\xfa\xceS\xfa\x0b\x1b\xc0=\xb4<\xe3\xf6\x05{\xacD\xb5\xb8\x92L\xf1!\xe0\xe7\xb8\x00\xb0{\xf0j\xef\xf5\x84L\x1e\xf2&\x18:\xc3\xd2\x0c\xad\x90R?FY\x86i\xa8\xa88\xd7\xa0\xdb\xdf\x92\x1b\xab\\\x16\xfbn\x11\xef\xbcq\xe8JOf\xc0\xdaQ\x99\xbfB\x19\xec\x8f\x9c\x1f\xca\xc35\xd4\x83H_\x00\xf5 E\xab\xe6\xe8z\xff\x0e\xd4{\r\xb9\x08\n\xb9\xd2Sv\x0b\x05x\xc4f>J<\xcfp\xd1\nMz}+\x0c\x18@n1\x89c\x86-\xdbjq\xe0\x18t\xad]\x86\xc1\xab>|\xe2\x02/+\xa4\xd9\xbb\xfb\x9eg\x9a\x8c\xfe\x9a\x0e\x98\xe7|\xb9\x96\xd8/\xf0\x18\xb7\x92\x15\xafZ\x9dEk\x9f_\x0c\xc8H)\x84\n+\xf0,\xa8q\xa0)\x0b-l\x8e\x1e\xa3D\xa3\x18T\x8b\xf2\tU\x12\xd8\xef/\xb6\xd2\x87\xf94 pL\xe8V\xc5\x1e\x05\xad\xa44\xb6\x11JXS\x1c\x12^v\xda\xee\x80\xf1\x1499\xe2\xe49\xf1,\x82(\xd5jo)\xae\xd9\x90\x86\xd6\xc8\xae\xb6K\xa3\xc0,\xf9m8\x8e\xc3\x90I\x9b\r9\xfdj\xc1n\xafl\xa2/\x92\x81\x0c\xcb?\x8f\x8f\xccj\x83[\xe0\xea\xfc\xe8\x02\xbf\xefc~]Ib\xbe\x8b\x84\x90\x0c\xaeH\xf4\xf6\xd0\xa5\xf35\xe87\xb5\xcd>^\x1a\xe9\\\xf7\x81\xf7\xd0\xf3;=\xc4\xf7\x8f[\xea\xf3\xc7\x12XM\x94fk\x19^\x8a\x8f^\xeb\xd9Gc\x8a\xa4\x96\xb2,\xc3e\x9b\xf0\\\x83R\xb0\xb4\xec\xd7\xfcJ\xa0\xae\x00\x19u/\'v\xfe\xcd\x86@\xc5\xd6\xc2\xa8|\xae\xb4\x8a\xc9\xf3G7\xb1\x13^\x97\xc5\x11"\xc7\xf6\x05`\x9c\xea\x18\x87Z\xb6\xfdn2H\xe7\xde\xccy~j\x00Qc\xcb\xa1\xfc\x19>\x82u\xb8\x1e\x11~+s4\x8c\xdd1S\xd1\x01\xae\xe6!\xcd\xaa\x10\r\xc3l\xccE\xc4\xb8W\xeaw\rD\x8a\x07\x82,^ibI\x9b?\xbf\x8av_\x10w\x98\xeb\xfei\xa2\x14\xb3\x16\x9ey)z\xb2R\xfe\x89\xa3\x1b\x8a\x15\x0c\xfb\xac:<\x0ej\xbe\xcd\xfd\xc8y\x81\x03\x80b\xa6\x08\xcc\xcb\xff\x17rE8P\x90c\x9dHk')))
except KeyboardInterrupt:
    exit()
