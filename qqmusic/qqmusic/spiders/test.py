import requests

detailHeader = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cookie": "tvfe_boss_uuid=1570fc77f158dc83; RK=ZfvD5WBKXj; _gscu_661903259=99136450hr2ez712; pgv_pvi=7741724672; mobileUV=1_15d315f403b_8a49e; pac_uid=1_1035407623; pgv_pvid=6600946934; o_cookie=1035407623; pt2gguin=o1035407623; ptcz=14a5a45f650a940dad4aa72caac550db2f382b5b06f008317e286dc110285a2c; luin=o1035407623; 3g_guest_id=-8761071944163352576; g_ut=2; AMCV_248F210755B762187F000101%40AdobeOrg=-1891778711%7CMCIDTS%7C17679%7CMCMID%7C81993840608289446074895381949754338905%7CMCAAMLH-1528035698%7C11%7CMCAAMB-1528035699%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCAID%7CNONE%7CMCOPTOUT-1527438098s%7CNONE%7CMCSYNCSOP%7C411-17686%7CvVersion%7C2.4.0; eas_sid=V155p2g7z479L5R4q0A5p6k7y3; ptui_loginuin=1035407623; lskey=00010000bc18f49cfdd85fa83da83bd460721b5032b043d2c9b5410dd41899cd80a043454238d726e9aa8537; pgv_info=ssid=s229662400; ts_refer=ADTAGmyqq; ts_uid=5514546086; pgv_si=s1659295744; yqq_stat=0; ts_last=y.qq.com/portal/playlist.html",
    "referer": "https://y.qq.com/n/yqq/playsquare/3732331276.html",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
}

url = 'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid=3732331276&format=jsonp&g_tk=128941526&jsonpCallback=playlistinfoCallback&loginUin=1035407623&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
detail = requests.get(url, headers=detailHeader)

print(detail.text)
