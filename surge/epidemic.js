/*

[Script]
# > 昆明医科大学疫情签到获取cookie (xg.kmmu.edu.cn)
昆明医科大学疫情签到 = type=http-request, pattern=^https?:\/\/xg\.kmmu\.edu\.cn\/SPCP\/Web\/Report\/Index, requires-body=1, max-size=-1, script-path=https://raw.githubusercontent.com/chiupam/Epidemic/master/sruge/epidemic.js
# > 昆明医科大学疫情签到
昆明医科大学疫情签到 = type=cron, cronexp="13 13 13,23 * * *", wake-system=1, timeout=180, script-path=https://raw.githubusercontent.com/chiupam/Epidemic/master/sruge/epidemic.js

[MITM]
hostname = %APPEND% xg.kmmu.edu.cn

*/

var appName = '🌼 昆明医科大学疫情签到 🌼'
var $ = Env()
var cookie = {"Cookie": $.read("CookieEpidemic")}
let isGetCookie = typeof $request !== 'undefined'
if (isGetCookie) {set_body()} else {sign()}

function set_body() {
  if ($request.body) {
    $.set($request.headers.Cookie, "CookieEpidemic")
    $.set($request.body, "BodyEpidemic")
    $.msg(appName, "【成功】写入数据包成功！🎉", $request.headers.Cookie)
  } else {
    $.msg(appName, "", "【失败】无法读取 body 啊，自查原因！🤦‍♂️")
  }
  $.done()
}

function sign() {
	const report = {
		url: "https://xg.kmmu.edu.cn/SPCP/Web/Report/Index", headers: cookie,
		body: $.read("BodyEpidemic")
	}
	$.post(report, (err, resp, data) => {
		$.log(data)
	}
}

function Env() {
  SL = () => {return undefined === this.$httpClient ? false : true}
  QX = () => {return undefined === this.$task ? false : true}
  read = (key) => {
    if (SL()) return $persistentStore.read(key)
    if (QX()) return $prefs.valueForKey(key)
  }
  set = (key, val) => {
    if (SL()) return $persistentStore.write(key, val)
    if (QX()) return $prefs.setValueForKey(key, val)
  }
  msg = (title, subtitle, body) => {
    if (SL()) $notification.post(title, subtitle, body)
    if (QX()) $notify(title, subtitle, body)
  }
  get = (url, cb) => {
    if (SL()) {$httpClient.get(url, cb)}
    if (QX()) {url.method = 'GET'; $task.fetch(url).then((resp) => cb(null, {}, resp.body))}
  }
  post = (url, cb) => {
    if (SL()) {$httpClient.post(url, cb)}
    if (QX()) {url.method = 'POST'; $task.fetch(url).then((resp) => cb(null, {}, resp.body))}
  }
  put = (url, cb) => {
    if (SL()) {$httpClient.put(url, cb)}
    if (QX()) {url.method = 'PUT'; $task.fetch(url).then((resp) => cb(null, {}, resp.body))}
  }
  log = (message) => console.log(message)
  done = (value = {}) => {$done(value)}
  return { SL, QX, msg, read, set, get, post, put, log, done }
}
