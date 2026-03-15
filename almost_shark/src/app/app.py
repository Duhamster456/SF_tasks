from flask import Flask, render_template, request, redirect

FLAG = "FLAG{i_made_that_with_docker_compose_123947348728347832}"
app = Flask(__name__)

REGISTER_INFO = '''
Отправьте POST-запрос с json в теле со следующими ключами:

\"login\" - Ваш логин
\"password\" - Ваш пароль
'''

REGISTER_GOOD = '''
Отлично!
'''

REGISTER_BAD = '''
Ошибка! Некорректные данные...
'''

@app.route("/")
def root():
	return redirect('/register', code=301)

def register_post():
	data = request.get_json(silent=True)
	if data is None:
		return REGISTER_BAD
	if data.get("login") is not None and data.get("password") is not None:
		return REGISTER_GOOD
	return REGISTER_BAD


@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method in ["GET", "HEAD"]:
		return REGISTER_INFO
	if request.method == "POST":
		return register_post()

if __name__ == "__main__":
	app.run()