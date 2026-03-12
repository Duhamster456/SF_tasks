from flask import Flask, render_template, request

GET_HELP = '''
Чтобы получить интересующие Вас данные, установите параметр запроса info

/api?info=get_flag - о получении флагов
/api?info=other - не о получении флагов
'''

GET_FLAG = '''
Отправьте POST-запрос с json в теле:

{\"get_flag\": true}
'''

CURL_DEFAULT_CONTENT_TYPE = "application/x-www-form-urlencoded"

FLAG = "FLAG{now_it_is_correct_345678965434567}"
ERR_INCORRECT_DATA = "Ошибка: некорректные данные"
ERR_NO_MIME = "Ошибка: не удалось распознать MIME-тип. Укажите его явно в заголовке Content-Type"
ERR_INCORRECT_MIME = "Ошибка: не удалось распознать MIME-тип"
ERR_NEED_LOCALHOST = "Доступ запрещён. Подключение доступно только с адреса 127.0.0.1. "
ERR_NO_X_FORWARDED_FOR = "Заголовка X-Forwarded-For не обнаружено"
ERR_NOT_BROWSER = "Доступ запрещён. В заголовке User-Agent нет подстроки \"Mozilla\", значит Вы - не браузер. Подключение доступно только с браузера."

app = Flask(__name__)

@app.route("/")
def root():
	return render_template("root.html")

def api_get():
	get_info = request.args.get("info")
	if get_info == "get_flag":
		return GET_FLAG
	if get_info == "other":
		return "403 Forbidden", 403
	return GET_HELP

def api_post():
	data = request.get_json(silent=True)
	data_force = request.get_json(silent=True, force=True)
	if data is None:
		if data_force is None:
			return ERR_INCORRECT_DATA
		content_type = request.headers.get("Content-Type")
		if content_type is None or content_type == CURL_DEFAULT_CONTENT_TYPE:
			return ERR_NO_MIME
		return ERR_INCORRECT_MIME
	
	x_forwarded = request.headers.get("X-Forwarded-For")
	if x_forwarded is None:
		return ERR_NEED_LOCALHOST + ERR_NO_X_FORWARDED_FOR, 403
	client_ip = x_forwarded.split(',')[0].strip()
	if client_ip != "127.0.0.1":
		return ERR_NEED_LOCALHOST + f"Исходный адрес клиента: {client_ip}", 403
	
	user_agent = request.headers.get("User-Agent", "")
	if not "Mozilla" in user_agent:
		return ERR_NOT_BROWSER, 403
	if data.get("get_flag") == True:
		return FLAG

@app.route("/api", methods=["GET", "POST"])
def api():
	if request.method == "GET":
		return api_get()
	if request.method == "POST":
		return api_post()
		
if __name__ == "__main__":
	app.run()